# WordtoNumber Calculator v0.2
import tkinter as TK 
import math

#The Main Gui
def helloCallBack():
    print('TESTING')
class my_gui(TK.Tk):
    def __init__(self,w=500,h=500): 
        super().__init__() 
        self.title("Word2Number Calculator")
        self.iconbitmap('Word2Num.ico')
        self.resizable(False,False)
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.gui_elements()
        #Elements
    def gui_elements(self):
        lbl1 = TK.Label(self,text= "Enter a Number in Word Format(ex: One Plus Two)", font="Helvetica")
        txt_field = TK.Text(self, font="Helvetica")
        calc_btn = TK.Button(self, text="Calculate", bd=5, font="Helvetica", command= helloCallBack)
        lbl1.pack()
        txt_field.pack()
        calc_btn.pack()

        
if __name__ == "__main__":
    main_app = my_gui()
    main_app.mainloop()
    
    



    
