"""

fk=Foreign Key
pk= Primary Key


"""

class Product():
    def __init__(self,category_id:int,title:str,short_description:str,description:str,slug,permalink:str,is_available:bool,

                sku:str,price:float,regular_price:float,sale_price:float,manage_stock:int,stock_quantity:int,is_visibla:bool,
        
                date_created_gmt:str,date_modified_gmt:str):
        
        
        self.category_id =category_id
        self.title = title
        self.short_description = short_description
        self.description=description
        self.slug = slug
        self.permalik = permalink
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

    def read(self):
        pass

    def __repr__(self):
        return f"Product [ {self.category_id} {self.title} {self.short_description} {self.description} {self.slug} {self.permalik} {self.permalik} {self.is_available} {self.sku} {self.price} {self.regular_price} {self.sale_price} {self.manage_stock} {self.stock_quantity} {self.is_visibla} {self.date_created_gmt} {self.date_modified_gmt} ]"

    """
    def __repr__(self) :
        return(\"""name : %s
        id : %d
        description : %s
        availability : %b
        regular price : %f
        sale price : %f
        date created : %s
        date modified : %s
        \"""%(self.title,self.category_id,self.description,self.is_available,
        self.regular_price,self.sale_price,self.date_created_gmt,self.date_modified_gmt))"""
        
