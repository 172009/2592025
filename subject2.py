import sympy as sp

#trash
answer_main = input("Type subject cagetory: ")

try:
    answer_main = int(answer_main)
except:
    print("get out")
a = float(input("enter a:"))
b = float(input("enter b:"))
c = float(input("enter c:"))

try:
    a = float(a)
    b = float(b)
    c = float(c)
except:
    print("please enter number")

if answer_main == 1:
    smallest_value = min(a, b, c)
    biggest_value = max(a, b, c)
    print(f"the biggest value is {biggest_value}, smallest value is {smallest_value}")
elif answer_main == 2:
    x = sp.symbols("x")
    pt = sp.Eq(a*x**2 + b*x + c, 0)
    nghiem = sp.solve(pt, x)
    print(f"nghiem cua phuong trinh {pt} la {nghiem}")
elif answer_main == 3:
    x = sp.symbols("x")
    pt =sp.Eq(b*x + c, 0)
    nghiem = sp.solve(pt, x)
    print(f"nghiem cua phuong trinh {pt} la {nghiem} ")
elif answer_main == 4:
    d = float(input("enter d:"))
    m = float(input("enter m:"))
    n = float(input("enter n:"))
    try:
        n = float(n)
        m = float(m)
        d = float(d)
    except ValueError:
        print("please type number")
    x = sp.symbols("x")
    y = sp.symbols("y")
    pt1 = sp.Eq(a*x + b*y, m)
    pt2 = sp.Eq(c*x + d*y, n)
    nghiem = sp.solve([pt1, pt2], (x, y))
    print(f"nghiem cua phuong trinh {pt1} cung {pt2} la {nghiem}")
elif answer_main == 5:
    print(f"chu vi tam giac abc la {a+b+c}, dien tich tam giac abc la ???")
elif answer_main == 6:
    money_cost = int(input("input money cost: "))
    name = str(input("please enter the names: "))
    ages = int(input("please enter ages: "))
    months_buys = int(input("please enter how much month you want to buys: "))
    try:
        money_cost = int(money_cost)
        name = str(name)
        ages = int(ages)
        months_buys = int(months_buys)
    except ValueError:
        print("please double check anything!")

    if ages <= 18:
        print(f"Gia ve thang: {money_cost}\nHo va ten: {name}\nTuoi: {ages}\nSo thang: {months_buys}\nSo tien phi: {(money_cost*months_buys)*0.9}")
    elif ages > 18:
        print(f"Gia ve thang: {money_cost}\nHo va ten: {name}\nTuoi: {ages}\nSo thang: {months_buys}\nSo tien phi: {money_cost*months_buys}")
elif answer_main == 7:
    value = int(input("enter value please: "))
    try:
        value = int(value)
    except:
        print("get out!")
    if value > 0:
        print("so duong!")
    if value == 0:
        print("bang 0!")
    else:
        print("so am!")