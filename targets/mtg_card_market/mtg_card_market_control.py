from targets.mtg_card_market.actions.card_market import market_card_search, get_class, create_products, create_cards
from utils.settings import config

dev_card_class = 'product'
card_market_url = config['source']['mtg_card_market']


def mtg_card_market_lookup(card):

    card_output = []

    card_query = market_card_search(card_market_url, card)

    if card_query:
        card_results = get_class(card_query, dev_card_class)

        if card_results:
            products = create_products(card, card_results)

            if products:
                cards = create_cards(card, products)

                if cards:
                    for output_card in cards:
                        card_output.append(output_card.to_gui())

                return card_output

