#week03_07.py

test = "i am a BOY"

print(test.count("a"))
print(test.count("A"))

print(test.find("a"))
print(test.find("q"))
print(test.find("am"))
print(test.find("qm"))

print(test.index("a"))
#print(test.index("q"))
print(test.index("am"))
if "qm" in test:
    print(test.index("qm"))

print(test.upper())
print(test.lower())
print(test.title())
print(test.capitalize())
print("/".join(test))

test = "   JMT Univercsity   "

print(";" + test.strip() + ";")
print(";" + test.rstrip() + ";")
print(";" + test.lstrip() + ";")
print(test)

print(test.replace("University", "High School"))

print(test.split())
print(test.split("i"))

'''
a = "%d%%" % 10
print (a)
'''
