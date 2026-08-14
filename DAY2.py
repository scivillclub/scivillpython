# ==============================
# 3. 비교 연산
# ==============================

# 대소비교 기초1
a = 10      # 값을 저장한다.
a == 10     # 두 값이 같은지 비교한다.

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
## a와 b를 변수로 지정한다.

if b == 0:
   print('짝수')

if b == 1:
   print('홀수')
## input()를 이용하여 원하는 숫자를 입력받아 홀수인지 짝수인지 구분할 수 있다.

# 논리 연산자
age = 17
height = 170

if age >= 14 and height >= 150:
    print("탑승할 수 있습니다.")
## and는 두 조건이 모두 참일 때 True가 된다.
## or는 두 조건 중 하나 이상이 참일 때 True가 된다.
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

# if - elif - else문을 이용한 계산기
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

# ==============================
# 5. 반복문
# ==============================

# for문 기초1
for i in range(5):
    print(i)
## for문은 정해진 범위의 값을 하나씩 가져오며 반복한다.
## 0~4까지 출력된다.

# for문 기초2
for a in range(5):
    print(a)
##for i in range의 i는 변수 부분이다.

# range() 기초
for i in range(3, 8):
    print(i)
## range(3, 8)은 3부터 7까지의 값을 만든다. 
## 마지막 숫자 8은 포함되지 않는다.

# continue를 이용하여 특정 반복 건너뛰기
for i in range(1, 11):

    if i == 5:
        continue

    print(i)
## continue는 반복문에서 특정 조건을 만족할 때, 그 반복을 건너뛰고 다음 반복으로 넘어가게 한다.
## 이 경우 5만 건너뛴다.

# 총합
sum = 0

for i in range(1,101):
    sum=sum+i
    print(i, "일때 여기까지 더해진 수 총합 :" ,sum)

print('1부터 100까지의 합 : %d' %sum)
## for문을 이용하여 1부터 100까지의 합을 구할 수 있다.

# range() 간격 설정
for i in range(1, 10, 2):
    print(i)
## range(1, 10, 2)는 1부터 10 직전까지 2씩 증가한다.
## 1, 3, 5, 7, 9가 출력된다.

# range()를 이용한 역순 반복
for i in range(10, 0, -1):
    print(i)
## -1을 사용하면 숫자를 1씩 감소시키며 반복할 수 있다.
## 10부터 1까지 출력된다.

# 중첩 for문을 이용한 곱셈
for i in range(2, 4):
    for j in range(1, 10):
        print(i, "X", j, "=", i * j)
## for문 안에 또 다른 for문을 사용할 수 있다.
## 이를 중첩 반복문이라고 한다.

# input 응용
a = int(input('숫자를 입력하세요'))
b= int(input('숫자를 입력하세요'))
for i in range(a,b+1):
    if i%2==1 :
        print(i,end="")
## input()을 이용하여 원하는 숫자를 입력받아 쓸 수 있다.

# while True 기초와 break를 이용한 반복 종료
while True:
    password = input("비밀번호를 입력하세요: ")

    if password == "0110":
        print("로그인되었습니다.")
        break

## while True는 조건이 항상 참이기 때문에 계속 반복된다.
## break는 반복문을 즉시 종료한다.
## while True:
##   print("계속 반복됩니다.") -> 이 경우 "계속 반복됩니다." 가 무한히 출력된다."

# while문 반복 횟수 정하기
count = 1

while count <= 5:
    print(count, "번째 반복입니다.")
    count = count + 1
## while문은 조건이 참인 동안 반복한다.
## count = count + 1을 이용하여 count의 값을 1씩 증가시킨다.
## count가 6이 되면 count <= 5가 거짓이 되어 반복문이 종료된다.


# while문 숫자 감소시키기
count = 5

while count >= 1:
    print(count)
    count = count - 1

print("종료!")
## while문에서는 변수의 값을 증가시킬 수도 있고 감소시킬 수도 있다.
## 위 코드는 5부터 1까지 출력한 후 반복을 종료한다.


# while문 원하는 숫자가 입력될 때까지 반복
number = int(input("0을 입력하면 종료됩니다: "))

while number != 0:
    print("입력한 숫자:", number)
    number = int(input("0을 입력하면 종료됩니다: "))

print("프로그램이 종료되었습니다.")
## number가 0이 아닌 동안 계속 입력을 받는다.
## 0을 입력하면 while문의 조건이 거짓이 되어 반복이 종료된다.


# while문과 if문 응용
number = 1

while number <= 10:

    if number % 2 == 0:
        print(number, "짝수")

    number = number + 1
## while문과 if문을 함께 사용할 수 있다.
## 1부터 10까지 반복하면서 짝수인 숫자만 출력한다.

# while True
import random

ai = random.randint(1, 100)
turns = 0

while True:
    if turns == 7:
        print("게임 오버")
        print("정답은? :", ai)
        break

    Q = int(input("숫자를 입력해보세요: "))

    if ai < Q:
        turns = turns + 1
        print("더 낮습니다")

    elif ai > Q:
        turns = turns + 1
        print("더 높습니다")

    else:
        turns = turns + 1
        print("정답입니다")
        print("시도 횟수:", turns)
        break
## while문은 조건이 참인 동안 반복한다.
## while True는 조건이 항상 참이므로 무한 반복하며, 보통 break를 이용하여 종료한다.
## import random을 이용하여 랜덤한 숫자를 생성할 수 있다.

# 라면가게
def 라면(a, b):
    if a == "신라면":
        print("선택하신 라면은 %s이며 주문 수량은 %d개 입니다" % (a, b))
        return 800 * b

    elif a == "진라면":
        print("선택하신 라면은 %s이며 주문 수량은 %d개 입니다" % (a, b))
        return 900 * b

    elif a == "육개장":
        print("선택하신 라면은 %s이며 주문 수량은 %d개 입니다" % (a, b))
        return 1000 * b

    elif a == "짜파게티":
        print("선택하신 라면은 %s이며 주문 수량은 %d개 입니다" % (a, b))
        return 1100 * b

    elif a == "삼양라면":
        print("선택하신 라면은 %s이며 주문 수량은 %d개 입니다" % (a, b))
        return 1200 * b

    else:
        print("그런건 여기에 없습니다")
        return 0


total = 0

while True:
    print("라면 식당 입니다")
    print(":신라면 800원")
    print(":진라면 900원")
    print(":육개장 1000원")
    print(":짜파게티 1100원")
    print(":삼양라면 1200원")

    a = input("원하시는 라면을 골라주세요 (결제하려면 x): ")

    if a == "x":
        print("가격은", total, "원 입니다")

        c = input("결제하실 카드를 카드 리더기에 넣고 d 버튼을 클릭해주세요: ")

        if c == "d":
            print("주문이 완료되었습니다.")
        else:
            print("결제 실패")

        break

    b = int(input("주문 수량을 입력해주세요: "))

    total = total + 라면(a, b)
## def 라면(a, b)는 라면의 종류와 수량을 입력받아 가격을 계산하는 함수이다.

# 2강 과제
## 1. 조건문과 while문을 이용하여 업다운 숫자 맞히기 게임 만들기
## 2. 조건문과 for문을 이용하여 입력한 범위의 홀수, 짝수 구분 프로그램 만들기
## 3. 점수를 입력받아 A, B, C 등급을 출력하는 성적 판정 프로그램 만들기
## 4. 비밀번호가 맞을 때까지 반복해서 입력받는 로그인 프로그램 만들기
## 5. 구구단의 시작 단과 끝 단을 입력받아 해당 범위의 구구단 출력하기