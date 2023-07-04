import tkinter as TK 
from tkinter import messagebox
#The Main Gui  
class my_gui(TK.Tk):

    def add(self,x,y):
        result = x + y
        return result
    def sub(self,x,y):
        result = x - y
        return result
    def mul(self,x,y):
        result = x * y
        return result
    def div(self,x,y):
        result = x / y
        return result
        
        #Elements
    def gui_elements(self):
        def clear_input():
            num_field1.delete(0,'end')
            num_field2.delete(0,'end')
        def calc_result(x):
            if x== "+":
                result = self.add(int(num_field1.get()), int(num_field2.get()))
                messagebox.showinfo("RESULT",result)
            elif x == "-":
                result = self.sub(int(num_field1.get()), int(num_field2.get()))
                messagebox.showinfo("RESULT",result)
            elif x == "*":
                result = self.mul(int(num_field1.get()), int(num_field2.get()))
                messagebox.showinfo("RESULT",result)
            elif x == "/":
                result = self.div(int(num_field1.get()), int(num_field2.get()))
                messagebox.showinfo("RESULT",result)
            else:
                messagebox.showerror("ERROR","Invalid")

        lbl1 = TK.Label(self,text= "Enter Two Numbers", font="Helvetica")
        lbl_num1 = TK.Label(self,text= "Value#1:", font="Helvetica")
        lbl_num2 = TK.Label(self,text= "Value#2:", font="Helvetica")
        num_field1 = TK.Entry(self, font="Helvetica", bd=3)
        num_field2 = TK.Entry(self, font="Helvetica", bd=3)
        clr_btn = TK.Button(self, text="Clear", bd=3, font="Helvetica", command=clear_input)
        var = TK.StringVar(self)
        operation = TK.OptionMenu(self, var, "+", "-", "*", "/", command=calc_result)
        var.set("Operation")
        operation.config(font="Helvetica")
        lbl1.pack()
        operation.place(x = 80, y = 85)
        lbl_num1.place(x = 10, y = 25)
        num_field1.place(x=80, y = 25)
        lbl_num2.place(x = 10, y = 50)
        num_field2.place(x=80, y = 50)
        clr_btn.place(x = 210, y = 85)
      
    def __init__(self,w=300,h=150): 
        super().__init__() 
        self.title("Waze2Py Calcuator")
        self.iconbitmap('Waze2Py.ico')
        self.resizable(False,False)
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.gui_elements()

if __name__ == "__main__":
    main_app = my_gui()
    main_app.mainloop()
    
    
