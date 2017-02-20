from targets.dice_dojo.actions.dojo import card_search, get_class, create_products, create_cards
from utils.settings import config

query_card = 'World Breaker'
card_classes = ['variant_info', 'price', 'qty']
dev_card_class = 'product_row'
dojo_url = config['source']['dice_dojo']

card_query = card_search(dojo_url, query_card)

if card_query:
    card_results = get_class(card_query, dev_card_class)

    if card_results:
        products = create_products(card_results)

        example = create_cards(products)

        for e in example:
            print e.__dict__
