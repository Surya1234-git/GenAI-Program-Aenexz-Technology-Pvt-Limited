username = input("Enter a username: ")

if username.strip() == "":
    print("Invalid username: it cannot be only spaces")
elif len(username) < 5:
    print("Invalid username: it should have at least 5 characters")
elif username.lower() == "admin":
    print("Invalid username: admin is not allowed")
else:
    print("Valid username")
