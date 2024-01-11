m = []
s = ['end'] #ключ стопер
while True:
    n = input().split() #аутпут сплит
    if n == s:
        break
    else:
        k = min(n, key=int) #поиск минимального
        m.append(k)
for i in m: #вывод
    print(i)