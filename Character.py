class Character:
    def __init__(self, **kwargs):
        self._name = kwargs['name'] if 'name' in kwargs else 'Jabronte'
        self._health = kwargs['health'] if 'health' in kwargs else 100
        self._attack = kwargs['attack'] if 'attack' in kwargs else 10
        self._defense = kwargs['defense'] if 'defense' in kwargs else 10

    def name(self, t = None):
        if t: self._name = t
        return self._name

    def health(self, t = None):
        if t: self._health = t
        return self._health

    def attack(self, t = None):
        if t: self._attack = t
        return self._attack

    def defense(self, t = None):
        if t: self._defense = t
        return self._defense

def print_character(c):
    if not isinstance(c, Character):
        raise TypeError('print_character(): requires a Character')
    print('{} has {} health, {} attack and {} defense.'.format(c.name(), c.health(), c.attack(), c.defense()))

def main():
    hero = Character(name = 'Jabronte', health = '100', attack = 9000, defense = 100)
    print_character(hero)


if __name__ == '__main__': main()
