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
## for문에서 a는 반복할 때마다 값을 하나씩 저장하는 변수이다.
## 변수 이름은 i, a 등 원하는 이름으로 정할 수 있다.


# range() 기초
for i in range(3, 8):
    print(i)
## range(3, 8)은 3부터 7까지의 값을 만들며, 마지막 숫자 8은 포함하지 않는다.


# continue를 이용하여 특정 반복 건너뛰기
for i in range(1, 11):

    if i == 5:
        continue

    print(i)
## continue는 반복문에서 특정 조건을 만족할 때, 그 반복을 건너뛰고 다음 반복으로 넘어가게 한다.
## 이 경우 5만 건너뛴다.


# 총합
total = 0
for i in range(1, 101):
    total = total + i

print('1부터 100까지의 합 : %d' % total)
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
## print()의 end를 이용하면 출력 후 줄바꿈 대신 원하는 문자를 넣을 수 있다.


# while True 기초와 break를 이용한 반복 종료
while True:
    password = input("비밀번호를 입력하세요: ")

    if password == "0110":
        print("로그인되었습니다.")
        break
## while True는 조건이 항상 참이기 때문에 계속 반복된다.
## break는 반복문을 즉시 종료한다.
## while True:
# print("계속 반복됩니다.") -> 이 경우 "계속 반복됩니다." 가 무한히 출력된다.


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
## import random으로 random 모듈을 불러올 수 있다.
## random.randint(1, 100)은 1부터 100 사이의 임의의 정수를 만든다.


# 편의점 장바구니
total = 0
while True:
    print("편의점입니다.")
    print(": 삼각김밥 1500원")
    print(": 컵라면 1800원")
    print(": 음료수 2000원")

    item = input("담을 상품을 입력하세요. 계산하려면 x: ")

    if item == "x":
        break

    if item == "삼각김밥":
        price = 1500
    elif item == "컵라면":
        price = 1800
    elif item == "음료수":
        price = 2000
    else:
        print("그런 상품은 없습니다.")
        continue

    count = int(input("수량을 입력하세요: "))
    total = total + price * count

    print(item, count, "개 담았습니다. 현재 합계:", total, "원")

print("최종 결제 금액은", total, "원입니다.")
## while True를 이용하여 x를 입력할 때까지 상품을 계속 담을 수 있다.
## if - elif - else를 이용하여 상품에 따라 다른 가격을 지정한다.
## continue를 이용하여 잘못된 입력일 때 다음 반복으로 넘어간다.
## total = total + price * count를 이용하여 금액을 계속 누적한다.
