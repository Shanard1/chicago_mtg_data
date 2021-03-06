from targets.dice_dojo.actions.dojo import card_search, get_class, create_products, create_cards
from utils.settings import config

dev_card_class = 'product_row'
dojo_url = config['source']['dice_dojo']


def dice_dojo_lookup(card):

    dojo_output = []

    card_query = card_search(dojo_url, card)

    if card_query:
        card_results = get_class(card_query, dev_card_class)

        if card_results:
            products = create_products(card_results)

            cards = create_cards(card, products)

            if cards:
                for card_dict in cards:
                    dojo_output.append(card_dict.to_gui())

            return dojo_output
