# enumerate: 횟수를 출력해주는 함수

# names = ['홍길동', '이순신', '강감찬']

# id = 1  # 5,8번 추가하면 번호 매기고 이름 출력
# for name in names:
#     print(f'{id}.{name}')
#     id +=1

# for id,name in enumerate(names,start=1):
#     print(id, name)


# split

test_str = "epoch=1, loss=0.45, acc=88.5"
print(test_str.split(','))
# ['epoch=1', ' loss=0.45', ' acc=88.5'] 이렇게 출력됨

test_str = ["epoch=1, loss=0.45, acc=88.5"]
for line in test_str:
    result = dict(item.split("=") for item in line.split(","))
    print(result)

