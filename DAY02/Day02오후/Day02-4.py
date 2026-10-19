# 리스트 컴프리핸션
result = []
#1-1
list_1 = [1,2,3,4,5]

for i in list_1:
    if i % 2 == 0:
        result.append(i)

result = [ i for i in list_1 if i%2 == 0 ] # 6,7,8 번을 대신할 수 있다 

print(result)

#1-2
for i in list_1:
     result.append(i*2)

result = [[i*2 for i in list_1]]

print(result)

#2
list_1 = ['1','2','3','4','5'] # '' 안에 잇으면 문자열인데 숫자열로 바꾸고 싶다면

result = [ int(i) for i in list_1]

print(result)

#3 
menu = ['아메리카노', '라떼', '초코']
ice_menu = ["아이스" +i for i in menu]

print(ice_menu)

#3-1 메뉴에 있는 것들의 길이
len_menu = [len(i) for i in menu] 
print(len_menu)

#3-2 조건에 맞는 애들만 출력
len_menu = [len(i) for i in menu if len(i)%2 == 0] 
print(len_menu)

#4
ages = [20,15,60,25,30,45,5]
print([ i for i  in ages if i >=20 ])
print(['성인' if i>=20 else '미성년' for i in ages])


if "":
    print("abc")  # 유효하지 않아서 print의 색이 달라졌다.

# set의 역할
print(set([1,2,3,4,5,6,7,8,1,2,3,4,5]))
# -> set은 중복을 다 날린다. 

bad_words = ['바보', '멍충이', '멍텅구리', '멍충이']
words = sorted(set(word for word in bad_words if word)), key=len, reverse=True
print(words)

# join의 역할: 합친다. ,를 빼고 원하는 기호(|)로 합친다
# print("|".join

