import numpy as np

def check():
    # df1 = np.loadtxt("./data_mod4/inv_w3_hex.txt", dtype = np.uint64)
    with open("./data/op1xop2.txt") as f:
        df1 = f.read().split("\n")
    with open("./data/mult_out4.txt") as f:
        df2 = f.read().split("\n")
    print("---check start---")
    for i in range(len(df1)):
        a = int(df1[i], 16)
        b = int(df2[i], 16)
        # print(i)
        if a != b:
            print(i)
            print(hex(a))
            print(hex(b))
            print("failed")
    print("---check end---")

def check_LH62():
    with open("./data/op1xop2.txt") as f:
        df1 = f.read().split("\n")
    with open("./data/LU62.txt") as f:
        df2 = f.read().split("\n")
    print("---check start---")
    print(df1[0])
    print(df2[0])
    for i in range(len(df1)):
        a_temp = int(df1[i], 16)
        a = int(bin(a_temp)[-62 : ], 2)
        b = int(df2[i], 16)
        # print(i)
        if a != b:
            print(i)
            print(hex(a))
            print(hex(b))
            print("failed")
    print("---check end---")

def check_UH62():
    with open("./data/op1xop2.txt") as f:
        df1 = f.read().split("\n")
    with open("./data/UH62.txt") as f:
        df2 = f.read().split("\n")
    print("---check start---")
    print(df1[0])
    print(df2[0])
    # for i in range(len(df1)):
    for i in range(10):
        a_temp = int(df1[i], 16)
        a = int(bin(a_temp)[2 : -62], 2)
        b = int(df2[i], 16)
        # print(i)
        if a != b:
            print(i)
            print(hex(a))
            print(hex(b))
            print("failed")
    print("---check end---")

def main():
    # print("hello")
    # df = np.loadtxt("./data_mod4/ntt_out_mod0.txt", dtype = np.uint64)
    # check_UH62()
    check_LH62()
    # check_intt_out()


if __name__ == '__main__':
    main()
