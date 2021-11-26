a = 149

def bit_2(a):
    global result
    result =''
    while a:
        result += str(a%2)
        a = a//2
    return result

bit_2(149)
print(result)