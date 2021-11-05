def email_validity():
    email = str(input("Enter e-mail: "))

    if "@" in email and "." in email:
        return True
    else:
        return False

if email_validity() == True:
    print("Valid e-mail.")
else:
    print("Invalid e-mail.")