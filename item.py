import sqlite3
from tkinter import *
import tkinter
from tkinter import ttk 
from db import cursor,conn





def add_new():
    t=Toplevel(window)
    t.title("Add New Item")
    t.geometry("300x300")
    
    # item name
    ln = ttk.Label(t,text="Item Name:")
    ln.grid(row=1,column=0)
    
    n_val =StringVar()
    n_en =ttk.Entry(t,textvariable=n_val)
    n_en.grid(row=1,column=2)
    
    
    # quantity
    lq = ttk.Label(t,text="Quantity: ")
    lq.grid(row=2,column=0)
    
    q_val = StringVar()
    q_en = ttk.Entry(t,textvariable=q_val)
    q_en.grid(row=2,column=2)
    
    
    # Price
    lp = ttk.Label(t,text="Price: ")
    lp.grid(row=3,column=0)
    
    p_val = StringVar()
    p_en = ttk.Entry(t,textvariable=p_val)
    p_en.grid(row=3,column=2)
    
    
    
    def add():
        print(q_val.get())
        name = n_val.get()
        quantity = q_val.get()
        price = p_val.get()
        if name !='' or quantity !='' or price !='':
            val = [name,quantity,price]
        else:
            print("can not empty")
        #print(name,quantity,price)
        cursor.execute("insert into store(item,quantity,price) values(?,?,?)",val)
        conn.commit()
        t.destroy()
        show_all()
        
        
    l=Label(t)
    l.grid(row=4,column=0)
        
    btn = ttk.Button(t,text="save",command=add)
    btn.grid(row=5,column=4)
    



def show_all():
    res = cursor.execute("SELECT * FROM store")
       
    
    tree = ttk.Treeview(window)
    tree.grid(row=5,column=0)
    tree['columns'] = ('Quantity','Price')
   
    tree.column('Quantity',width=70,anchor='center')
    tree.heading('Quantity',text="Quantity")
    tree.column('Price',width=50,anchor='center')
    tree.heading('Price',text="Price")
    
    
    for x in res:
        ch_var = StringVar(value=x[1])
        ch_var.set(x[1])
        
        #tree.insert(x,'end',text=x[1])
        tree.insert('',0,text=x[1],values=(x[2],x[3]))
    
    # l = Listbox(window,listvariable=ch_var)
    # l.grid(row=3,column=0)

window = Tk()
window.title("Item Manager")
window.geometry("700x500")

lb = ttk.Label(window,text="Item Manager Application")
lb.grid(row=0,column=0)

btn = ttk.Button(window,text="Show All Item",command=show_all)
btn.grid(row=0,column=5)
btn1 = ttk.Button(window,text="Add New Item",command=add_new)
btn1.grid(row=0,column=10)




window.winfo_rgb('black')

window.mainloop()