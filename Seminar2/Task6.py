#банкомат
# начальнас сумма = 0
# действия: пополнить, снять, выйти
# суммы пополнения и снятия кратны 50 у.е.
# процент за снятие 1.5% не менее 30 и неболее 600
# после каждой 3 операции снятия или поплнения начисляются проценты = 3%
# нельзя снять больше чем на счете
# если больше 5 млн - налог на богатство 10% перед каждой операцией, даже ошибочной
# любое действие выводит сумму денег

import datetime

balance = 350
oper_list = {}
date_time = datetime.datetime.now()
print(date_time)
count = 0

def minus(summ):
    """снятие
    """
    global balance
    global oper_list
    percent = (balance / 100) * 1.5 
    if balance > summ + percent:
        if 30 > percent:
            percent = 30
        elif percent > 600:
            percent = 600
        balance = balance - summ - percent
        oper_list.setdefault(date_time, ['снятие', summ])
        print(balance, oper_list)
    else:
        print("Баланс с учетом % за снятие меньше снимаемой суммы")
    return balance


def plus_(summ):
    """внесение
    """
    global balance
    global oper_list
    balance = float(balance + summ)
    oper_list.setdefault(date_time, ['пополнение', summ]) # не добавляет
    print(balance, oper_list)# нет словаря с операциями
    return balance


def bye():
    """выход
    """
    print("бланс" + str(balance))
    print("До свидания")
    exit()
    
    
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
                balance = plus_(user_summ)
                count += 1

        case "2":
            user_summ = int(input("Введите сумму, кратную 50: "))
            if user_summ % 50 != 0:
                print("Вы ввели неверную сумму и вернетесь в главное меню. Баланс: "+ str(balance))
                continue
            else:
                balance = minus(user_summ)
                count += 1
                
        case "3":
            bye()
            
        case _:
            print("Вы ввели неверные данные")
            continue