from collections import Counter
d1={'a':100,'b':200,'c':300,'d':100}
d2={'a':200,'b':100,'d':200}
d=Counter(d1)+Counter(d2)
print(d)

