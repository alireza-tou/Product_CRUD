from datetime import datetime
from product_injson_db import ProductInMemoryDb

class Product():

    def __init__(self, title:str, short_description:str , description:str  , slug:str, permalink:str, sku:str, price:float, regular_price:float,
                 sale_price:float, manage_stock:bool, stock_quantity:int, date_created_gmt :int, date_modified_gmt:int,category_id:int = 0, 
                 is_visible = True, is_available:bool = False):

        self.id = None
        self.category_id = category_id
        self.title = title
        self.short_description =  short_description
        self.description = description
        self.slug = slug
        self.permalink = permalink
        self.is_available = is_available
        self.sku = sku
        self.price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.manage_stock = manage_stock
        self.stock_quantity = stock_quantity
        self.is_visible = is_visible
        self.date_created_gmt = date_created_gmt
        self.date_modified_gmt = date_modified_gmt


    def create(self,id:int):
        self.id=id
        self.info={"object":self,"id":self.id,"category_id":self.category_id,"title":self.title,"short_description":self.short_description
        ,"slug":self.slug,"permalink":self.permalink,"is_available":self.is_available,"sku":self.sku,"price":self.price,"regular_price":self.regular_price
        ,"sale_price":self.sale_price,"manage_stock":self.manage_stock,"stock_quantity":self.stock_quantity,"is_visible":self.is_visible
        ,"date_created_gmt":self.date_created_gmt,"date_modified_gmt":self.date_modified_gmt}
    
    
    @property
    def info(self):
        self.info={"object":self,"id":self.id,"category_id":self.category_id,"title":self.title,"short_description":self.short_description
        ,"slug":self.slug,"permalink":self.permalink,"is_available":self.is_available,"sku":self.sku,"price":self.price,"regular_price":self.regular_price
        ,"sale_price":self.sale_price,"manage_stock":self.manage_stock,"stock_quantity":self.stock_quantity,"is_visible":self.is_visible
        ,"date_created_gmt":self.date_created_gmt,"date_modified_gmt":self.date_modified_gmt}

        return self.info



    def update(self,**kwrgs) -> None :
        for i in kwrgs.keys():
            setattr(self,i,kwrgs[i])
        print("update succesfully")



    def __repr__(self) -> str:
        return f"the product with \n\
        Product Id: N/A \n\
        Title: {self.title} \n\
        Short description: {self.short_description} \n\
        Description: {self.description} \n\
        Slug: {self.slug} \n\
        Permanent link: {self.permalink} \n\
        availablity: {self.is_available} \n\
        Stock keeping Unit: {self.sku} \n\
        Price: {self.price} \n\
        Reqular Price: ${self.regular_price} \n\
        Sale Price: ${self.sale_price} \n\
        Manage Stock {self.manage_stock} \n\
        Stock Quantity: {self.stock_quantity} \n\
        Visible: {self.is_visible} \n\
        Date Created: {datetime.utcfromtimestamp(self.date_created_gmt).strftime('%Y-%m-%d %H:%M:%S')} \n\
        Date Modified: {datetime.utcfromtimestamp(self.date_modified_gmt).strftime('%Y-%m-%d %H:%M:%S')} \n\
        "

