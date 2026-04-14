class Computer:                                         # 1. defineeri class

    def __init__(self):                                 # 2. loome konstruktori
        self.__selling_price = 700
        self.public_price = 1000


    def sell(self):                                     # 3. ja 4. defineeri ja väärtusta väljad
        print(f"Selling price {self.__selling_price}")
        print(f"Public price {self.public_price}")

    def set_selling_price(self, price):                 # 5. tee midagi kasuliku
        if price < 0:
            raise Exception("Sorry,  you cannot sell for negative price")
        self.__selling_price = price


if __name__ == '__main__':
    c = Computer()
    c.sell()


    # change the price
    c.__selling_price = 1000
    c.sell()

    # setting selling price using setter function
    c.set_selling_price(1000)
    c.sell()
