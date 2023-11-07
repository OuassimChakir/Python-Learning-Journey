login = input("Login: ")
password = input("Password: ")
if(login.lower() == "admin" and password == "admin"):
    print("Bienvenue")
else:
    print("Le login ou le Mot de passe est Incorrect")