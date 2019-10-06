import tkinter as tk
#from tkinter import *
import cv2
import tkinter.messagebox
 


#SAYFANIN ÇOK AÇILMASINA BAKMAK LAZIM

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        

    def create_widgets(self):
        
        variable = StringVar()
        self.label = tk.Label(self, text="Username :")
        self.label.grid (row =40 , column=40) #İŞE YARAMIYOR  .place(x=.. , y= ..) dene
        self.label.pack()
        
        self.input1 = tk.Entry(self, textvariable = variable).pack()
    
        
        self.label1 = tk.Label(self, text ="Password: ")
        self.label1.pack()
        
        self.input2 = tk.Entry().pack()
        
        
        self.yüz_tanima = tk.Button(self,text="FIND ME",fg="red",bg="blue",
                                    command=self.ımg_pro)
        self.yüz_tanima.pack()


        self.a_newp = tk.Button(self, text="ADD NEW PROFILES",fg="red", 
                                command= self.a_newp)
        self.a_newp.pack()


        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy,
                              )
        self.quit.pack()

        
        self.ref_profile = tk.Button(self,text="REFRESH PROFILE",fg="red",
                                     command=self.ref_profıle)
        self.ref_profile.pack()
        
        
    def a_newp(self):
        print("hi there, everyone!")


        
    def ımg_pro (self):
        self.master.destroy()
        image = cv2.imread("/home/beyza/Resimler/monarch.png")
        cv2.imshow("Image",image)
        cv2.waitKey(0)
        
        
    def ref_profıle(self):
        self.window=Tk()
        self.master.destroy()
        self.window.title("Welcome to Login")
        self.window.geometry("250x200")
        
        #YENİ PENCEREYE YAZILMIYOR
       # self.labelw = window2.Label(window2,text="yeni penceree")
       # self.labelw.pack()
        
        print("entry .")
     
   
        
        
root = tk.Tk()
root.geometry("500x500")
app = Application(master=root)
app.mainloop()
