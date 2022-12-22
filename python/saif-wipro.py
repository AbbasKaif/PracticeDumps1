num = input()
no_of_digits = len(num)
s, even, odd = 0, 0, 0
for i in num:
    s += int(i) ** no_of_digits
if(int(num) == s):
    even += sum([int(i) for i in num if int(i) % 2 == 0])
    print(even)
else:
    odd += sum([int(i) for i in num if int(i) % 2 == 1])
    print(odd)