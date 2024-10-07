first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
zp = zip(first,second)
first_result = (len(x)-len(y) for x,y in zp if len(x)!=len(y))
third = first + second
second_result = second_result = (len(first[i]) - len(second[i]) for i in range(len(first)) if i < len(second))
print(list(first_result))
print(list(second_result))