from core.card import Card
class Thing:
    def __init__(self):
        self.hi_wassup = 23423
        self.no = 4

    def __getattribute__(self, item):
        if item == 'hi_wassup':
            return 3

        return super(Thing, self).__getattribute__(item)
def main():
    thing = Thing()
    print(thing.hi_wassup)
    print(thing.no)

if __name__ == '__main__':
    main()



