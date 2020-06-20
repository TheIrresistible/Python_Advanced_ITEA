class Shop:

    sell_list = []

    def __init__(self, name, sell):
        self.name = name
        self.sell = int(sell)
        Shop.sell_list.append(sell)

    def selling(self, new_sell):
        self.sell += new_sell
        Shop.sell_list.append(new_sell)
        print(self.name, 'sellings increased by', new_sell)

    def info(self):
        theSum = 0
        for i in self.sell_list:
            theSum = theSum + i
        return theSum

skymall = Shop('SkyMall', 20)
rivermall = Shop('RiverMall', 15)

rivermall.selling(5)

print('SkyMall:', skymall.sell)
print('RiverMall:', rivermall.sell)

rivermall.selling(5)
print('All shops:', rivermall.info())
