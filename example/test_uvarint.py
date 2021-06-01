
def byte(x):
    ret = []
    while x > 1:
        ret.append(str(x % 2))
        x = x >> 1
    ret.append(str(x))
    ret.reverse()
    s = ''.join(ret)
    if len(s) >= 8:
        return s[-8:]
    else:
        return "".join((["0"] * (8-len(s)))) + s


hex_dic = {}
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('a'),ord('a')+6)]
for i in range(len(base)):
    hex_dic[i] = base[i]


def dec2hex(x):
    a = int(x[0]) * 8 + int(x[1]) * 4 + int(x[2]) * 2 + int(x[3])
    b = int(x[4]) * 8 + int(x[5]) * 4 + int(x[6]) * 2 + int(x[7])

    return hex_dic[a] + hex_dic[b]


def convert(x):
    val = byte(x)
    val = "1" + val[1:]
    return dec2hex(val)


def put_uvarint(x):
    i = 0
    s = ""
    while x >= 0x80:
        s += str(convert(x))
        print(s)
        x = x >> 7
        i = i + 1

    # print("last x:", str(x), s, byte(x))
    s += dec2hex(byte(x))
    return s


#print(byte(1))
#print(convert(1))
#print(put_uvarint(1521625823))

print(put_uvarint(2))

