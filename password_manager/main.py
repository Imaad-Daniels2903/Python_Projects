import requests, encryption, os

exit_prog = ''
while exit_prog != 'exit' :
    file = open('passwords.txt', 'r+')
    passwords_raw = file.readlines()
    user_input = input('>>> ')
    os.system('cls' if os.name == 'nt' else 'clear')

    if user_input == 'exit' :
        exit_prog = 'exit'
        file.close()

    elif user_input == 'add' :
        print('Add Password')
        accName = input('Account Name: ')
        accPassword = input('Account Password: ')
        file.write('\n' + accName + ':' + accPassword)
        os.system('cls' if os.name == 'nt' else 'clear')
        file.close()

    elif user_input == 'encrypt' :
        print('Encrypt Password')
        accName = input('Account Name: ')
        for i in range(len(passwords_raw)):
            accLine = passwords_raw[i].split(':')
            if accLine[0] == accName:
                print(encryption.encrypt_text(accLine[1]))

    elif user_input == 'cls' :
        os.system('cls' if os.name == 'nt' else 'clear')

    elif user_input == 'lu' :
        print('Lookup Passwords')
        user_input = input('Account: ')
        for i in range(len(passwords_raw)):
            account_name = passwords_raw[i].split(':')
            if account_name[0] == user_input.lower():
                print(account_name[1])

    elif user_input == 'edit' :
        print('Edit Passwords')
        user_input = input('Account: ')
        for i in range(len(passwords_raw)):
            account_name = passwords_raw[i].split(':')
            if account_name[0] == user_input.lower():
                new_password = input('New Password: ')
                account_name[1] = new_password
                passwords_raw[i] = '\n' + ':'.join(account_name)                file.writelines(passwords_raw)
                file.close()

