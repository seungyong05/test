# week06_03.py
myInfo = {}

myInfo["n"] = "김인하"
myInfo["a"] = 23
myInfo["h"] = 163.2
print(myInfo)

myInfo["h"] = 173.2
print(myInfo)

del myInfo["h"]
print(myInfo)

# print(f"키:{myInfo['h']}cm")

if 'h' in myInfo:
    print(f"키:{myInfo['h']}cm")
else:
    print("키 자료 없음")

print(f"키:{myInfo.get('h')}cm")

if myInfo.get('h'):
    print(f"키:{myInfo['h']}cm")    
else:
    print("키 자료 없음")

h = myInfo.get('h')
if h:
    print(f"키:{h}cm")    
else:
    print("키 자료 없음")

print(f"키:{myInfo.get('h', '--')}cm")

myInfo.clear()
print(myInfo)













