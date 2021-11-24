email = input("Enter your email address: ").strip()

e_list = list(email)
element = '@'
true_domain = ['hotmail.com', 'live.com', 'msn.com', 'yahoo.com', 'ymail.com', 'rocketmail.com',
            'yahoomail.com', 'yahoo-inc.com', 'gmail.com', 'googlemail.com', 'aol.com', 'mail.ru',
            'list.ru', 'bk.ru', 'inbox.ru', 'corp.mail.ru', 'yandex.ru', 'rambler.ru', 'qip.ru',
            'bigmir.net', 'ukr.net', 'kimo.com', ]
if element not in e_list:
    print("You entered the wrong email address")
else:
    index = email.index(element)
    username = email[:index]
    domain = email[index+1:]
    if domain not in true_domain:
        print("You have entered an email address with an incorrect domain name")
    else:
        print("\nYour email address: ", email)
        print("Username: ", username)
        print("Domain name: ", domain)