class Product():
    def __init__(self,category_id,title,short_description,slug,permalik,is_available,sku,price,regular_price,sale_price,manage_stock,stock_quantity,is_visibla,date_created_gmt,date_modified_gmt):
        self.category_id =category_id
        self.title = title
        self.short_description = short_description
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
        
