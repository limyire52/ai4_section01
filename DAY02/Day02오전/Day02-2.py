# 논리연산자
# and = 곱의 의미 (하나라도 F 면 F), 그리고 
# or  = 더하기의 의미 (하나라도 T 면 T), 혹은 

# isSuccess = True    # is 붙이면 ~했니? 라는 의미
# isPass = False

# if isSuccess and isPass:
#     print('A')
# else:
#     print('B')

# isSuccess = True    
# isPass = False

# if isSuccess or isPass:
#     print('A')
# else:
#     print('B')


# 단락평가 Short-circuit

def expensive_check():
    print("시간이 오래 걸리는 함수 실행")
    return True # 참으로 지정

is_active = False

if is_active and expensive_check():
    print('통과')
else :
    print('차단 ( expensive_check 실행 안됨)')

def expensive_check():
    print("시간이 오래 걸리는 함수 실행")
    return True # 참으로 지정

is_active = False

if is_active or expensive_check():
    print('통과')
else :
    print('차단 ( expensive_check 실행 안됨)')

# None 값을 방어
user_profile = None

if user_profile is not None and user_profile.get('is_verified'):
    print('인증된 사용자')
else:
    print('비인증된 사용자')
