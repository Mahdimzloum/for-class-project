import tkinter
from tkinter import messagebox
from users import *
from products import *


def btn_login():
    global current_user,session
    user=txt_user.get()
    pas=txt_pass.get()
    result=current_user.login(user,pas)
    if not result:
        lbl_msg.configure(text="wrong username or password!",fg="red")
    else:
        lbl_msg.configure(text=f"welcome {result[1]}" , fg='green')
        btn_login.configure(state="disabled")
        btn_shop.configure(state="active")
        btn_cart.configure(state="active")
         
        btn_logout.configure(state="active")
        txt_user.delete(0,"end")
        txt_pass.delete(0,"end")
        session=user
        if user=="admin":
            btn_admin.configure(state="active")
            btn_delete.configure(state="disabled")
            btn_setting.configure(state="active")
            
def btn_submit():
    # --------------------------
    def signup():
        global current_user
        user=txt_user.get()
        pas=txt_pass.get()
        cpas=txt_cpass.get()
        name=txt_name.get()
        addr=txt_addr.get()
        
        result,msg=current_user.submit(user,pas,cpas,name,addr)
        if not result:
            lbl_msg.configure(text=msg,fg="red")
        else:
            lbl_msg.configure(text=msg,fg="green")
            txt_user.delete(0,"end")
            txt_pass.delete(0,"end")
            txt_cpass.delete(0,"end")
            txt_name.delete(0,"end")
            txt_addr.delete(0,"end")
        
    # -----------------------
    
    submit_win=tkinter.Toplevel(win)
    submit_win.geometry("500x400")  
    submit_win.title("submit")
    lbl_user=tkinter.Label(submit_win,text="username:")
    lbl_user.pack()
    
    txt_user=tkinter.Entry(submit_win,width=20)
    txt_user.pack()
    
    lbl_pass=tkinter.Label(submit_win,text="password:")
    lbl_pass.pack()
    
    txt_pass=tkinter.Entry(submit_win,width=20)
    txt_pass.pack()
    
    lbl_cpass=tkinter.Label(submit_win,text="password confirm:")
    lbl_cpass.pack()
    
    txt_cpass=tkinter.Entry(submit_win,width=20)
    txt_cpass.pack()
    
    lbl_name=tkinter.Label(submit_win,text="name:")
    lbl_name.pack()
    
    txt_name=tkinter.Entry(submit_win,width=20)
    txt_name.pack()
    
    lbl_addr=tkinter.Label(submit_win,text="address:")
    lbl_addr.pack()
    
    txt_addr=tkinter.Entry(submit_win,width=20)
    txt_addr.pack()
    
    lbl_msg=tkinter.Label(submit_win,text="")
    lbl_msg.pack()
    
    btn_signup=tkinter.Button(submit_win,text="submit",command=signup)
    btn_signup.pack()
    
    
    submit_win.mainloop()

def btn_delete():
    confirm=messagebox.askyesno("message","are you sure?")
    if confirm:
        global session
        result=current_user.deleteUser(session)
        if result:
            lbl_msg.configure(text="your account has been deleted!",fg="green")
            session=""
            btn_login.configure(state="active")
            btn_delete.configure(state="disabled")
        else:
            lbl_msg.configure(text="something went wrong",fg="red") 
    
def btn_logout():
    global session
    session=""
    btn_logout.configure(state="disabled")
    btn_login.configure(state="active")
    btn_delete.configure(state="disabled")
    btn_admin.configure(state="disable")
    btn_shop.configure(state="disabled")
    btn_setting.configure(state="disabled")
    btn_cart.configure(state="disable")
    
    lbl_msg.configure(text="")

def btn_admin():
    def btn_psave():
        global current_product
        pname=txt_pname.get()
        qnt=txt_qnt.get()
        price=txt_price.get()
        if pname=="" or qnt=="" or price=="":
             lbl_pmsg.configure(text="please fill the inputs",fg="red")
             return
        result=current_product.save_product(pname,qnt,price)
        if result:
            lbl_pmsg.configure(text="ptoduct saved to database!",fg="green")
            txt_pname.delete(0,"end")
            txt_qnt.delete(0,"end")
            txt_price.delete(0,"end")
        else:
            lbl_pmsg.configure(text="something went wrong!",fg="red")
        
            
    win_btn=tkinter.Toplevel(win)
    win_btn.geometry("300x400")
    win_btn.title("Admin Panel")
    
    lbl_pname=tkinter.Label(win_btn,text="product name:")
    lbl_pname.pack()
    
    txt_pname=tkinter.Entry(win_btn,width=20)
    txt_pname.pack()
    
    lbl_qnt=tkinter.Label(win_btn,text="Quantity:")
    lbl_qnt.pack()
    
    txt_qnt=tkinter.Entry(win_btn,width=20)
    txt_qnt.pack()
    
    lbl_price=tkinter.Label(win_btn,text="Price:")
    lbl_price.pack()
    
    txt_price=tkinter.Entry(win_btn,width=20)
    txt_price.pack()
    
    lbl_pmsg=tkinter.Label(win_btn,text="")
    lbl_pmsg.pack()
    
    btn_psave=tkinter.Button(win_btn,text="save",command=btn_psave)
    btn_psave.pack()

    win_btn.mainloop()    

def btn_shop():
    def final_shop():
        global plist
        pid=pid_text.get()
        qnt=pqnt_text.get()
        is_id_exist=False
        for product in plist:
            if product[0]==int(pid):
               is_id_exist=True
               pqnt=product[2]
        if not is_id_exist:
            lbl_msg.configure(text="wrong product id", fg="red")
            return
        if int(qnt)>pqnt:
            lbl_msg.configure(text="not enough products!", fg="red")
            return
        result=current_product.save_to_cart(pid,qnt,session)
        if result:
            lbl_msg.configure(text="saved to cart.", fg="green")
            pid_text.delete(0,"end")
            pqnt_text.delete(0,"end")
            
            
            
            plist=current_product.products_list()
            lstbox.delete(0,"end")
            for product in plist:
                text=f"id:{product[0]} , Name:{product[1]} , QNT:{product[2]} , price:{product[3]}"
                lstbox.insert(0,text)
            
            
        else:
            lbl_msg.configure(text="something went wrong!", fg="red")
            
        
    global plist   
    win_shop=tkinter.Toplevel(win)
    
    win_shop.geometry("300x300")
    win_shop.title("shop")
    
   
    lstbox=tkinter.Listbox(win_shop,width=70)
    lstbox.pack()
    
    plist=current_product.products_list()
    for product in plist:
        text=f"id:{product[0]} , Name:{product[1]} , QNT:{product[2]} , price:{product[3]}"
        lstbox.insert(0,text)

   
    
    lbl_pid=tkinter.Label(win_shop,text="product ID:")
    lbl_pid.pack()
    
    pid_text=tkinter.Entry(win_shop)
    pid_text.pack()
    
    lbl_pqnt=tkinter.Label(win_shop,text="quantity:")
    lbl_pqnt.pack()
    
    pqnt_text=tkinter.Entry(win_shop)
    pqnt_text.pack()
    
    btn_final_shop=tkinter.Button(win_shop,text="finalize shop",command=final_shop)
    btn_final_shop.pack()
    
    lbl_msg=tkinter.Label(win_shop,text="")
    lbl_msg.pack()
    
    win_shop.mainloop()
    
def btn_setting():

    setting_win=tkinter.Toplevel(win)
    setting_win.geometry("500x400")  
    setting_win.title("Setting")
    
    lbl_font_size=tkinter.Label(setting_win,text="font size:")
    lbl_font_size.pack()
    
    txt_font_size=tkinter.Entry(setting_win,width=20)
    txt_font_size.pack()
    
    
    
    lbl_color=tkinter.Label(setting_win,text="color:")
    lbl_color.pack()
    
    txt_color=tkinter.Entry(setting_win,width=20)
    txt_color.pack()
    
    
    btn_setting_done = tkinter.Button(setting_win , text="finalize change")
    btn_setting_done.pack()
    
    txt_setting_coller.delete(0,"end")
    txt_setting_size.delete(0,"end")
    
    setting_res_one=text_setting_coller.get()
    setting_res_two=text_setting_size.get()
    
    win_setting.mainloop()
    
    def accessblity (item):
        if item:
            btn_admin.configure(state="active")
    
def btn_cart():
    cart_win=tkinter.Toplevel(win)
    cart_win.geometry("400x300")  
    cart_win.title("cart")
    
    lstbox=tkinter.Listbox(cart_win,width=70)
    lstbox.pack()
    
    cart_list=current_product.get_from_cart(session)
    for product in cart_list:
        text=f"name: {product[0]} price:{product[1]} QNT:{product[2]} Total price:{product[1]*product[2]}"
        lstbox.insert(0,text)
    
    cart_win.mainloop()
     
if __name__=="__main__":
    current_user=users()
    current_product=products()
    session=""
    
    win=tkinter.Tk()
    win.title("login")
    win.geometry("250x350")
    win.resizable(False,False)
    
    # ------------------login widgets------------
    lbl_user=tkinter.Label(win,text="username:")
    lbl_user.pack()
    
    txt_user=tkinter.Entry(win,width=20)
    txt_user.pack()
    
    lbl_pass=tkinter.Label(win,text="password:")
    lbl_pass.pack()
    
    txt_pass=tkinter.Entry(win,width=20)
    txt_pass.pack()

    lbl_msg=tkinter.Label(win,text="")
    lbl_msg.pack()
    
    btn_login=tkinter.Button(win,text="login",command=btn_login)
    btn_login.pack()
    
    btn_submit=tkinter.Button(win,text="submit",command=btn_submit)
    btn_submit.pack()
    
    btn_delete=tkinter.Button(win,text="delete",command=btn_delete,state="disabled")
    btn_delete.pack()
    
    btn_logout=tkinter.Button(win,text="logout",command=btn_logout,state="disabled")
    btn_logout.pack()
    
    btn_admin=tkinter.Button(win,text="admin panel",command=btn_admin,state="disabled")
    btn_admin.pack()
  
    btn_shop=tkinter.Button(win,text="shop",command=btn_shop,state="disabled")
    btn_shop.pack()
   
    btn_setting=tkinter.Button(win,text="setting",command=btn_setting,state="disabled")
    btn_setting.pack() 
    
    
    btn_cart=tkinter.Button(win,text="My Cart",command=btn_cart,state="disabled")
    btn_cart.pack()
   
    tkinter.mainloop()
    
    
    
    
    
    
    
    