# week06_04.py
fruites = {"kim": "딸기", "lee": "귤"}

for f in fruites:
    print(f, fruites[f])

for f in fruites.keys():
    print(f, fruites[f])

for f in fruites:
    # print(f, fruites['f'])
    pass

for f in fruites.values():
    print(f)

for f in fruites.items():
    print(f)

c = (1, 2)
a, b = c
print(a, b, c)
print(c[0], c[1], c)

for k, v in fruites.items():
    print(k, v)


a = {"h": 127.0, "w": 30, "e": 2.0}
b = {"h": 160, "w": 40}
c = [a, b]
for idx, ele in enumerate(c):
    print(f"{idx+1}번 키:{ele['h']}")
    print(f"{idx+1}번 키:{c[idx]['h']}")

a = {"source": "고추장", "topping": ["버섯", "계란"]}

print(f"양념:{a['source']}")
topping = "/".join(a["topping"])
print(f"고명:{topping}")

a = {
    "kim": {1: "귤", 2: "사과"},
    "lee": {1: "귤"},  # , 2:'딸기'},
}

for k, v in a.items():
    print(f"{k}씨가 좋아하는 과일")
    # 반복문 처리
    print(f"{v[1]}, {v[2]}")
