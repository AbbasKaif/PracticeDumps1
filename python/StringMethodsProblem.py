"""
len() and str() practice:
1.create a variable and assign it the string "Python"
2.create another variable and assign it the length of the string assigned to the variable in step 1
3.create a variable and use string slicing and len() to assign it the length of the slice "yth" from the string assigned
 to the variable from step 1
4.create a variable and assign it the float 1.32
5.create a variable and assign it the string "2" from the float assigned to the variable from the last problem (use the
 str() string method for this)
"""
var1="Python"
var2=len(var1)
var3=len(var1[1:4])
var4=1.32
var5=str(var4)[3]
print var1
print var2
print var3
print var4
print var5

"""
.upper() and .lower() practice:
1.create a variable and assign it the string "upper" changed to "UPPER" using .upper()
2.create a variable and assign it the string "owe" from "LOWER" using string slicing and .lower()
"""

var6="upper".upper();
var7="LOWER"[1:4].lower();
print var6
print var7
