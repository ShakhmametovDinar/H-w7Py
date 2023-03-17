dict = 'ауыоеёюиэя'
a = input().split()
res = [sum(True for i in word if i in dict) for word in a]

print(res)
if len(set(res)) ==1:
    print("Парам пам-пам")
else:
    print("Пам парам")
