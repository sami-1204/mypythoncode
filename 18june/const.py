from d import dmart
class cloth(dmart):
    def __init__(self,cat,pro_name,price,qty,color,size):
        super().__init__(cat,pro_name,price,qty)
        self.color=color
        self.size=size
    def dis(self):
        print(super().storedetail())
        # print(super().display())
        return f"category: {self.cat} \n Product_name: {self.pro_name} \n price: {self.price} \n Quantity: {self.qty}\n Color:{self.color}\n Size:{self.size}"