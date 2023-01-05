#Insert, list, delete, update
class ProductInMemoryDb:
    _product_list = []

    @classmethod
    def Insert(cls,obj):
        try:
            ProductInMemoryDb._product_list.append(obj.info)
        except:
            print("object not found")

    
    @classmethod
    def List(cls):
        for i in  ProductInMemoryDb._product_list:
            print(i.__repr__())



    @classmethod
    def delete_by_id(cls,id:int):
        for i in ProductInMemoryDb._product_list :
            if i['id']==id:
                ProductInMemoryDb._product_list.pop(i)
                
                print("delete successful")
                break
        else:
            print("unsuccessful")


    @classmethod
    def delete_all(cls):
        ProductInMemoryDb._product_list.clear()
        print("delete successful")




    @classmethod
    def update_object(cls,obj):
        for i in ProductInMemoryDb._product_list :
            if i["object"]==obj:
                ProductInMemoryDb._product_list[i]=obj.info