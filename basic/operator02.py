# 문자열 연산 

first = 'Hello'
second = 'World!'

print(first + second) # 문자연산 + (합치기)
print(first, second) # CONCAT 동일

print(first * 3) # 문자열연산 +, *밖에 없음

# 문자열 길이 내장함수
print(len('한글'))
print(len(first))

# 리스트 연산
print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])
# print(first[-6]) # IndexError!! 큰문제

## 현재 일시
currnt_date = '2022-05-02 14:23:45'
year = currnt_date[0:4]
month = currnt_date[5:7]
day = currnt_date[8:10]
hour = currnt_date[11:13]
min = currnt_date[14:16]
second = currnt_date[17:19]
print(year, '년', month, '월', day, '일' )
print(hour, '시' , min , '분' , second , '초')

print(year + '년', month + '월', day + '일' )
print(hour + '시' , min + '분' , second + '초')

print(currnt_date[-5:-3])

p = 'python'
print(p)
# p[0] = 'P' # Python TypeError
p2 = 'P' + p[1:]
print(p2)

print(p.upper())
print(p2.lower())

