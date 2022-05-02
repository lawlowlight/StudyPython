# for문 학습
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = 0

for x in range(1, 101):
    result = result + x

print('배열의 합 =', result)

arr2 = ('me', 'my', 'friend', 'jane')

for item in arr2:
    print(f'{item * 2}') # print(f'{item:>10}')

## 1~10까지 수에서 짝수로 구분하기
for num in range(1, 11):
    if (num % 2) == 0:
        print(f'{num}은 짝수입니다.')   
    else: 
        print(f'{num}은 홀수입니다.')   

# for문 내에서 사용하는 continue, break
values = [1,3,5,7,9,11,13,15,17,19]

num = 0
for item in values:
    num += 1 # num = num + 1
    if (num % 2) == 0:
        # break # 반복물 탈출
        continue # if 조건만 패스 다음값 진행
    else:
        print(f'{num}번의 수는 {item}입니다.')


