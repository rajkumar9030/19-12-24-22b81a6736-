def check_password(password):
    ch = ["!","@","#","$","%","&","*","(",")"]
    if len(password) < 10 or len(password) > 15:
        return "Weak: Password should contain min 10 and max 15 characters"
    elif not (any(char.isupper() for char in password) and any(char.islower() for char in password) and any(char.isdigit() for char in password) and any(char in ch for char in password)):
        return "Password should contain at least 1 uppercase letter, 1 lowercase letter, 1 digit, and 1 special character"
    elif " " in password:
        return "Password should not allow white spaces"
    elif password[-1] == "." or password[-1] == "@":
        return "Password should not end with .(dot) or @ symbol"
    else:
        return "Good Password"
password = input("Enter your password: ")
print(check_password(password))