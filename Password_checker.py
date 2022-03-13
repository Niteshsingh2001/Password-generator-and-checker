
password = input("Enter Your Password :")

def pass_chcker(pass_word):
    import random
    lower_char = "abcdefghijklmnopqrstuvwxyz"
    upper_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    s_char = "!@#$%^&*()"   
    pass_char = upper_char + lower_char + num + s_char
    pass_len = len(pass_word)
    
    if pass_len < 8:
        return "Weak Password,Password must be 8 or greater digit"
    else:
        i = 0
        lst = {
                "u":0,
                "l":0,
                "n":0,
                "s":0
              }
        while i < pass_len :
            if pass_word[i] in upper_char:
                lst["u"] = lst["u"]+1
            elif pass_word[i] in lower_char:
                lst["l"] = lst["l"]+1
            elif pass_word[i] in num:
                lst["n"] = lst["n"]+1
            elif pass_word[i] in s_char:
                lst["s"] = lst["s"]+1
            else:
                return "Your Password must have one A-Z, a-z, 0-9, @-#"      
            i= i+1

        if lst["u"] > 0 and lst["l"] > 0 and lst["n"] > 0 and lst["s"] > 0:
            return "Unbreakable! Password :-)"
        
        elif lst["u"] == 0 and lst["l"] > 0 and lst["n"] ==0 and lst["s"] == 0:
            return f"Your Poor Password :-( have {lst['u']} UpperCase Letter, {lst['l']} Lowercase Letter, {lst['n']} Numbers and {lst['s']} Special Charcters"
           
            
        else:
            return f"Your Password is Average have {lst['u']} UpperCase Letter, {lst['l']} Lowercase Letter, {lst['n']} Numbers and {lst['s']} Special Charcters"

            




print(pass_chcker(password))