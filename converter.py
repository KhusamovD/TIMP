# 10.04.18
rub = 1
dollar = 58.2
euro = 71.8
yen = 0.56
v = [rub, dollar, euro, yen]
t = ['в рублях', 'в долларах', 'в евро', 'в йенах']


def convert(money, ind):
    return [t[ind], str(round(money / v[ind], 3))]