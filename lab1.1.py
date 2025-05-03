import itertools # Импортируем модуль, который содержит функции для генерации перестановок
def fun():
    n = int(input("Введите число n"))
    perms = list(itertools.permutations(range(1, n + 1))) 
    print(len(perms)) #выводит общее число перестоновок
    for perm in perms: #Перебирает все перестановки в списке
        print(*perm)
fun()