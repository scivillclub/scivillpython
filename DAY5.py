# ==============================
# 8. 함수
# ==============================


# 함수 기초
def hello():
    print("안녕하세요")

hello()
## 함수(function)는 특정 작업을 하나로 묶어 필요할 때 실행할 수 있도록 만든 코드이다.
## def를 이용하여 함수를 정의한다.
## hello()와 같이 함수의 이름 뒤에 소괄호를 붙이면 함수를 실행할 수 있다.
## 함수를 실행하는 것을 함수 호출이라고 한다.


# 함수 여러 번 호출하기
def welcome():
    print("방문을 환영합니다.")

welcome()
welcome()
welcome()
## welcome은 사용자가 직접 정한 함수의 이름이다.
## 함수 이름은 함수가 하는 일을 알기 쉽게 정하는 것이 좋다.
## 한 번 정의한 함수는 필요한 만큼 여러 번 호출할 수 있다.


# 매개변수가 있는 함수
def hello_name(name):
    print(name, "님 안녕하세요.")

hello_name("민수")
hello_name("철수")
## 매개변수란 함수가 값을 전달받기 위해 사용하는 변수이다.
## name은 함수가 값을 전달받기 위해 사용하는 매개변수(parameter)이다.
## "민수", "철수"처럼 함수를 호출할 때 전달하는 실제 값을 인자(argument)라고 한다.


# 여러 개의 매개변수
def introduce(name, age):
    print("이름:", name)
    print("나이:", age)

introduce("민수", 17)
introduce("영희", 16)
## 함수에는 여러 개의 매개변수를 사용할 수 있다.
## 전달하는 인자의 순서는 매개변수의 순서와 맞아야 한다.


# 함수를 이용한 계산
def add(a, b):
    print(a + b)

add(10, 20)
add(5, 7)
## 함수에 전달받은 값을 계산에 사용할 수 있다.


# return 기초
def add_return(a, b):
    return a + b

result = add_return(10, 20)

print(result)
## return은 함수에서 만든 결과를 함수 밖으로 돌려준다.
## return으로 돌려받은 값은 변수에 저장할 수 있다.


# print()와 return의 차이
def print_add(a, b):
    print(a + b)

def return_add(a, b):
    return a + b

print_add(10, 20)

result = return_add(10, 20)
print(result)
print(result * 2)
## print()는 결과를 화면에 출력한다.
## return은 결과를 함수 밖으로 돌려준다.
## return으로 돌려받은 값은 다른 계산에 다시 사용할 수 있다.


# return 값 다시 사용하기
def multiply(a, b):
    return a * b
result = multiply(5, 4)

print(result)
print(result + 10)
print(result * 2)
## 함수가 return한 값은 변수에 저장하거나 다른 연산에 사용할 수 있다.


# 조건문이 들어간 함수
def check_number(number):
    if number % 2 == 0:
        print("짝수입니다.")
    else:
        print("홀수입니다.")

check_number(10)
check_number(7)
## 함수 안에서도 if, elif, else와 같은 조건문을 사용할 수 있다.


# 조건에 따라 다른 값 return하기
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

result = grade(85)
print(result)
## 조건에 따라 서로 다른 값을 return할 수 있다.


# 반복문이 들어간 함수
def count_number(end):
    for i in range(1, end + 1):
        print(i)

count_number(5)
## 함수 안에서도 for문이나 while문을 사용할 수 있다.


# 함수를 여러 번 이용하기
def gugudan(dan):
    for i in range(1, 10):
        print(dan, "X", i, "=", dan * i)

gugudan(2)
gugudan(3)
## 하나의 함수를 여러 값으로 호출하면 같은 기능을 반복해서 사용할 수 있다.


# 리스트를 함수에 전달하기
def show_foods(foods):
    for food in foods:
        print(food)

food_list = ["라면", "김밥", "떡볶이"]
show_foods(food_list)
## 리스트도 함수의 인자로 전달할 수 있다.
## 함수 안에서 전달받은 리스트의 값을 사용할 수 있다.


# 리스트의 값을 계산하는 함수
def total_score(score_list):
    total = 0

    for score in score_list:
        total = total + score

    return total

exam_scores = [80, 90, 100]
print(total_score(exam_scores))
## 반복문을 이용하여 리스트의 값을 처리한 뒤 결과를 return할 수 있다.


# 리스트의 평균을 구하는 함수
def average(score_list):
    total = 0

    for score in score_list:
        total = total + score

    return total / len(score_list)

exam_scores = [80, 90, 100]
print(average(exam_scores))
## 함수에서는 리스트, 반복문, 연산을 함께 사용할 수 있다.


# 지역 변수
def test():
    message = "함수 안에서 만든 변수입니다."
    print(message)

test()
## 함수 안에서 만들어진 변수는 기본적으로 함수 안에서만 사용할 수 있다.
## 이러한 변수를 지역 변수(local variable)라고 한다.


# 함수 밖의 변수
name = "민수"

def show_name():
    print(name)

show_name()
## 함수 밖에서 만들어진 변수를 함수 안에서 사용할 수도 있다.
## 함수 밖에서 만들어진 변수를 전역 변수(global variable)라고 한다.


# 매개변수의 기본값
def greeting(name="손님"):
    print(name, "님 안녕하세요.")

greeting("민수")
greeting()
## 매개변수에 기본값을 지정할 수 있다.
## 인자를 전달하지 않으면 지정된 기본값이 사용된다.


# return을 이용한 계산기
def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "올바른 연산자를 입력해주세요."

print(calculator(10, 5, "+"))
print(calculator(10, 5, "*"))
## 함수 안에 여러 조건문을 넣어 하나의 기능으로 만들 수 있다.


# 함수와 input() 응용
def age_check(age):
    if age >= 19:
        return "성인입니다."
    else:
        return "미성년자입니다."

user_age = int(input("나이를 입력하세요: "))
print(age_check(user_age))
## input()으로 입력받은 값도 함수의 인자로 전달할 수 있다.


# 라면 가격 계산 함수
def 라면(a, b):
    if a == "신라면":
        print("선택하신 라면은 %s이며 주문 수량은 %d개 입니다." % (a, b))
        return 800 * b

    elif a == "진라면":
        print("선택하신 라면은 %s이며 주문 수량은 %d개 입니다." % (a, b))
        return 900 * b

    elif a == "육개장":
        print("선택하신 라면은 %s이며 주문 수량은 %d개 입니다." % (a, b))
        return 1000 * b

    elif a == "짜파게티":
        print("선택하신 라면은 %s이며 주문 수량은 %d개 입니다." % (a, b))
        return 1100 * b

    elif a == "삼양라면":
        print("선택하신 라면은 %s이며 주문 수량은 %d개 입니다." % (a, b))
        return 1200 * b

    else:
        print("그런 라면은 여기에 없습니다.")
        return 0


total = 0

while True:
    print("라면 식당입니다.")
    print(": 신라면 800원")
    print(": 진라면 900원")
    print(": 육개장 1000원")
    print(": 짜파게티 1100원")
    print(": 삼양라면 1200원")

    a = input("원하시는 라면을 골라주세요. (결제하려면 x): ")

    if a == "x":
        print("가격은", total, "원입니다.")

        c = input("결제하실 카드를 카드 리더기에 넣고 d 버튼을 클릭해주세요: ")

        if c == "d":
            print("주문이 완료되었습니다.")
        else:
            print("결제 실패")

        break

    b = int(input("주문 수량을 입력해주세요: "))

    total = total + 라면(a, b)

## def 라면(a, b)는 라면의 종류와 수량을 전달받는 함수이다.
## a와 b는 함수의 매개변수이다.
## 조건문을 이용하여 라면 종류에 따라 다른 가격을 계산한다.
## return을 이용하여 계산한 가격을 함수 밖으로 돌려준다.
## 돌려받은 가격을 total에 계속 더하여 전체 주문 금액을 계산한다.
## while True를 이용하여 결제하기 전까지 주문을 계속할 수 있다.