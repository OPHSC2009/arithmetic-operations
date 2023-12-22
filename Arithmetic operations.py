from tkinter import*
root=Tk()
root.title("Mathematic Operations")
root.geometry("1000x1000")
root.configure(background="orange")



lbl_1=Label(root,text="Enter first number",font=("Arial",18,"bold"),bg="orange",fg="black")
lbl_2=Label(root,text="Enter second number",font=("Arial",18,"bold"),bg="orange",fg="black")
lbl_1.place(relx=0.3,rely=0.2,anchor=CENTER)
lbl_2.place(relx=0.3,rely=0.3,anchor=CENTER)

num_1=Entry(root)
num_1.place(relx=0.5,rely=0.2,anchor=CENTER)

num_2=Entry(root)
num_2.place(relx=0.5,rely=0.3,anchor=CENTER)

value_1=0
value_2=0



lbl_3=Label(root,font=("Arial",20,"italic"))
lbl_3.place(relx=0.5,rely=0.6,anchor=CENTER)

def add():
    global value_1
    value_1=int(num_1.get())
    
    
    global value_2
    value_2=int(num_2.get())
    
    
    lbl_3["text"]="The answer is "+str(value_1 + value_2)
    
def sub():
    global value_1
    value_1=int(num_1.get())
    global value_2
    value_2=int(num_2.get())
    lbl_3["text"]="The answer is "+str(value_1 - value_2)
    
def multi():
    global value_1
    value_1=int(num_1.get())
    global value_2
    value_2=int(num_2.get())
    lbl_3["text"]="The answer is "+str(value_1 * value_2)
    
def div():
    global value_1
    value_1=int(num_1.get())
    global value_2
    value_2=int(num_2.get())
    lbl_3["text"]="The answer is "+str(int(value_1 / value_2))

    

btn_1=Button(root,text="Addition",command=add)
btn_2=Button(root,text="Subtraction",command=sub)
btn_3=Button(root,text="Multiplication",command=multi)
btn_4=Button(root,text="Division",command=div)

btn_1.place(relx=0.2,rely=0.4,anchor=CENTER)
btn_2.place(relx=0.4,rely=0.4,anchor=CENTER)
btn_3.place(relx=0.6,rely=0.4,anchor=CENTER)
btn_4.place(relx=0.8,rely=0.4,anchor=CENTER)




root.mainloop()
