

def check():   
    username = input("Gib deinen Username ein: ")

    if len(username) > 12:
        print("Dein Username darf nicht länger als 12 Zeichen sein")
        check()
 
    elif not username.find(" ") == -1:
        print("Dein Username darf keine Leerzeichen besitzen")
        check()
    
    elif not username.isalpha():
        print("Dein Username darf keine Nummern beinhalten")
        check()
    else:
        print(f"Willkomen {username}!")

check()
