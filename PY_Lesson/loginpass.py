login = input('Введите ваш логин: ')
password = input('Введите ваш пароль: ')

while password != '1q2w3e4r5t6y' or login != 'user' :
    print('Пароль или логин неверны!')
    login = input('Введите ваш логин: ')
    password = password = input('Введите ваш пароль: ')
print('Добро пожаловать в аккаунт!')