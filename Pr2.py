def AmountDays(year):
    january = 31
    if (year % 4 == 0):
        february = 29
    else: february = 28
    march = 31
    april = 30
    may = 31
    june = 30
    july = 31
    august = 31
    september = 30 
    october = 31
    november = 30
    december = 31
    
    months = [january, february, march, april, may, june, july, august, september, october, november, december]
    itog = 0
    for i in range(len(months)):
        itog += summa(months[i])
    return itog

def summa(month):
    i = 1
    month += 1
    itog = 0
    for i in range(month):
        if (month < 10):
            itog += i
        else: itog += (i // 10) + (i % 10)
    return itog

x = int(input("Введите год: "))
if(x > 0):
    print(AmountDays(x))
else:
    print("Ну ты дурак? Сам подумай что ты написал")