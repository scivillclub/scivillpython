# ==============================
# 3. 비교 연산
# ==============================


# 대소비교 기초1
a = 10
print(a == 10)
## a == 10은 a가 10과 같은지 비교하는 것이다. 같으면 True, 다르면 False를 반환한다.


# 대소비교 기초2
age = 17

print(age >= 14)
print(age == 17)
print(age != 20)
## 대소비교 연산자는 두 값을 비교하여 참(True) 또는 거짓(False)을 반환한다.


# 대소비교 기초3
a = 10
b = 5

print(a > b)    # True
print(a >= b)   # True
print(a < b)    # False
print(a <= b)   # False
print(a == b)   # False
print(a != b)   # True
## 비교 연산자
## >   크다, 초과
## >=  크거나 같다, 이상
## <   작다, 미만
## <=  작거나 같다, 이하
## ==  같다
## !=  다르다


# ==============================
# 4. 조건문
# ==============================


# if문 기초
age = 17

if age >= 14:
    print("14세 이상입니다.")

if age < 14:
    print("14세 미만입니다.")
## if문은 조건이 참일 때만 실행되는 조건문이다.


# if문 홀수짝수구분하기
print('홀수 짝수 구분')
a = int(input('원하는 숫자'))
b = a%2

if b == 0:
   print('짝수')

if b == 1:
   print('홀수')
## a와 b를 변수로 지정한다.
## input()를 이용하여 원하는 숫자를 입력받아 홀수인지 짝수인지 구분할 수 있다.


# 논리 연산자 and
age = 17
height = 170

if age >= 14 and height >= 150:
    print("탑승할 수 있습니다.")
## and는 두 조건이 모두 참일 때 True가 된다.


# 논리 연산자 or
weekend = True
holiday = False

if weekend or holiday:
    print("오늘은 쉬는 날입니다.")
## or는 두 조건 중 하나 이상이 참일 때 True가 된다.


# 논리 연산자 not
is_member = False

if not is_member:
    print("회원가입이 필요합니다.")
## not은 조건의 참과 거짓을 반대로 바꾼다.


# if문을 이용한 계산기
print('계산기')
num1 = int(input('원하는 숫자'))
num2 = int(input('원하는 숫자'))
a = input('+,-,*,/중에 어떤 방식으로 계산할지 선택해주세요')

if a == '+' :
    b = num1 + num2
    print(b)

if a == '-' :
    b= num1 - num2
    print(b)

if a == '*' :
    b= num1 * num2
    print(b)

if a == '/' :
    b= num1 / num2
    print(b)
## if문을 이용하여 원하는 숫자를 입력받아 계산할 수 있다.


# if - else문 기초
user_id = input("아이디: ")
password = input("비밀번호: ")

if (user_id == "김코드") and (password == "0110"):
    print("방문을 환영합니다")
else:
    print("아이디와 패스워드를 확인해주세요")
## else문은 if문의 조건이 거짓일 때 실행되는 조건문이다.


# if - elif - else문 기초
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
## elif는 앞의 조건이 거짓일 때 새로운 조건을 "검사"한다.
## else는 앞의 모든 조건이 거짓일 때 실행된다.


# 계산기
print("계산기")

num1 = int(input("첫 번째 숫자: "))
num2 = int(input("두 번째 숫자: "))
a = input("+,-,*,/ 중 연산자를 선택하세요: ")

if a == '+':
    print(num1 + num2)
elif a == '-':
    print(num1 - num2)
elif a == '*':
    print(num1 * num2)
elif a == '/':
    print(num1 / num2)
else:
    print("올바른 연산자를 입력해주세요.")
## if - elif - else문을 이용하여 계산기를 개선할 수 있다.
## input()으로 입력받은 값은 문자열이므로 계산을 하려면 int()로 변환해야 한다.
## 연산자는 계산에 쓰이는 값이 아니므로 문자열 그대로 사용한다.
## a == '+'는 입력받은 값이 +인지 비교하는 것이다.
## elif는 앞의 조건이 거짓일 때만 검사하므로 조건 중 하나만 실행된다.
## else는 +,-,*,/ 가 아닌 값을 입력했을 때 실행된다.
