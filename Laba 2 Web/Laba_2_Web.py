import functools, time
#Декоратор, который кэширует результат и считает сколько раз отдается результат
def Customcache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count +=1
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper.cache:
            wrapper.cache[cache_key] = func(*args, **kwargs)
        return wrapper.cache[cache_key]
    wrapper.cache = dict()
    wrapper.count = 0
    return wrapper

#Функция для определения палиндрома
def Palindrom(x):
    temp_x = x
    rev = 0
    while(x > 0):
        dig = x % 10
        rev = rev * 10 + dig
        x = x // 10
    if (temp_x == rev):
        return True
    else:
        return False
#Функция для сортировки чисел по делению без остатка на 2, 3, 5
def DevBy235(lst):
    two = []
    three = []
    five = []
    for i in lst:
        if i%2 == 0:
            two.append(i)
        if i%3 == 0:
            three.append(i)
        if i%5 == 0:
            five.append(i)
    return two, three, five
#Функция для трансформации числа в обратное ему
def ReversedInt(x):
    rev_x = 0
    if(x > 0):
        while(x > 0):
            dig = x % 10
            rev_x = rev_x * 10 + dig
            x = x // 10
    elif(x < 0):
        x = x - 2*x
        while(x > 0):
            dig = x % 10
            rev_x = rev_x * 10 + dig
            x = x // 10
        rev_x = rev_x - 2 * rev_x
    return rev_x
#Функция - Алгоритм нахождения корня n-ной степени
def NewtonsFormula(a,n):
    pog = 0.001
    root = a / n
    rn = a
    while abs(root-rn) >= pog:
        rn = a
        for i in range(1,n):
            rn = rn / root
        root = 0.5 * (rn + root)
    return root
#Функция для определения простого числа
def SimpleNum(a):
    if(a>=0 and a<=100000):
        x = 2
        while a % x != 0:
            x+=1
        return x == a
    else:
        return"Wrong number, try again"
#Встроенная стандартная библиотека с декоратором и кэшированием
#@functools.lru_cache()
@Customcache
#Функция чисел Фибоначчи
def Fibonacci(num):
    if num < 2:
        return num
    return Fibonacci(num - 1) + Fibonacci(num - 2)

#Функция для выбора других функций
def FuncChooser(a):
    if a == '0':
        print ("Exiting...")
    elif a == '1':
        x = int(input("Enter the num to check:"))
        print(Palindrom(x))
    elif a == '2':
        lst = []
        for el in input("Enter the numbers:").split():
            lst.append(int(el))
        f = (DevBy235(lst))
        for i in f:
            print (i)
            #for i in range(len(f)):
                #print (f[i]) - еще можно выводить так по индексам (для справки)
    elif a == '3':
        x = int(input("Enter the num to reverse:"))
        print("Result:", ReversedInt(x))
    elif a == '4':
        a = float(input("Enter a number:"))
        n = int(input("Enter degree:"))
        print("Result:",NewtonsFormula(a,n))
    elif a =='5':
        a = int(input("Enter a number:"))
        print(SimpleNum(a))
    elif a =='6':
        num = int(input("Enter a number:"))
        start = time.perf_counter();Fibonacci(num);print('Time run:', time.perf_counter()-start)
        print("Result:",Fibonacci(num))
        print("Count:",Fibonacci.count)
    else:
        print ("There is no such function!")

a=''

while a != '0':
    print("\nChoose func:\n0.Exit\n1.Palindrom\n2.DevBy235\n3.ReversedInt\n4.NewtonsFormula\n5.SimpleNum\n6.Fibonacci")
    a = input()
    FuncChooser(a)
    