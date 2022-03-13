
from tkinter import *

class checker_gui(Tk):
    
    def __init__(self) -> None:
        super().__init__()

    # ------------------------ Logic Var Block -------------------------

        self.lower_char = "abcdefghijklmnopqrstuvwxyz"
        self.upper_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.num = "0123456789"
        self.s_char = "!@#$%^&*()\/|-_~`''><,.*-+"  
        
        
    # --------------------------- GUI -------------------------------
        self.bg_color = "#888886"
        self.title("Checker")
        self.geometry("380x640")
        self.minsize(640,380)
        self.maxsize(640,380)
        self["bg"] = self.bg_color
        self.resizable(False,False)
        
    
    # --------------------------- main screen -------------------------------

    def main_scn(self):

        self.main_Screen = Frame()
        self.main_Screen.pack(fill="both",expand=1)

        self.btn_S1 = Button(self.main_Screen,text="Generate Password",border=0,bg="White")
        self.btn_S1.pack(fill="both",side="left",expand=1)
        self.btn_S1.bind("<ButtonRelease-1>",self.g_p)
        self.btn_S1.bind("<Return>",self.g_p)

        self.btn_S2 = Button(self.main_Screen,text="Check Password",border=0,bg=self.bg_color)
        self.btn_S2.pack(fill="both",side="left",expand=1)
        self.btn_S2.bind("<ButtonRelease-1>",self.c_p)
        self.btn_S2.bind("<Return>",self.c_p)     
        
    def back(self,e):
        self.frame1.destroy()
        self.main_scn()

    def back2(self,e):
        self.frame2.destroy()
        self.main_scn()

    # --------------------------- screen 2 -------------------------------

    def g_p(self,e):
        self.main_Screen.destroy()

        self.frame1 = Frame(bg=self.bg_color)
        self.frame1.pack(fill="both",expand=1)  

        self.btn_frm = Frame(self.frame1,bg=self.bg_color)
        self.btn_frm.pack(side="bottom",fill=X)


        self.new_pass_var = StringVar()
         
        self.new_pass = Entry(self.frame1,textvariable=self.new_pass_var)
        self.new_pass["bg"] = self.bg_color
        self.new_pass["font"] = 100
        self.new_pass.pack(fill="x",expand=1)

        self.btn1 = Button(self.btn_frm,text="Generate Password",border=0,bg="white")
        self.btn1.pack(side="left",fill="both",expand=1)
        self.btn1.bind("<ButtonRelease-1>",self.pass_gen)
        self.btn1.bind("<Return>",self.pass_gen)   

        self.btn_b = Button(self.btn_frm,text="Back",border=0,bg=self.bg_color,)
        self.btn_b.pack(side="left")
        self.btn_b.bind("<ButtonRelease-1>",self.back)
        self.btn_b.bind("<Return>",self.back)

       
    
    # --------------------------- screen 2 -------------------------------

    def c_p(self,e):
        self.main_Screen.destroy()
        self.frame2 = Frame(bg=self.bg_color)
        self.frame2.pack(fill="both",expand=1)  

        self.btn_frm2 = Frame(self.frame2,bg="green")
        self.btn_frm2.pack(side="bottom",fill=X)
        
        self.log1 = Label(self.frame2,text="Enter Password",anchor="w")
        self.log1["bg"] = self.bg_color
        self.log1["font"] = 100
        self.log1.pack(fill="both",pady=5)
    

        self.user_pass = Entry(self.frame2)
        self.user_pass.pack(fill=X,padx=2,pady=5)

        self.log2 = Label(self.frame2,text="Status",anchor="w")
        self.log2["bg"] = self.bg_color
        self.log2["font"] = 100
        self.log2.pack(fill="both",pady=5)

        self.p_chek = Label(self.frame2,anchor="w")
        self.p_chek["bg"] = self.bg_color
        self.p_chek["font"] = 100
        self.p_chek.pack(fill="both")   


        self.btn3 = Button(self.btn_frm2,text="Check Password",border=0)
        self.btn3.pack(side="left",fill="both",expand=1)
        self.btn3.bind("<ButtonRelease-1>",self.pass_chcker)
        self.btn3.bind("<Return>",self.pass_chcker)

        self.btn_b = Button(self.btn_frm2,text="Back",border=0,bg=self.bg_color)
        self.btn_b.pack(side="left",fill="both")
        self.btn_b.bind("<ButtonRelease-1>",self.back2)
        self.btn_b.bind("<Return>",self.back2)

    # ------------------------ Logic Var Block -------------------------
        

        self.lower_char = "abcdefghijklmnopqrstuvwxyz"
        self.upper_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.num = "0123456789"
        self.s_char = "!@#$%^&*()"  
    # ------------------------ Logic Block -------------------------

    def pass_gen(self,e):
        import random
        pass_char = self.upper_char + self.lower_char + self.num + self.s_char
        password = "".join(random.sample(pass_char,random.randint(8,len(pass_char))))
        # self.new_pass["text"]=password
        self.new_pass_var.set(password)
        self.new_pass.update()
        
    def pass_chcker(self,e):
        which_btn = e.widget.cget("text")
        if which_btn == "Check Password" :
           pass_word = self.user_pass.get()
        elif which_btn == "Check Generated Password" :
            pass_word = self.new_pass.get()

        pass_word = self.user_pass.get()
        pass_len = len(pass_word)

        if pass_len < 8:
            self.p_chek["text"] = "Weak Password,Password must be 8 or greater digit"
        else:
            i = 0
            lst = {
                    "u":0,
                    "l":0,
                    "n":0,
                    "s":0
                  }
            while i < pass_len :
                if pass_word[i] in self.upper_char:
                    lst["u"] = lst["u"]+1
                elif pass_word[i] in self.lower_char:
                    lst["l"] = lst["l"]+1
                elif pass_word[i] in self.num:
                    lst["n"] = lst["n"]+1
                elif pass_word[i] in self.s_char:
                    lst["s"] = lst["s"]+1
                else:
                    self.p_chek["text"] = "Your Password must have one A-Z, a-z, 0-9, @-#"      
                i= i+1

            if lst["u"] > 0 and lst["l"] > 0 and lst["n"] > 0 and lst["s"] > 0:
                self.p_chek["text"] = "Unbreakable! Password :-)"

            elif lst["u"] == 0 and lst["l"] > 0 and lst["n"] ==0 and lst["s"] == 0:
               self.p_chek["text"] = f"Poor Password :-( have {lst['u']} UpperCase Letter, {lst['l']} Lowercase Letter, {lst['n']} Numbers \n and {lst['s']} Special Charcters"
            
            elif lst["u"] == 0 and lst["l"] == 0 and lst["n"] > 0 and lst["s"] == 0:
               self.p_chek["text"] = f"Poor Password :-( have {lst['u']} UpperCase Letter, {lst['l']} Lowercase Letter, {lst['n']} Numbers \n and {lst['s']} Special Charcters"


            else:
                self.p_chek["text"] =  f"Password is Average have {lst['u']} UpperCase Letter, {lst['l']} Lowercase Letter, {lst['n']} Numbers \n and {lst['s']} Special Charcters"



if __name__ == "__main__":

    window = checker_gui()
    window.main_scn()
    window.mainloop()

