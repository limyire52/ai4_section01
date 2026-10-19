list_a = [1,2,3,4,5,6,7,8,9,10]

for i in list_a:
    if i % 2 == 0:
        continue #continue가 있으면 다음문장 스킵
    print(i)

for i in list_a:
    if i == 5:
        continue 
    print(i)    # 5만 빼고 출력이 됨