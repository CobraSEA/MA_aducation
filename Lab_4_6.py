import string
users = {'Tom':'rtyf&', 'John':'876', 'Fil':'8ui@'}
#STR_P = set(list(string.punctuation))
STR_P = {x for x in string.punctuation}
try:
    login = input('Login:')
    if len(login) == 0:
        raise RuntimeError
    password = input('Password:')

    if users[login] != password:
        print('Access Denied')
    else:
        while bool(STR_P & set(users[login])) or len(users[login]) <= 0:
            users[login] = input(f"Enter new password without {string.punctuation} and not empty:")
            if len(users[login]) <= 0:
                continue
            if not bool(STR_P & set(users[login])):
                print("Password has changed")
        print('Access Granted')


except ValueError:
    print('No Login')
except RuntimeError:
    print("Breach try!")
else:
    print("The End")