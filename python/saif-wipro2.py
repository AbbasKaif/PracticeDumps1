a, b, c = map(int, input().split(" "))

k1 = min(a//1000, b//1000, c//1000)

a1, b1, c1 = a%1000, b%1000, c%1000
k2 = max(a1//100, b1//100, c1//100)

a2, b2, c2 = a%100, b%100, c%100
k3 = min(a2//10, b2//10, c2//10)

k4 = max(a%10, b%10, c%10)

key = str(k1)+str(k2)+str(k3)+str(k4)
print(key)