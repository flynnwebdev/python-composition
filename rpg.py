class Currency:
  def __init__(self, gold, silver, copper):
    self.gold = gold
    self.silver = silver
    self.copper = copper

  def set(self, gold, silver, copper):
    self.gold = gold
    self.silver = silver
    self.copper = copper

  def add(self, gold, silver, copper):
    self.gold += gold
    self.silver += silver
    self.copper += copper

  def add_currency(self, currency):
    self.add(currency.gold, currency.silver, currency.copper)

  # Developer-friendly representation
  # def __repr__(self):
  #   return f'Currency(gold={self.gold}, silver={self.silver}, copper={self.copper}))'

  # End-user readable representation of the object
  def __str__(self):
    return f'{self.gold}G {self.silver}S {self.copper}C'


class Character:
  def __init__(self, name, race):
    self.name = name
    self.race = race
    self.wallet = Currency(0, 0, 0)

class Chest:
  def __init__(self, items, gold, silver, copper):
    self.items = items
    self.cash = Currency(gold, silver, copper)

  # Transfer chest contents to character
  def loot(self, character):
    character.wallet.add_currency(self.cash)
    self.cash.set(0,0,0)
