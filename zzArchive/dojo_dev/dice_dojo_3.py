from bs4 import BeautifulSoup

from utils.settings import config
from utils.browser import br


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


def get_class(url, class_list):

    results = {}

    try:
        # Attempts to pull back information about a card
        search_results_page = br.open(url)
        search_html = search_results_page.read()
        search_soup = BeautifulSoup(search_html)
        #product_table = search_soup.findAll('tr', {'class': 'product_row'})
        #for card_class in class_list:
        #    print card_class[0], card_class[1][0], card_class[1][1]
        for card_class in class_list:
            results[card_class[1][1]] = []
            product_row = search_soup.findAll(card_class[0], {card_class[1][0]: card_class[1][1]})
            values = BeautifulSoup(str(product_row)).stripped_strings
            for v in values:
                if v not in [',', '[', ']', ':']:
                    results[card_class[1][1]].append(v.encode('utf-8'))
    except Exception as e:
        print e

    return results


# Get the values that we need to complete the search
query_card = 'Thought-Knot Seer'
card_classes = [['span', ['class', 'category_name']],
                ['span', ['class', 'info']],
                ['td',   ['class', 'price']],
                ['td',   ['class', 'qty']]]
dojo_url = config['source']['dice_dojo']

card_results = {}

# Search for the card
card_query = card_search(dojo_url, query_card)
if card_query:
    # Returns the prices they have
    card_results = get_class(card_query, card_classes)

print card_results
# Return a bunch of values for the card

# Save all our values