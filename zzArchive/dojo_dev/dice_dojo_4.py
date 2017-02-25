from bs4 import BeautifulSoup

from targets.card_models import DiceDojoCard
from utils.browser import br
from utils.settings import config, dev

def card_search(url, card):
    # Returns a browser object from a URL
    try:
        br.open(url)
    except Exception as e:
        print e
    try:
        br.select_form(predicate=lambda f: f.attrs.get('method', None) == 'get')
        card_search = br.form.find_control('query')
        card_search.value = card
        dojo_browser = br.submit()
        search_results = dojo_browser.geturl()
    except Exception as e:
        print e
    return search_results


def get_class(url, card_class):

    results = []

    if not dev:
        try:
            # Attempts to pull back information about a card
            search_results_page = br.open(url)
            search_html = search_results_page.read()
            search_soup = BeautifulSoup(search_html)
            if card_class != 'variant_info':
                product_table = search_soup.findAll('td', {'class': card_class})
            else:
                product_table = search_soup.findAll('span', {'class': 'category_name'})
            category_names = BeautifulSoup(str(product_table)).stripped_strings
        except Exception as e:
            print e
        for cat in category_names:
            if cat not in [',', '[', ']', ':']:
                results.append(cat.encode('utf-8'))
    else:
        try:
            search_results_page = br.open(url)
            search_html = search_results_page.read()
            search_soup = BeautifulSoup(search_html)
            product_table = search_soup.findAll('tr', {'class': card_class})
        except Exception as e:
            print e
        category_names = BeautifulSoup(str(product_table)).stripped_strings
        for cat in category_names:
            if cat not in [',', '[', ']', ':']:
                results.append(cat.encode('utf-8'))
    return results


def create_products(card_list):

    '''
    :param card_list: cleaned list of strings from website data
    :return: list of lists broken out by card variant
    '''

    product_rows = []

    product_row_markers = []

    for i in xrange(len(card_list)):
        if str(card_list[i]) == 'Use arrow keys to navigate.':
            product_row_markers.append(i)

    for i in product_row_markers:
        if product_row_markers.index(i) != len(product_row_markers) - 1:
            item_end = product_row_markers[product_row_markers.index(i) + 1]
            product_row = card_list[i:item_end]
            product_rows.append(product_row)
        else:
            product_row = card_list[i:]
            product_rows.append(product_row)

    return product_rows


def create_cards(product_list):
    '''
    :param product_list: list of lists broken out by card variant
    :return: each card variant as a class
    '''

    created_cards = []

    for product_row in product_list:
        if len(product_row) < 7:
            new_card = DiceDojoCard(
                name     =str(product_row[2]),
                set      =product_row[3],
                condition=None,
                qty      =0,
                price    ='{:.2f}'.format(float(product_row[5].strip('$')))
            )
            created_cards.append(new_card)
        else:
            card_qty = (len(product_row)-3)/4
            for i in xrange(card_qty):
                new_card = DiceDojoCard(
                    name     =str(product_row[2]),
                    set      =product_row[(i*4)+3],
                    condition=product_row[(i*4)+4],
                    price    ='{:.2f}'.format(float(product_row[5].strip('$'))),
                    qty      =int(product_row[(i * 4)+6].strip('x '))
                )
                created_cards.append(new_card)

    return created_cards



'''
letter_groups_to_make = (len(numbers)-3)/4

for i in xrange(letter_groups_to_make):
    print i, numbers[2], numbers[(i*4)+3], numbers[(i*4)+4], numbers[(i*4)+5], numbers[(i*4)+6]
'''


# Get the values that we need to complete the search
query_card = 'World Breaker'
card_classes = ['variant_info', 'price', 'qty']
dev_card_class = 'product_row'
dojo_url = config['source']['dice_dojo']

card_results = {}

# Search for the card
card_query = card_search(dojo_url, query_card)

if not dev:
    if card_query:
        # Returns the prices they have
        for c in card_classes:
            card_results[c] = get_class(card_query, c)

    print card_results
    print len(card_results['variant_info'])
else:
    card_results = get_class(card_query, dev_card_class)

    products = create_products(card_results)

    print products

    example = create_cards(products)
