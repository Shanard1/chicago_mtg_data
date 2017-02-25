from targets.mtg_card_market.mtg_card_market_control import mtg_card_market_lookup
from targets.dice_dojo.dice_dojo_control import dice_dojo_lookup

query_card = 'Transgress the Mind'

def card_lookup(card):
    mtg_card_market_lookup(card)
    dice_dojo_lookup(card)

if __name__=='__main__':
    card_lookup(query_card)