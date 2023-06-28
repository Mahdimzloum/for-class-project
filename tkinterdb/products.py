from database import *
class products():
    def __init__(self):
         self.currentDB=db()
    def save_product(self,pname,qnt,price):
        return self.currentDB.psavetoDB(pname,qnt,price)

    def products_list(self):
         return self.currentDB.products_list_db()
    
    def save_to_cart(self,pid,qnt,user):
        return self.currentDB.save_to_cart_db(pid,qnt,user)
    
    def get_from_cart(self,user):
        return self.currentDB.get_cart_db(user)
        