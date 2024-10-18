#week05_07.py
scores = []

while True:
    score = input("점수:")
    if not score.strip():
        break
    scores.append(float(score))

if len(scores):
    number = 0
    summary = 0
    for score in scores:
        number += 1
        summary += score
        print(f"(number) 점수:[score]")
    print(f"총 평균 : [summary/len(score)]")
else:
    print("점수가 없어요!")
