# Random password genrator

def pass_gen(pass_len):
    import random
    lower_char = "abcdefghijklmnopqrstuvwxyz"
    upper_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    s_char = "!@#$%^&*()"   
    pass_char = upper_char + lower_char + num + s_char
    password = "".join(random.sample(pass_char,pass_len))
    return password

if __name__ == "__main__":
    length = int(input("Enter length of password you Want :"))
    print(pass_gen(length))
