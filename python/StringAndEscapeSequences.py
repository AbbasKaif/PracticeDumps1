"""
string and escape sequences:
1.create a variable and assign a string that is surrounded in double quotes to it
2.create a variable and assign a string that is surrounded in single quotes to it
3.create a variable and assign it a string that uses the double quote escape sequence within it
4.create a variable and assign it a string that uses the single quote escape sequence within it
"""
var1="My name is Kaif Abbas."
var2='My name is Kaif Abbas.'
var3="My name is \"Kaif Abbas\"."
var4='My name is \'Kaif Abbas\'.'

"""
accessing values by index and string slicing:
1.create a variable called lannisters and assign it the string "JaimeCerseiTyrion"
2.create a variable and assign it the "a" from the string assigned to the variable lannisters.
3.create a variable and assign it the "J" from the string assigned to the variable lannisters.
4.create a variable and assign it "Jaime" from the string assigned to the variable lannisters.
5.create a variable and assign it "Cersei" from the string assigned to the variable lannisters.
6.create a variable and assign it "Tyrion" from the string assigned to the variable Lannisters.
"""

lannisters="JaimeCerseiTyrion"
var5=lannisters[1]
var6=lannisters[0]
var7=lannisters[0:5]
var8=lannisters[5:11]
var9=lannisters[11:]

print var1
print var2
print var3
print var4
print var5
print var6
print var7
print var8
print var9