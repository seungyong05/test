# week06_03.py
info = {}
info["n"] = "김인하"
info["a"] = 23
info["h"] = 163.2
print(info)

info["h"] = 173.2
print(info)

del info["h"]
print(info)

# print(f"키:{info['h']}cm")

if "h" in info:
    print(f"키:{info['h']}cm")

if "a" in info:
    print(f"나이:{info['a']}세")    

h = info.get('h')
if h:
    print(f"키:{h}cm")

a = info.get('a')
if a:
    print(f"나이:{a}세")    

print(f"키:{info.get('h')}cm")
print(f"키:{info.get('h', '__')}cm")







    
    









