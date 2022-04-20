import random
bitwidth = 62
a = 0x100bea9a4b25c717
b = 0x03d85abba0f51614
a_bit = [26, 26, 10]
b_bit = [17, 17, 17, 11]
sw = [17, 9, 8, 9, 8, 1, 8, 9, 8, 9, 17, 21]
op = [[0, 0], [0, 1], [1, 0], [0, 2], [1, 1], [0, 3], [2, 0], [1, 2], [2, 1], [1, 3], [2, 2], [2, 3]]

def only(a, b):
    bin_a = bin(a)
    bin_b = bin(b)
    la = len(bin_a) - 2
    lb = len(bin_b) - 2
    bin_a = "0" * (bitwidth - la) + bin_a[2:]
    bin_b = "0" * (bitwidth - lb) + bin_b[2:]
    # print(len(bin_a))
    # print("0b" + bin_a[0 : 10])
    # print(int(bin_a[0 : 10], 2))
    a_arr = [int(bin_a[0 : 10], 2), int(bin_a[10 : 36], 2), int(bin_a[36 : 62], 2)]
    b_arr = [int(bin_b[0 : 11], 2), int(bin_b[11 : 28], 2), int(bin_b[28 : 45], 2), int(bin_b[45 : 62], 2)]
    # print(a_arr)
    # print(b_arr)
    return [a_arr, b_arr]

def print_hex(l):
    for i in range(len(l)):
        print(hex(l[i]), end = "")
        if i != len(l) - 1:
            print(", ", end = "")
    print("")

def print_AB(AB):
    temp = ""
    for i in range(len(AB)):
        temp = AB[i] + temp
    print(hex(int(temp, 2)))

def mult():
    temp = only(a, b)
    A = list(reversed(temp[0]))
    B = list(reversed(temp[1]))
    print_hex(A)
    print_hex(B)
    C = 0
    AB = []
    for i in range(12):
        print(f"stage {i + 1}")
        print(f"A : {hex(A[op[i][0]])}, B : {hex(B[op[i][1]])}")
        stg = bin(A[op[i][0]] * B[op[i][1]] + C)[2:]
        print(f"s_{i + 1}_out : {hex(int(stg, 2))}")
        stg_bit = op[i][0] + op[i][1] + 1
        stg = "0" * (stg_bit - len(stg)) + stg
        AB.append(stg[-sw[i]:])
        # print(int(stg[: -sw[i]], 2))
        if stg[: -sw[i]] == "":
            C = 0
        else:
            C = int(stg[: -sw[i]], 2)
        print(f"carry : {hex(C)}, lsb : {hex(int(stg[-sw[i]:], 2))}")
    # print(AB)
    print_AB(AB)
    print(AB[-1])
    print(hex(int(AB[-1], 2)))


def main():
    mult()



if __name__ == '__main__':
    main()
