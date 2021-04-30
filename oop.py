class Shop:
    def __init__(self, color, size, stock,sales):
        self.color = color
        self.size = size
        self.stock = stock
        self.sales = sales

    def about_shirt(self):
        return f'Color : {self.color.capitalize()} | Size : {self.size.upper()} | Stock : {self.stock} | Sales : {self.sales}'

    def __str__(self) -> str:
        return f'Color : {self.color.capitalize()} | Size : {self.size.upper()} | Stock : {self.stock} | Sales : {self.sales}'

    def change_color(self, new_color):
        self.color = new_color

    def sell_shirt(self, sell):
        if self.stock - sell >=0 and self.sales >=0:
            self.stock -= sell #self.stock = self.stock - sell
            self.sales += sell #self.sales = self.sales + sell

        elif self.stock - sell < 0:
            print("Not Enough | Stock max : ", self.stock)

class Shop2(Shop):
    pass

shirt1=Shop("red", "s", 100, 0)
shirt2=Shop2("green","xl",50, 20)
shirt1.change_color("blue")
shirt1.sell_shirt(120)
shirt2.sell_shirt(20)
print(shirt1.about_shirt())
print(shirt2.__str__())