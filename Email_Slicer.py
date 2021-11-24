email = input("Enter your email address: ").strip()

e_list = list(email)
element = '@'

if element not in e_list:
    print("You entered the wrong email address")
else:
    index = email.index('@')
    username = email[:index]
    domain = email[index+1:]

    print("\nYour email address: ", email)
    print("Username: ", username)
    print("Domain name: ", domain)