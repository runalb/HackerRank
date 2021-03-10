# sWAP cASE

def swap_case(s):
    res = ""
    for ch in s:
        if ch.isupper():
            res = res + ch.lower()

        else:
            res = res + ch.upper()

    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)