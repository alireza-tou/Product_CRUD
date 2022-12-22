from product import Product
item1=Product(1,"iphone 12 mini","phone","apple mobile phone","iphone-12","https://www.apple.com/shop/buy-iphone/iphone-12",True,"A2176",600,600,799,20,20,True,"2022/12/15","2022/12/20")
print(item1) # __str__
print(Product.all_objects)#__repr__
print(type(item1)) #<class 'product.Product'>

