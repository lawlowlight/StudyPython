# 파일 입출력 1

# mode = w 새로생성쓰기 a 추가쓰기 r 읽기
f = open(file='C:/STUDY/StudyPython/temp.txt', mode='a' , encoding='utf-8')

f.write('안녕하세요.\n')
f.write('저는 김지환입니다.\n')
f.write('한국사람이죠.\n')

f.close() ## 필수
print('파일 생성완료')
