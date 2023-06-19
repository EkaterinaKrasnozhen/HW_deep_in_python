#банкомат
# начальнас сумма = 0
# действия: пополнить, снять, выйти
# суммы пополнения и снятия кратны 50 у.е.
# процент за снятие 1.5% не менее 30 и неболее 600
# после каждой 3 операции снятия или поплнения начисляются проценты = 3%
# нельзя снять больше чем на счете
# если больше 5 млн - налог на богатство 10% перед каждой операцией, даже ошибочной
# любое действие выводит сумму денег

# снятие
def minus(summ, balance):
    percent = (balance / 100) * 1.5 # по-моему на семинаре озвучили, что % \
        #именно от общего баланса, но наверно правильнее от суммы снятия. Делаю от общего баланса
    if balance > summ + percent:
        if 30 > percent:
            percent = 30
        elif percent > 600:
            percent = 600
        balance = balance - summ - percent
        print(balance)
    else:
        print("Баланс с учетом % за снятие меньше снимаемой суммы")
    return balance

# внесение
def plus_(summ, balance):
    balance = float(balance + summ)
    print(balance)
    return balance

# выход
def bye():
    print("бланс" + str(balance))
    print("До свидания")
    exit()
    
    
count = 0
balance = 6000000000000

#не пойму куда вводить переменные balance и count чтобы внутри бесконечного цикла сохранялись текущие значения?
while True:
    
    answer = input("Действия: 1 - Пополнить, 2 - Снять, 3 - Выход")
    
    if count % 3 == 0 and count != 0 :
        balance = balance * 1.3
        print("Ура, вы получили 3% бонуса " + str(balance))
    
    if balance > 5000:
        balance /= 10
        print("налог на богатство минус 10%, баланс = " + str(balance))
    
    
    match answer:
        
        case "1":
            user_summ = int(input("Введите сумму, кратную 50: "))
            if user_summ % 50 != 0:
                print("Выввели неверную сумму и вернетесь в главное меню. Баланс: "+ str(balance))
                continue
            else:
                balance = plus_(user_summ, balance)
                count += 1

        case "2":
            user_summ = int(input("Введите сумму, кратную 50: "))
            if user_summ % 50 != 0:
                print("Вы ввели неверную сумму и вернетесь в главное меню. Баланс: "+ str(balance))
                continue
            else:
                balance = minus(user_summ, balance)
                count += 1
                
        case "3":
            bye()
            
        case _:
            print("Вы ввели неверные данные")
            continue