# print("2 x 1 = 2")
# print("2 x 2 = 4")
# print("2 x 3 = 6")
# print("2 x 4 = 8")

# 반복문 : 비슷한 모양이 반복되어도 사용할 수 있음

# i = 1
# print(f"2 x {i} = {2*i}")

# for i in range(1,10) : # 1,2,3,4 만큼만 반복
#     print(f"2 x {i} = {2*i}") # 2를 3으로 바꾸면 구구단이 3단이 된다.

# for dan in range(2,10) :    
#     for i in range(1,10) :  
#         print(f"{dan} x {i} = {dan*i}")
#     print("=============================================") # dan은 변수의 이름


'''
2 x 1 = 2   3 x 1 = 3   4 x 1 = 4
2 x 2 = 4   3 x 2 = 6   4 x 2 = 8
2 x 3 = 6   3 x 3 = 9   4 x 3 = 12
'''
# 이렇게 출력하려면? 고정된 값과 아닌 값을 생각해보기

# for dan in range(2,5) :    
#     for i in range(1,5) :  
#         print(f"{dan} x {i} = {dan*i}", end="\t")    
#     print("\n=============================================")    #\n 은 enter 기능, \t tab만큼 띄어쓰기

# 2 x 1 = 2       2 x 2 = 4       2 x 3 = 6       2 x 4 = 8
# 3 x 1 = 3       3 x 2 = 6       3 x 3 = 9       3 x 4 = 12
# 4 x 1 = 4       4 x 2 = 8       4 x 3 = 12      4 x 4 = 16
# 이렇게 출력됨


for dan in range(1,10) :    
    for i in range(2,10) :  
        print(f"{i} x {dan} = {i*dan}", end="\t")    
    print("\n") 