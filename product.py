"""
fk=Foreign Key
pk= Primary Key


"""

class Product():
    def __init__(self,category_id:int,title:str,short_description:str,description:str,slug:str,permalik:str,is_available:bool,
    
                sku:str,price:float,regular_price:float,sale_price:float,manage_stock:int,stock_quantity:int,is_visibla:bool,
        
                date_created_gmt:str,date_modified_gmt:str):

        self.category_id =category_id
        self.title = title
        self.short_description = short_description
        self.description=description
        self.slug = slug
        self.permalik = permalik
        self.is_available = is_available
        self.sku = sku
        self.price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.manage_stock = manage_stock
        self.stock_quantity = stock_quantity
        self.is_visibla = is_visibla
        self.date_created_gmt = date_created_gmt
        self.date_modified_gmt = date_modified_gmt

    def update(self):
        pass

    def delete(self):
        pass

    def remove(self):
        pass
        
