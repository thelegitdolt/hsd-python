import json
import core.hsdownloader as hsd
from core.cardenums import *


class Card:
    def __init__(self):
        self.id = ''
        self.dbfId = None
        self.name = ''
        self.text = ''
        self.flavor = None
        self.artist = None
        self.attack = None
        self.cardClass = CardClass.INVALID
        self.classes = None
        self.collectible = False
        self.cost = None
        self.elite = False
        self.race = None
        self.isMiniSet = False
        self.races = []
        self.spellSchool = None
        self.mechanics = []
        self.rarity = Rarity.INVALID
        self.set = CardSet.INVALID
        self.type = CardType.INVALID


    @property
    def is_multi_class(self):
        return self.classes is not None

    @property
    def print_name(self):
        return self.name + ' ' + self.id


    def __lt__(self, other):
        return str.__lt__(self.print_name, other.print_name)








class CardList:
    @staticmethod
    def load_json(file, predicate):
        list_fields = [a for a in dir(Card()) if not a.startswith('__')]

        def convert_to_parameter(dick):
            card = Card()
            for field, value in dick:
                if field in list_fields:
                    card.__setattr__(field, value)

            if predicate(card):
                return card

        with open(file) as my_json:
            cards = [a for a in json.load(my_json, object_pairs_hook=convert_to_parameter) if a is not None]

        return cards


    def __init__(self, file=hsd.read_json_path, pred=lambda a: True, sort=False, only=None):
        if only is None:
            only = []
        else:
            pred = lambda a : a.id in only

        card_list = CardList.load_json(file, pred)
        if sort:
            card_list.sort()
        else:
            card_list = set(card_list)

        self.list = card_list
