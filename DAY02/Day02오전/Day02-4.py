# 삼항연산자

user_score = 85

if user_score >= 80:
    grade = 'Pass'
else:
    grade = 'Fail'

# 5번-8번 문장을 삼항연산자로 표현하면 한줄로 할당할 수 있다.

grade = 'Pass' if user_score >= 80 else 'Fail'
print(grade)
