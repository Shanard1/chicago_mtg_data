from targets.mtg_card_market.mtg_card_market_control import mtg_card_market_lookup
from targets.dice_dojo.dice_dojo_control import dice_dojo_lookup

query_card = 'Tarmogoyf'


def card_look_up(card):
    market_cards = mtg_card_market_lookup(card)
    dojo_cards = dice_dojo_lookup(card)

    return {'market_cards': market_cards, 'dojo_cards': dojo_cards}

if __name__=='__main__':
    card_look_up(query_card)