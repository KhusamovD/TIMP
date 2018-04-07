flag = "+"
while flag == "+":
    print("\n" "Добро пожаловать в НАциональный Единый БАНК кредитования в иностранной валюте")

    nok = 69
    usd = 57
    print ("\n" "Курс Шведской кроны = ", nok, "\n" "Курс доллара =", usd)

    currency = int(input("\n Введите код валюты, в которой вы хотите взять кредит: Крона - 1, Доллар - 2:"))
    x = (input("\nВведите с какой целью вы хотите взять кредит: "))

    if currency == 1:
        money=int(input("Введите необходимое количество крон"))
        if money > 0:
             rate = int(input("Введите процентную ставку = "))
             period = int(input("Введите период на который вы берете кредит = "))
             result = round((((money*rate)/100)+money),0)
             mounth = round(result/period,2)
             print("Вам надо будет отдать банку: ",result,"Евро","или по",mounth,"Евро в течении",period,"месяцев")
        else:
             print ("\n""Введите сумму отличную от нуля")

    elif currency==2:
        money = int(input("Введите необходимое количество долларов сша"))
        if money > 0:
            rate = int(input("Введите процентную ставку = "))
            period = int(input("Введите период на который вы берете кредит = "))
            result = round((((money * rate) / 100) + money), 0)
            mounth = round(result / period, 2)
            print("Вам надо будет отдать банку: ", result, "Евро", "или по", mounth, "Евро в течении", period, "месяцев")
        else:
           print("\n""Введите сумму отличную от нуля")
flag = input("\tЖелаете еще взять кредит? ( + или - ) ")