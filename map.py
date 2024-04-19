scores = [88, 92, 78, 60, 75, 95]

def convert_to_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

grade=list(map(convert_to_grade,scores))
print(grade)