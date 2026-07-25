class dmart:
    storename="dmart"
    def __init__(self,cat,pro_name,price,qty):
        self.cat=cat
        self.pro_name=pro_name
        self.price=price
        self.qty=qty
    @classmethod
    def storedetail(cls):
        return f"Store name:{cls.storename}"

    # def display(self):
        # return f"category: {self.cat} \n Product_name: {self.pro_name} \n price: {self.price} \n Quantity: {self.qty}"
         