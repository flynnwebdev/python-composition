class Currency:
  def __init__(self, gold, silver, copper):
    self.__gold = gold
    self.__silver = silver
    self.__copper = copper

  @property
  def value(self):
    return self.__gold, self.__silver, self.__copper

  @value.setter
  def value(self, value_tuple):
    gold, silver, copper = value_tuple
    self.__gold = gold
    self.__silver = silver
    self.__copper = copper

  def __add__(self, other):
    return Currency(
      gold=self.__gold + other.__gold,
      silver=self.__silver + other.__silver,
      copper=self.__copper + other.__copper
    )

  def add(self, gold, silver, copper):
    self.__gold += gold
    self.__silver += silver
    self.__copper += copper

  def __iadd__(self, other):
    if not isinstance(other, Currency):
      raise TypeError('Can only add Currency to Currency')
      
    return Currency(
      gold=self.__gold + other.__gold,
      silver=self.__silver + other.__silver,
      copper=self.__copper + other.__copper
    )

  # Developer-friendly representation
  def __repr__(self):
    return f'Currency(gold={self.__gold}, silver={self.__silver}, copper={self.__copper}))'

  # End-user readable representation of the object
  def __str__(self):
    return f'{self.__gold}G {self.__silver}S {self.__copper}C'


class Character:
  def __init__(self, name, race, health, attack):
    self._name = name
    self.race = race
    self.health = health
    self.attack = attack
    self.wallet = Currency(0, 0, 0)

  def battle(self, other):
    print(f'{self._name} launches a melee attack at {other._name}!')


class Mage(Character):
  def __init__(self, name, race, health, attack, mana):
    super().__init__(name, race, health, attack)
    self.mana = mana

  def show_gold(self):
    print(f'{self._name} has {self.wallet.__gold} gold')

  def battle(self, other):
    print(f'{self._name} casts a wicked spell at {other._name}!')

  def portal(self, destination):
    print(f'{self._name} opens a portal to {destination}!')


class Burglar(Character):
  def battle(self, other):
    print(f'{self._name} sneaks in a stealth attack on {other._name}!')


class Warlock(Mage):
  pass

class Chest:
  def __init__(self, items, gold, silver, copper):
    self.items = items
    self.cash = Currency(gold, silver, copper)

  # Transfer chest contents to character
  def loot(self, character):
    character.wallet += self.cash
    self.cash.value = 0, 0, 0
