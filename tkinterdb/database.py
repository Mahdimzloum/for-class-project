import sqlite3
import hashlib

class db:
    def __init__(self):
        self.cnt=sqlite3.connect("shop.db")
    
    def login_db(self,user,pas):
        coded_pas = hashlib.md5(pas.encode())
        
        sql=''' SELECT * FROM users WHERE username=? AND 
        password=? '''
        result=self.cnt.execute(sql,(user,coded_pas.hexdigest()))
        return result
    
    def isUserExist(self,user):
        sql='''SELECT * FROM users WHERE username=?'''
        result=self.cnt.execute(sql,(user,))
        row=result.fetchone()
        if row:
            return True
        else:
            return False
    
    def savetoDB(self,user,pas,name,addr):
        
            sql='''INSERT INTO users (name,username,password,addr)
                    VALUES(?,?,?,?)'''
            coded_pas = hashlib.md5(pas.encode())
            
            self.cnt.execute(sql,(name,user,coded_pas.hexdigest(),addr)) 
            self.cnt.commit()
            return True
    def deleteUser(self,user):
            try:
                sql='''DELETE FROM users WHERE username=?'''
                self.cnt.execute(sql,(user,))
                self.cnt.commit()
                return True
            except:
                return False
    
    def psavetoDB(self,pname,qnt,price):
        try:
            sql='''INSERT INTO products (pname,qnt,price)
                        VALUES(?,?,?)'''
            
            self.cnt.execute(sql,(pname,qnt,price))
            self.cnt.commit()
            return True
        except:
            return False
    
    def products_list_db(self):
        sql='''SELECT * FROM products'''
        result=self.cnt.execute(sql)
        rows=result.fetchall()
        return rows
    
    def __find_user_id(self,user):
        sql='''SELECT id FROM users WHERE username=?'''
        result=self.cnt.execute(sql,(user,))
        row=result.fetchone()
        return row[0]
         
    def __updateqnt(self,pid,qnt):
        sql='''UPDATE  products SET   qnt=(qnt - ?) WHERE id=? '''
        self.cnt.execute(sql,(qnt,pid))
        self.cnt.commit()
        
        
    def save_to_cart_db(self,pid,qnt,user):
        uid=self.__find_user_id(user)
        sql='''INSERT INTO cart (pid,uid,qnt) VALUES(?,?,?)'''
        try:
           self.cnt.execute(sql,(pid,uid,qnt)) 
           self.cnt.commit()
           self.__updateqnt(pid,qnt)
           return True
        except:
           return False
       
    def get_cart_db(self,user):
         uid=self.__find_user_id(user)
         sql='''SELECT products.pname,products.price,cart.qnt
             FROM cart
             INNER JOIN products
             ON cart.pid=products.id
             WHERE cart.uid=?'''
         
         result=self.cnt.execute(sql,(uid,))
         rows=result.fetchall()
         return rows
        
            
    def setting_db(self,setting_res_one,setting_res_two):
        with open ("Setting.json")as f :
            result = json.load (f)
            
            
    def accessblity_db (self,user):
        lst_access=[]
        lst_1=[]
        lst_0=[]
        for item in user:
            if item =="hoomehr":
                lst_1.append(item)
            elif item=="mina":
                lst_0.append(item)
                
        return lst_access.appned(lst_0,lst_1)
        
       
        
        
        
        
        
        
        
        
        
        
        
    