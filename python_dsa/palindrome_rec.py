s="hello"
n=len(s)
l=0
r=n-1

def func(s,l,r):
    if l>=r:
        return True
    
    if s[l]!=s[r]:
        return False
    return func(s,l+1,r-1)

print(func(s, l, r))