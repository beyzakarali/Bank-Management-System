import tkinter as tk
import tkinter.messagebox
 

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack() #OLMAK ZORUNDALAR
        self.grid()  
        self.place() 
        self.first_windows()
       
        

    def first_windows(self):

     
        self.i_lab = tk.Label(self , text ="Welcome").grid(row=1, column=4 )

        self.label1 = tk.Label(self,text="Username:").grid(row=5,column=3) 

        self.input1 = tk.Entry(self, font=40 ).grid(row=5,column=4)

        self.label2 = tk.Label(self, text="Password").grid(row=10, column=3)

        self.input2 = tk.Entry(self, font=40).grid(row=10, column= 4)
        
        self.enterButton = tk.Button(self,text="ENTER",fg="white",bg="black",command = self.enterPro ).grid(row =15 , column=4)
        #DEGERLERİ AL    Lambda:self.sıgn_ın(self.input1.get()
        self.label3 = tk.Label(self,text="Don't have an account?").grid(row=50,column=4)
        self.SıgnButton = tk.Button(self,text="SIGN UP",fg="white",bg="black",command =self.sıgn_ın).grid(column=4)

        
        '''
        self.ref_profile = tk.Button(self,text="REFRESH PROFILE", fg="red", command=self.ref_profıle)
        self.ref_profile.pack()
        '''
  
    
    
    def enterPro(self):
        self.master.destroy()
        new2=tk.Tk()
        new2.title("Image Processing")
        new2.geometry("300x300")
        self.PosLabel= tk.Label(new2,text="Login successful..").grid(row=3 ,column=3 )  
        
       
        
        
        
    
    def sıgn_ın(self):
        
        self.master.destroy()
        
        #HİDE OLAYLARI DENEME
        #self.master.update()
        #self.master.withdraw()  
        
        new=tk.Tk()
        new.title("Add Account")         
        #n1=Application(master=new)
        new.geometry("350x310")
        self.Label4 = tk.Label(new,text = "Username:").grid(row=1,column=1, sticky = "W", pady = 2)
        self.input3  = tk.Entry(new,font=20).grid(row=1 ,column=2 )
        self.button3 = tk.Button(new,text="Confirm",bg="black",fg="white").grid(row=1,column=3)
        self.Label5 = tk.Label(new,text="Name:").grid(row= 2 ,column =1)
        self.input4 = tk.Entry(new,font=20).grid(row=2 , column=2)
        self.Label6 = tk.Label(new,text="Surname:").grid(row= 3 ,column =1)
        self.input5 = tk.Entry(new,font=20).grid(row=3 , column=2)
        self.Label7 = tk.Label(new,text="Password:").grid(row= 4 ,column =1)
        self.input6 = tk.Entry(new,font=20).grid(row=4 , column=2)
        self.button4 = tk.Button(new,text="SIGN",bg="red",fg="white").grid(row=5,column=2)
        self.buton5 = tk.Button(new,text="BACK",fg="white",bg="black").grid(row=6,column=3)
        
        
        self.img = tk.PhotoImage(file = r"/home/beyza/Resimler/no-profile.png") 
        self.img1 = self.img.subsample(6,6) 
        self.buton4 = tk.Button(new, text = 'Click Me !', image = self.img1,).grid(row=0,column=2) 
        

        new.mainloop()
        
   
   
root = tk.Tk()
root.geometry("300x200")
root.title("Security System")
app = Application(master=root)
app.mainloop()
