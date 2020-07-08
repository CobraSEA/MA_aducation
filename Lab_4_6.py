import string
users = {'Tom':'rtyf&', 'John':'876', 'Fil':'8ui'}
STR_P = set(list(string.punctuation))
try:
    login = input('Login:')
    if len(login) == 0:
        raise RuntimeError
    password = input('Password:')

    if users[login] != password:
        print('Access Denied')
    else:
        while bool(STR_P & set(users[login])):
            users[login] = input(f"Enter new password without {string.punctuation}:")
        else:
            print("Password has changed")
        print('Asccess Granted')


except ValueError:
    print('No Login')
except RuntimeError:
    print("Breach try!")
