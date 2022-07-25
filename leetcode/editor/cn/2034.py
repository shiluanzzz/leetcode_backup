from sortedcontainers import SortedList,SortedDict


from sortedcontainers import SortedList,SortedDict

class StockPrice:

    def __init__(self):
        self.data={}
        self.price=SortedList()
        self.current=0

    def update(self, timestamp: int, price: int) -> None:

        if timestamp in self.data:
            self.price.remove(self.data[timestamp])


        self.data[timestamp]=price
        self.price.add(price)

        if timestamp>=self.current:
            self.current=timestamp

    def current(self) -> int:
        print(2)
        return self.data[self.current]

    def maximum(self) -> int:
        return self.price[-1]

    def minimum(self) -> int:
        return self.price[0]



if __name__ == '__main__':
    a=StockPrice()
    a.update(1,10)
    a.update(2,5)
    print(a.current())
    print(a.maximum())
    print(a.minimum())