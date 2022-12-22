def solve(s):
    k = s
    rev = ""
    for i in k:
        rev = i + rev
    return(rev)
s = input()
out_ = solve(s)
print(out_)