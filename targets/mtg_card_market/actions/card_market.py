import re

from bs4 import BeautifulSoup

from targets.card_models import CardMarketCard
from utils.browser import br


def market_card_search(url, card):
    # Returns a browser object from a URL
    try:
        br.open(url)
    except Exception as e:
        print e
    try:
        market_url_query = get_url_query(url,  card)
    except Exception as e:
        print 'Query error: ', e

    search_results_url = 'http://www.mtgcardmarket.com/products/search' + market_url_query

    return search_results_url


def get_url_query(url, card):
    br.select_form('search-form')
    br.form['q'] = card
    card_market_browser = br.submit()
    search_url = card_market_browser.geturl()
    url_query = search_url.replace(url, '')

    return url_query


def get_class(url, card_class):

    results = []


    try:
        search_results_page = br.open(url)
        search_html = search_results_page.read()
        search_soup = BeautifulSoup(search_html)
        product_table = search_soup.findAll('li', {'class': card_class})
    except Exception as e:
        print e
    category_names = BeautifulSoup(str(product_table)).stripped_strings
    for cat in category_names:
        if cat not in [',', '[', ']', ':']:
            results.append(cat.encode('utf-8'))
    return results


def create_products(card_name, card_list):

    '''
    :param card_list: cleaned list of strings from website data
    :return: list of lists broken out by card variant
    '''

    product_rows = []

    product_row_markers = []

    for i in xrange(len(card_list)):
        if str(card_list[i]).startswith(card_name):
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
        if len(product_row) == 8 and product_row[3] != 'Out of Stock':
            #print '{} is the quantity'.format(int(re.search(r'\d+', product_row[3]).group()))
            new_card = CardMarketCard(
                name     =str(product_row[0]),
                set      =product_row[1],
                condition=product_row[5],
                qty      =int(re.search(r'\d+', product_row[3]).group()),
                price    ='{:.2f}'.format(float(product_row[7].strip('$')))
            )
            created_cards.append(new_card)
        elif len(product_row) == 8:
            #print 'Out of stock'
            new_card = CardMarketCard(
                name     =str(product_row[0]),
                set      =product_row[1],
                condition=None,
                qty      =0,
                price    ='{:.2f}'.format(float(product_row[6].strip('$')))
            )
            created_cards.append(new_card)
        else:
            #print 'Multiple {} {} cards will be made'.format(len(product_row), (len(product_row)-5)/3)
            card_qty = (len(product_row)-5)/3
            for i in xrange(card_qty):
                new_card = CardMarketCard(
                    name     =str(product_row[0]),
                    set      =product_row[1],
                    condition=product_row[(i*3)+5],
                    qty      =int(re.search(r'\d+', product_row[(i * 3)+6]).group()),
                    price    ='{:.2f}'.format(float(product_row[(i*3)+7].strip('$')))

                )
                created_cards.append(new_card)
    return created_cards

'''
['Wooded Foothills', 'Onslaught', '$27.00', 'Out of Stock', 'View Product', 'Add to wishlist to be notified when the item is in stock.', '$27.00', 'Wishlist',
 'Wooded Foothills', 'Khans of Tarkir', '$16.40', 'Out of Stock', 'View Product', 'Add to wishlist to be notified when the item is in stock.', '$16.40', 'Wishlist',
 'Wooded Foothills - Foil', 'Onslaught', '$150.00', '2 In Stock', 'View Product', 'NM-Mint, English,', '1 In Stock', '$150.00',
                                                                                  'Light Play, English,', '1 In Stock', '$120.00',
 'Wooded Foothills - Foil', 'Battle For Zendikar - Expeditions', '$92.00', '1 In Stock', 'View Product', 'NM-Mint, English,', '1 In Stock', '$92.00',
 'Wooded Foothills - Foil', 'Khans of Tarkir', '$43.90', 'Out of Stock', 'View Product', 'Add to wishlist to be notified when the item is in stock.', '$43.90', 'Wishlist',
 'Wooded Foothills - Foil DCI Judge Promo', 'Promos: Judge Rewards', '$110.00', 'Out of Stock', 'View Product', 'Add to wishlist to be notified when the item is in stock.', '$110.00', 'Wishlist']

'''