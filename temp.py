import random

def utils():
    s = [186, 89, 71, 71, 55, 5, 39, 35, 23, 17, 16]
    lsb = [17, 9, 8, 9, 8, 1, 8, 9, 8, 9, 17]
    last = []
    for i in range(len(s)):
        if i != len(s) - 1:
            tex = f"s{i + 1} <=" + "{" + f"s{i + 1}[{s[i] - lsb[i]} : 0], s{i + 1}_out[{lsb[i] - 1} : 0]" + "};"
            print(tex)
            last.append(f"s{i + 1}[{s[i]} : {s[i] - lsb[i] + 1}]")
        else:
            print(f"s{i + 1} <= s{i + 1}_out[{lsb[i] - 1} : 0];")
            last.append(f"s{i + 1}")
        # print(f"s{i + 1}_last <= s{i + 1}[{s[i]} : {s[i] - lsb[i] + 1}];")
    temp = list(reversed(last))
    for i in range(len(temp)):
        print(temp[i], end="")
        if i != len(temp) - 1:
            print(", ", end = "")
        else:
            print("")
def main():
    utils()



if __name__ == '__main__':
    main()
