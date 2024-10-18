
scores_dict = {
    'A': {'국어': 49, '수학': 43, '영어': 49},
    'B': {'국어': 80, '수학': 60, '영어': 82},
    'C': {'국어': 20, '수학': 85, '영어': 48},
    'D': {'국어': 100, '수학': 30, '영어': 50},
    'E': {'국어': 80, '수학': 90, '영어': 100}
}


averages_dict = {}
for student, subjects in scores_dict.items():  
    total = sum(subjects.values())            
    avg = total / len(subjects)                
    averages_dict[student] = avg               


print("학생별 평균:", averages_dict)
