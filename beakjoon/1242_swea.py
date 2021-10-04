T = int(input())

hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

pattern_dict = {
    "211": 0,
    "221": 1,
    "122": 2,
    "411": 3,
    "132": 4,
    "231": 5,
    "114": 6,
    "312": 7,
    "213": 8,
    "112": 9,
}

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]

    data_set = list(set(data))
    N2 = len(data_set)

    data_to_binary = [""] * N2
    for i in range(N2):
        for j in range(M):
            data_to_binary[i] += hex_to_bin[data_set[i][j]]

    clean_data_to_binary = []
    for x in data_to_binary:
        if int(x) != 0:
            clean_data_to_binary.append(x)

    result = 0
    visited = []
    for binary_code in clean_data_to_binary:
        NewCode = []
        a = b = c = d = 0
        binary_code = binary_code.rstrip("0")
        L = len(binary_code)
        for i in range(L - 1, -1, -1):
            if c == 0 and binary_code[i] == "1":
                d += 1
            elif d > 0 and b == 0 and binary_code[i] == "0":
                c += 1
            elif a == 0 and binary_code[i] == "1":
                b += 1
            elif b > 0 and c > 0 and d > 0 and binary_code[i] == "0":

                div = min(b, c, d)
                b //= div
                c //= div
                d //= div
                key = str(b) + str(c) + str(d)
                NewCode = [pattern_dict[key]] + NewCode
                a = b = c = d = 0

            if len(NewCode) == 8:
                if ((NewCode[0] + NewCode[2] + NewCode[4] + NewCode[6]) * 3 + NewCode[1] + NewCode[3] + NewCode[5] +
                    NewCode[7]) % 10 == 0:
                    if NewCode not in visited:
                        result += sum(NewCode)
                        visited.append(NewCode)
                NewCode = []
    print(f"#{tc} {result}")
