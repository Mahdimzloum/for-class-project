import sqlite3
class developeCode:
    def __init__(self):
        self.cnt=sqlite3.connect("shop.db")
        
    def create_products_table(self):
        sql='''CREATE TABLE products(
           id INTEGER PRIMARY KEY,
           pname CHAR(20),
           qnt INTEGER,
           price INTEGER)'''
        self.cnt.execute(sql)
    
    def create_cart_table(self):
        sql='''CREATE TABLE cart(
           id INTEGER PRIMARY KEY,
           pid INTEGER,
           uid INTEGER,
           qnt INTEGER)'''
        self.cnt.execute(sql)


if __name__=="__main__":
    dvl=developeCode()
    # dvl.create_products_table()
    dvl.create_cart_table()
        
        
                