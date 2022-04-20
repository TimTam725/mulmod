def op():
    for i in range(1, 12):
        # if i < 6:
        #     print(f"A0[{i}] <= A0[{i - 1}];")
        if i < 6:
            print(f"A1[{i}] <= A1[{i - 1}];")
        if i < 5:
            print(f"A2[{i}] <= A2[{i - 1}];")
        if i < 5:
            print(f"B0[{i}] <= B0[{i - 1}];")
        if i < 7:
            print(f"B1[{i}] <= B1[{i - 1}];")
        if i < 9:
            print(f"B2[{i}] <= B2[{i - 1}];")
        if i < 10:
            print(f"B3[{i}] <= B3[{i - 1}];")

def s1():
    for i in range(1, 12):
        print(f"s1[{i}] <= s1[{i - 1}];")

def LU62():
    for i in range(8):
        for j in range(1, 8 - i - 1):
            print(f"s{i + 1}[{j}] <= s{i + 1}[{j - 1}];")

def main():
    # s1()
    LU62()



if __name__ == '__main__':
    main()
