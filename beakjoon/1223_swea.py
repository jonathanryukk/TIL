T = 10
for tc in range(1, T + 1):

    N = int(input())
    emp = input()

    emp_int = ''
    emp_temp = []
    for i in emp:
        if i == '*':
            emp_temp.append(i)
        elif i == '+':
            while emp_temp:
                emp_int += emp_temp.pop()
            emp_temp.append(i)
        else:
            emp_int += i
    while emp_temp:
        emp_int += emp_temp.pop()

    result = []
    for i in emp_int:

        if i == '*':
            emp2 = result.pop()
            emp1 = result.pop()
            emp3 = emp1 * emp2
            result.append(emp3)

        elif i == '+':
            emp2 = result.pop()
            emp1 = result.pop()
            emp3 = emp1 + emp2
            result.append(emp3)

        else:
            result.append(int(i))
    print("#{} {}".format(tc, result[0]))
