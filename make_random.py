import random

def utils():
    op1 = []
    op2 = []
    op1xop2 = []

    for i in range(100):
        op1_temp = random.randint(0, 2 ** 62 - 1)
        op2_temp = random.randint(0, 2 ** 62 - 1)
        op1_hex = hex(op1_temp)
        op1.append("0" * (16 - len(op1_hex) + 2) + op1_hex[2:])
        op2_hex = hex(op2_temp)
        op2.append("0" * (16 - len(op2_hex) + 2) + op2_hex[2:])
        op1xop2.append(hex(op1_temp * op2_temp))

    with open(f"./data/op1.txt", "wt") as f:
        for i in range(len(op1)):
            if i == len(op1) - 1:
                f.write(op1[i])
            else:
                f.write(op1[i] + "\n")

    with open(f"./data/op2.txt", "wt") as f:
        for i in range(len(op2)):
            if i == len(op2) - 1:
                f.write(op2[i])
            else:
                f.write(op2[i] + "\n")

    with open(f"./data/op1xop2.txt", "wt") as f:
        for i in range(len(op1xop2)):
            if i == len(op1xop2) - 1:
                f.write(op1xop2[i])
            else:
                f.write(op1xop2[i] + "\n")

def main():
    utils()



if __name__ == '__main__':
    main()
