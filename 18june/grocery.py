from d import dmart
class grocery(dmart):
    def __init__(self, cat,pro_name,price, qty,brand_name,mfg,exp):
        super().__init__(cat,  pro_name,price, qty)
        self.brand_name=brand_name
        self.mfg=mfg
        self.exp=exp
    def show(self):
        print(super().storedetail())
        # print(super().display())
        return f"category: {self.cat} \n Product_name: {self.pro_name} \n price: {self.price} \n Quantity: {self.qty} \n Brand Name:{self.brand_name}\n Mfg:{self.mfg} \n Exp:{self.mfg}"
    