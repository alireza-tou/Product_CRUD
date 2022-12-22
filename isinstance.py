from product import Product

class Car():
    def __init__(self,name:str,company:str,price:float,year:int):
        self.name=name
        self.company=company
        self.price=price
        self.year=year

    def __repe__(self):
        return f"Car({self.name}, {self.company} ,{self.price} ,{self.year})"



item1=Product(1,"iphone 12 mini","phone","apple mobile phone","iphone-12","https://www.apple.com/shop/buy-iphone/iphone-12",True,"A2176",600,600,799,20,20,True,"2022/12/15","2022/12/20")
car1=Car("cls","Benz",1000000,2019)

#isinstance
print(isinstance(car1,Product)) #False
print(isinstance(car1,Car)) #True