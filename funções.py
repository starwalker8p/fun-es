def maior (a):
    print(f"{max(a)}")
def menor (a):
    print(f"{min(a)}")
def santo(a):
    if 'santo' in a[:5]:
        print(f"a cidade tem santo no nome")
    else:
        print(f"a cidade não tem santo no nome")
def aluguel(a,b):
    a = a*60
    b = b*0.15
    c = a+b
    print(c)