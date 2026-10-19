class Safeprofile:
    def get(self,a):
        return True

user_profile = Safeprofile()
if user_profile and user_profile.get(): 
    print('성공')
else:
    print('실패')
# -> 실패

user_profile = Safeprofile()
if user_profile and user_profile.get('is_verified'): 
    print('성공')
else:
    print('실패')
# -> 성공

class Safeprofile:  # 함수들을 하나로 묶어줌
    def _init_(self): 
        pass
    def get(self,key):  # 만든 함수
        return True
    def set(self,key):  # 만든 함수
        return True

# 객체의미 설명
user_profile1 = Safeprofile()
user_profile2 = Safeprofile()
user_profile3 = Safeprofile() # 같은 설계도로 여러가지 객체를 만들 수 있다. 

if user_profile and user_profile.get('is_verified'): 
    print('성공')
else:
    print('실패')