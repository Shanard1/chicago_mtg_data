class DiceDojoCard:

    # http://stackoverflow.com/questions/8187082/how-can-you-set-class-attributes-from-variable-arguments-kwargs-in-python

    def __init__(self, name, set, condition, qty, price):
        self.name      = name,
        self.set       = set,
        self.condition = condition,
        self.qty       = qty,
        self.price     = price

    def to_gui(self):
        card_d = {}
        card_d['name']      = ''.join(map(str, self.name))
        card_d['set']       = ''.join(map(str, self.set))
        card_d['condition'] = ''.join(map(str, self.condition))
        card_d['qty']       = ''.join(map(str, self.qty))
        card_d['price']     = ''.join(map(str, self.price))
        return card_d


class CardMarketCard:

    def __init__(self, name, set, condition, qty, price):
        self.name      = name,
        self.set       = set,
        self.condition = condition,
        self.qty       = qty,
        self.price     = price

    def to_gui(self):
        card_d = {}
        card_d['name']      = ''.join(map(str, self.name))
        card_d['set']       = ''.join(map(str, self.set))
        card_d['condition'] = ''.join(map(str, self.condition))
        card_d['qty']       = ''.join(map(str, self.qty))
        card_d['price']     = ''.join(map(str, self.price))
        return card_d
