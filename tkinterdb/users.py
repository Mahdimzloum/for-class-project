from database import *
class users:
    def __init__(self):
        self.currentDB=db()
    
    def login(self,user,pas):
        result=self.currentDB.login_db(user,pas)
        row=result.fetchone()
        return row
    
    def __validation(self,user,pas,cpas,name):
        if user=="" or pas=="" or cpas=="" or name=="":
            return False,"please fill the blanks!"
        if pas!=cpas:
            return False,"password and confirmation not match"
        if len(pas)<8:
            return False,"password length should be at least 8"
        
        if self.currentDB.isUserExist(user):
            return False,"username already exist!"
        
        return True,""
        
    def submit(self,user,pas,cpas,name,addr):
        
        
        result,msg=self.__validation(user,pas,cpas,name)
        if not result:
            return result,msg
        
        result=self.currentDB.savetoDB(user,pas,name,addr)
        if not result:
            return result,"something went wrong"
        else:
            return result,"submit done!"
    
    def deleteUser(self,user):
        return self.currentDB.deleteUser(user)
    
    
    def accessbility(self,lst_access):
        if item in lst_access[1]:
            return True
        else:
            return False
        
           
        
        
        
        
       
        
        
    
        
