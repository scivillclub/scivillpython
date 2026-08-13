# ==============================
# 1. 출력과 기본 연산
# ==============================

# HELLO WORLD
print ("Hello, World!")
##print 명령어를 통해 출력할 수 있다

# 사칙연산을 이용한 연산
print (3 * 4)
print (5 + 7)
print (10 - 3)
print (15 / 3)
##사칙연산을 이용하여 값을 계산할 수 있다

# 몫과 나머지 구하기
a = 350
b = 30

print(a // b)       # 몫: 11
print(a % b)        # 나머지: 20
print(divmod(a, b)) # (11, 20)
##//, %, divmod()를 이용하여 몫과 나머지를 구할 수 있다.

# ==============================
# 2. 변수와 자료형
# ==============================

# 변수
c = 10
print(c)

c = 20
print(c)
##변수는 값을 저장해두는 이름이다. 값이 변할 수 있다.

# 문자열 세기
text = "수리 수리 마하수리, 열려라 참깨"
print(text.count('수리'))
##print(text.count('수리')) 는 문자열 안에 특정 문자열이 몇 번 나오는지 출력된다.

# 문자열 길이, 위치찾기
text = "수리수리 마하수리, 열려라 참깨"
print(len(text))
##len(text) 는 문자열 안에 글자 수를 출력한다.

print(text.find("마"))
print(text.find("수"))
## find() 는 문자열 안에 특정 문자열이 몇 번째 위치에 있는지 출력한다. 맨 처음은 0부터 시작한다.

# text.replace()를 이용한 문자열 바꾸기
text = '오늘 오후 &시 ^분에 $에서 만나자'\

text = text.replace('&','3')
text = text.replace('^','15')
text = text.replace('$','우리집')

print(text)
## text.replace() 는 문자열 안에 특정 문자열을 다른 문자열로 바꿀 수 있다.

# text.split()를 이용한 문자열 나누기
text = "사과 바나나 포도 딸기"

words = text.split()

print(words)
## text.split() 는 문자열 안에 특정 문자열을 기준으로 나눌 수 있다. 기본값은 공백이다.

# 자료형변환 (str, int, float)
age = 17
height = 175.5

print(str(age))
print(int(height))
print(float(age))
## 자료형변환을 통해 서로 다른 자료형으로 값을 변환할 수 있다.
## str()은 값을 문자열로 변환한다.
## int()는 값을 정수형으로 변환한다.
## float()는 값을 실수형으로 변환한다.

# type()를 이용한 자료형 확인
a = 10
b = 3

print(type(a + b))
print(type(a * b))
print(type(a / b))
## type()은 변수나 값의 자료형을 확인할 때 사용한다.

# input()를 이용한 사용자 입력
print('회원가입을 환영합니다.')
name = input("성함을 입력해 주세요")
age = input("나이를 입력해 주세요")

print(name + "님 안녕하세요")
print(age + '살 이시군요!')
print('회원가입이 완료되었습니다')
## input()은 사용자로부터 값을 입력받을 때 사용한다.

# divmod() 응용
a = int(input("전체 학교 학생수"))
b = int(input("한 교실에 들어갈 학생수"))
c,d = divmod(a,b)
print(c ,'학급 개수')
print(d ,'남는 학생수')
## divmod(a, b)는 a를 b로 나눈 몫과 나머지를 동시에 반환한다.
## 반환되는 값의 순서는 (몫, 나머지)이다.

# 환율계산기
print("미국 달러 환율")
D = int(input('원화를 입력해 주세요'))
a = D * 0.00072
print(a)

# 피자이야기
print('피자 이야기')
a = int(input('피자 판 개수'))
b = int(input('사람 수'))
c = a*12
x,y = divmod(c,b)
print ('한사람당 먹을수 있는 피자 조각 수는', x ,'개')
print ('남는 조각 수', y ,'개')
print ('1인당 내야 하는 가격 계산')
d = int(input('판당 피자 가격'))
# a-판 , b-사람 , c-전체 조각 , d-판당 가격
e = a*d
# e-전체 가격
q,w = divmod(e,b)
print ('인당 내야할 가격:' , q)
print ('남는 돈:' , w)

#1강 과제
## 1. 변수 이용하여 계산기 만들기
## 2. 일본 앤화 환율 만들기