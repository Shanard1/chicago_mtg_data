class DiceDojoCard:

    # http://stackoverflow.com/questions/8187082/how-can-you-set-class-attributes-from-variable-arguments-kwargs-in-python

    def __init__(self, name, set, condition, qty, price):
        self.name      = name,
        self.set       = set,
        self.condition = condition,
        self.qty       = qty,
        self.price     = price


class CardMarketCard:

    def __init__(self, name, set, condition, qty, price):
        self.name      = name,
        self.set       = set,
        self.condition = condition,
        self.qty       = qty,
        self.price     = price

'''
class Foo:
  def setAllWithKwArgs(self, **kwargs):
    for key, value in kwargs.items():
      setattr(self, key, value)
'''