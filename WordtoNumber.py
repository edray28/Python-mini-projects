# WordtoNumber Calculator v0.1
import tkinter 

#The Main Gui
class myGui(tkinter.Tk):
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

if __name__ == "__main__":
    main_app = myGui()
    main_app.mainloop()
