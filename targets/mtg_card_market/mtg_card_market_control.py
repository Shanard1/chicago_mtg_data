from targets.mtg_card_market.actions.card_market import market_card_search, get_class, create_products, create_cards
from utils.settings import config

#query_card = 'Wooded Foothills'
#card_classes = ['variant_info', 'price', 'qty']
dev_card_class = 'product'
card_market_url = config['source']['mtg_card_market']


def mtg_card_market_lookup(card):
    card_query = market_card_search(card_market_url, card)

    if card_query:
        # print card_query
        card_results = get_class(card_query, dev_card_class)

        if card_results:
            products = create_products(card, card_results)
            #print products
            if products:
                cards = create_cards(products)

                if cards:
                    print 'Card Market Output ########'
                    for output_card in cards:
                        print output_card.__dict__

