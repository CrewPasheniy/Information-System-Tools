m = []
s = ['end'] #команда остановки 
while True:
    n = input().split() #вводим через сплит
    k = min(n) #поиск минимального значения
    if n == s:
        break
    m.append(k)
for i in m: #вывод
    print(i)
