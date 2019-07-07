import sys

def ceaser(s,n):
    d = {}
    for c in (65, 97):
        for i in range(26):
            #ずらす方向を変える時は(i - n)を+にする
            d[chr(i+c)] = chr((i + n) % 26 + c)
    
    return "".join([d.get(c,c) for c in s])

def usage():
    print("Error!!")
    print("--Usage--")
    print("rot.py [encrypt txt] [shift count]")
    print("---------")

def main():
    try:
        args = sys.argv
        encrypt_txt = args[1]
        rot = int(args[2])
        t = ceaser(encrypt_txt, rot)
        print(t)

    except:
        usage()

main()