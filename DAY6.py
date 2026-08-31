# ==============================
# 9. 파일 입출력
# ==============================


# 파일 쓰기
file = open("hello.txt", "w", encoding="utf-8")

file.write("안녕하세요.")
file.close()
## 파일 이름만 적으면 Python이 현재 작업 중인 폴더에 파일을 만든다.
## open()을 이용하여 파일을 열 수 있다.
## "w"는 파일에 내용을 새로 작성하는 쓰기 모드(write)이다.
## "w" 모드에서 파일이 없으면 새로 만들고, 이미 있으면 기존 내용을 지우고 새로 작성한다.
## write()를 이용하여 파일에 내용을 저장할 수 있다.
## close()를 이용하여 사용이 끝난 파일을 닫는다.
## encoding="utf-8"은 파일을 UTF-8 방식으로 저장하고 읽도록 지정한다.


# 파일 접근 방식
file = open("mode.txt", "w", encoding="utf-8")
file.write("첫 번째 내용\n")
file.close()

file = open("mode.txt", "a", encoding="utf-8")
file.write("뒤에 덧붙인 내용\n")
file.close()

file = open("mode.txt", "r", encoding="utf-8")
print(file.read())
file.close()
## 파일 객체 = open("파일 경로", "파일 접근 방식") 의 형태로 파일을 연다.
## "w"는 쓰기 모드로, 파일이 없으면 만들고 있으면 기존 내용을 지우고 새로 쓴다.
## "a"는 추가 모드로, 기존 내용을 그대로 두고 뒤에 이어서 쓴다.
## "r"은 읽기 모드로, 파일의 내용을 읽어 온다. 파일이 없으면 오류가 발생한다.
## 파일을 다 쓰고 나면 close()로 닫아야 내용이 제대로 저장된다.


# 여러 줄을 파일에 저장하기
file = open("students.txt", "w", encoding="utf-8")

file.write("민수\n")
file.write("영희\n")
file.write("철수\n")

file.close()
## \n은 줄을 바꾸는 줄바꿈 문자이다.
## write()를 여러 번 사용하여 여러 내용을 파일에 저장할 수 있다.


# 여러 줄 한 번에 쓰기 - writelines()
file = open("members.txt", "w", encoding="utf-8")

members = ["민수\n", "영희\n", "철수\n"]
file.writelines(members)

file.close()
## writelines()는 리스트에 담긴 여러 줄을 한 번에 파일에 쓴다.
## write()를 여러 번 부르는 대신 리스트로 한 번에 저장할 수 있다.
## writelines()는 줄바꿈을 자동으로 넣어 주지 않으므로 값마다 \n을 직접 넣어야 한다.


# 파일 읽기
file = open("hello.txt", "r", encoding="utf-8")
text = file.read()
print(text)
file.close()
## "r"은 파일의 내용을 읽는 읽기 모드(read)이다.
## read()는 파일의 전체 내용을 읽어온다.


# 파일 한 줄씩 읽기
file = open("students.txt", "r", encoding="utf-8")

print(file.readline())
print(file.readline())
print(file.readline())

file.close()
## readline()은 파일의 내용을 한 줄씩 읽어온다.
## readline()으로 읽은 값에는 줄바꿈 문자인 \n이 포함되어 있다.
## 그래서 print()로 출력하면 줄이 한 번 더 바뀐다.


# 파일의 모든 줄을 리스트로 읽기
file = open("students.txt", "r", encoding="utf-8")
students = file.readlines()
print(students)
file.close()
## readlines()는 파일의 모든 줄을 읽어 리스트로 반환한다.
## 리스트로 읽어온 값에도 줄바꿈 문자인 \n이 그대로 포함되어 있다.


# 파일에 내용 추가하기
file = open("students.txt", "a", encoding="utf-8")
file.write("지민\n")
file.close()
## "a"는 기존 내용을 지우지 않고 파일의 마지막에 새로운 내용을 추가하는 모드(append)이다.


# with open() 사용하기
with open("message.txt", "w", encoding="utf-8") as file:
    file.write("Python 파일 입출력을 공부하고 있습니다.")
## with open()을 이용하면 파일 사용이 끝났을 때 자동으로 파일을 닫아준다.
## 따라서 close()를 따로 작성하지 않아도 된다.


# with open()으로 파일 읽기
with open("message.txt", "r", encoding="utf-8") as file:
    message = file.read()

print(message)
## with open()은 파일을 읽거나 쓸 때 자주 사용하는 방식이다.


# ==============================
# 10. CSV와 데이터 처리
# ==============================


# CSV 파일 만들기
import csv

with open("scores.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["이름", "국어", "영어", "수학"])
    writer.writerow(["민수", 90, 80, 85])
    writer.writerow(["영희", 95, 90, 100])
    writer.writerow(["철수", 70, 80, 75])
## CSV는 쉼표 등을 이용하여 여러 데이터를 표 형태로 저장하는 파일 형식이다.
## import csv를 이용하여 Python의 csv 모듈을 사용할 수 있다.
## writerow()는 CSV 파일에 한 행의 데이터를 저장한다.


# CSV 파일 읽기
with open("scores.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
## csv.reader()를 이용하여 CSV 파일의 데이터를 읽을 수 있다.
## for문을 이용하면 CSV의 각 행을 하나씩 가져올 수 있다.


# CSV 첫 번째 줄 구분하기
with open("scores.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    header = next(reader)

    print("항목:", header)

    for row in reader:
        print("학생 정보:", row)
## next()는 현재 위치에서 다음 값을 하나 가져온다.
## 이 예제에서는 첫 번째 줄을 항목 이름으로 따로 가져온다.


# CSV 점수 계산
with open("scores.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        name = row[0]
        korean = int(row[1])
        english = int(row[2])
        math = int(row[3])

        total = korean + english + math
        average = total / 3

        print(name, "총점:", total, "평균:", average)
## CSV에서 읽은 값은 문자열로 읽어오므로 계산하려면 int()로 변환해야 한다.
## 리스트의 인덱스를 이용하여 각 열의 값을 가져올 수 있다.
## 파일, 리스트, 반복문을 함께 사용하여 데이터를 처리할 수 있다.


# CSV에서 가장 높은 평균 찾기
best_name = ""
best_average = 0

with open("scores.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        name = row[0]

        korean = int(row[1])
        english = int(row[2])
        math = int(row[3])

        average = (korean + english + math) / 3

        if average > best_average:
            best_average = average
            best_name = name

print("가장 높은 평균:", best_name, best_average)
## 반복문과 조건문을 이용하여 CSV 데이터에서 가장 높은 평균을 찾을 수 있다.


# ==============================
# 11. 예외 처리
# ==============================


# 예외 발생
# number = int(input("숫자를 입력하세요: "))
## 숫자가 아닌 문자를 입력하면 ValueError가 발생한다.


# try - except 기초
try:
    number = int(input("숫자를 입력하세요: "))
    print("입력한 숫자:", number)

except ValueError:
    print("숫자만 입력해주세요.")
## try 안의 코드를 실행하다가 except에 지정된 예외가 발생하면 해당 except의 코드가 실행된다.
## ValueError는 값의 형태가 올바르지 않을 때 발생할 수 있는 오류이다.


# 0으로 나누기 예외 처리
try:
    a = int(input("첫 번째 숫자: "))
    b = int(input("두 번째 숫자: "))

    print(a / b)

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
## ZeroDivisionError는 숫자를 0으로 나누려고 할 때 발생한다.
## 이 예제에서는 ZeroDivisionError만 처리한다.


# 여러 예외 처리하기
try:
    a = int(input("첫 번째 숫자: "))
    b = int(input("두 번째 숫자: "))

    print(a / b)

except ValueError:
    print("숫자를 입력해주세요.")

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
## 하나의 try문에 여러 개의 except를 사용할 수 있다.
## 발생한 오류의 종류에 따라 서로 다른 처리를 할 수 있다.


# 존재하지 않는 파일 처리
try:
    with open("없는파일.txt", "r", encoding="utf-8") as file:
        print(file.read())

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
## FileNotFoundError는 존재하지 않는 파일을 읽기 모드로 열려고 할 때 발생한다.
## 예외 처리를 이용하면 지정한 예외가 발생했을 때 프로그램이 바로 종료되는 것을 막을 수 있다.


# 성적관리
students = []

with open("class_scores.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["이름", "점수"])

    for i in range(3):
        name = input("학생 이름을 입력하세요: ")
        score = int(input("점수를 입력하세요: "))

        writer.writerow([name, score])

with open("class_scores.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        name = row[0]
        score = int(row[1])

        students.append([name, score])

total = 0

for student in students:
    print("이름:", student[0], "점수:", student[1])

    total = total + student[1]

average = total / len(students)
print("전체 평균:", average)
## 학생의 이름과 점수를 입력받아 CSV 파일에 저장한다.
## 저장한 CSV 파일을 다시 읽어 리스트에 저장한다.
## 반복문을 이용하여 모든 학생의 점수를 더하고 평균을 계산한다.
## DAY1의 입력과 변수, DAY3의 반복문, DAY4의 리스트, DAY6의 파일 처리를 함께 이용한 예제이다.


# ==============================
# 12. 클래스
# ==============================


# 클래스 만들기
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
## 클래스는 서로 관련 있는 값과 기능을 하나로 묶어 두는 틀이다.
## class 클래스이름: 의 형태로 만들며, 클래스 이름은 보통 대문자로 시작한다.
## __init__()은 객체를 만들 때 자동으로 실행되는 함수이다.
## self는 만들어진 객체 자신을 가리키며, 첫 번째 매개변수로 항상 적는다.
## self.name = name 은 객체 안에 name이라는 값을 저장한다는 뜻이다.


# 객체 만들기
student1 = Student("민수", 90)

print(student1.name)
print(student1.score)
## 클래스이름(값) 형태로 객체를 만든다.
## 객체 안에 저장된 값은 객체이름.값이름 으로 꺼내 쓴다.
## 클래스는 틀이고, 객체는 그 틀로 실제로 만들어 낸 것이다.


# 메서드 만들기
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def introduce(self):
        print("이름:", self.name, "점수:", self.score)

student1 = Student("민수", 90)
student1.introduce()
## 클래스 안에 만든 함수를 메서드라고 한다.
## 메서드도 첫 번째 매개변수로 self를 적는다.
## 메서드 안에서는 self.값이름 으로 객체에 저장된 값을 사용할 수 있다.
## 객체이름.메서드이름() 형태로 메서드를 부른다.


# 객체 여러 개 만들기
students = [Student("민수", 90), Student("영희", 85), Student("철수", 78)]

total = 0

for student in students:
    student.introduce()

    total = total + student.score

print("평균:", total / len(students))
## 같은 클래스로 서로 다른 객체를 얼마든지 만들 수 있다.
## 각 객체는 자기만의 값을 따로 가지므로 서로 영향을 주지 않는다.
## 객체를 리스트에 담으면 반복문으로 하나씩 다룰 수 있다.
## DAY4의 리스트, DAY5의 함수를 클래스와 함께 이용한 예제이다.


# ==============================
# 13. 교과서 예제
# ==============================


# 이벤트 참여 명단
print('우리 가게를 이용해 주셔서 감사합니다. 이벤트에 참여해 주세요!')
name = input('성명을 입력해 주세요.>> ')
number = input('전화번호를 입력해 주세요.>> ')
mail = input('메일 주소를 입력해 주세요.>> ')
print('참여해 주셔서 감사합니다. 안녕히 가세요.')

file = open('event.txt', 'a', encoding='UTF-8')
file.write('성명: ' + name + '\t 전화번호: ' + number + '\t 메일 주소: ' + mail + '\n')
file.close()

event = open('event.txt', 'r', encoding='UTF-8')
print('<현재까지 참여 명단>')
print(event.read())
event.close()
## 참여자에게 이름과 전화번호, 메일 주소를 입력받아 event.txt 파일에 이어서 저장한다.
## 파일 객체 file은 "a" 모드로 열었기 때문에 앞서 참여한 사람의 기록이 지워지지 않는다.
## '\t'는 탭 문자로, 항목 사이를 띄워 보기 좋게 만든다.
## 저장이 끝나면 같은 파일을 "r" 모드로 다시 열어 지금까지의 참여 명단을 모두 출력한다.
## 하나의 파일을 쓰기와 읽기 두 가지 방식으로 다루는 예제이다.


# 카페 주문 프로그램
# cafemenu.csv 파일을 읽고 출력하기
menufile = open('cafemenu.csv', 'r', encoding = 'UTF-8')   # 메뉴 파일 열기
print('메뉴 목록입니다. \n', menufile.read())                 # 파일 읽기
menufile.close()                                           # 파일 닫기
# 음료 주문 받고 receipt.txt 파일에 주문 내역 저장하기
order = input('주문하실 음료를 입력해 주세요.')
quantity = input('몇 잔 주문하시겠습니까?')
print(order, quantity, '잔 주문 받았습니다.')
file = open('receipt.txt', 'w', encoding = 'UTF-8')        # 주문 내역 파일 열기
file.write('주문 내역\n음료:' + order + '\t수량:' + quantity)  # 파일 쓰기
file.close()                                               # 파일 닫기
## cafemenu.csv에 저장된 메뉴를 읽어서 손님에게 보여 준다.
## read()는 파일 전체를 한 번에 읽어 오므로 메뉴 목록이 그대로 출력된다.
## input()으로 주문할 음료와 잔 수를 입력받는다.
## receipt.txt를 "w" 모드로 열어 주문 내역을 새로 저장한다.
## '\n'은 줄바꿈, '\t'는 탭 문자로 영수증을 보기 좋게 만든다.
## 파일을 읽는 일과 쓰는 일을 한 프로그램에서 함께 다루는 예제이다.


# 약수 구하기
num = int(input('정수를 입력하세요.: '))
if num <= 0:
    print('잘못된 입력입니다.')
else:
    print(num, '의 약수: ', end = '')
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end = ' ')
## range(1, num + 1)은 1부터 num까지의 숫자를 만든다.
## num % i == 0 이면 i로 나누어떨어지므로 num의 약수이다.
## print()에 end = ' '를 주면 줄을 바꾸지 않고 옆으로 이어서 출력한다.
## 0 이하의 수를 입력하면 약수를 구하지 않고 안내만 출력한다.


# 알파벳 개수 찾기
string = 'Change has a considerable psychological impact on the human mind. To the fearful it is threatening because it means that things may get worse. To the hopeful it is encouraging because things may get better. To the confident it is inspiring because the challenge exists to make things better. - King Whitney Jr. -'
alphabet = input('검색할 알파벳을 입력해 주세요. ')
count = 0
for char in string:
    if char == alphabet:
        count = count + 1
print(alphabet, '의 개수:', count, '개')
## 문자열도 for문으로 글자를 하나씩 꺼내 올 수 있다.
## 꺼낸 글자가 찾는 알파벳과 같으면 count를 1씩 늘린다.
## 대문자와 소문자는 서로 다른 문자로 센다.


# 2차원 리스트와 중첩 반복문 - 코드 1
list_population = [['ROK', 51.6],
                   ['JPN', 123.3],
                   ['CHN', 1425.7],
                   ['TWN', 23.4]]

count1 = 0
count2 = 0
for row in list_population:
    count1 = count1 + 1
for num in row :
    print(num, end = " ")
    count2 = count2 + 1
print()

print('첫 번째 반복문 실행 횟수:', count1 )
print('두 번째 반복문 실행 횟수:', count2 )
## 두 번째 for문이 첫 번째 for문 바깥에 있다.
## 그래서 첫 번째 반복이 모두 끝난 뒤 마지막 row 하나만 출력된다.
## count1은 4가 되지만 count2는 2에 그친다.


# 2차원 리스트와 중첩 반복문 - 코드 2
list_population = [['ROK', 51.6],
                   ['JPN', 123.3],
                   ['CHN', 1425.7],
                   ['TWN', 23.4]]

count1 = 0
count2 = 0
for row in list_population:
    count1 = count1 + 1
    for num in row :
        print(num, end = " ")
        count2 = count2 + 1
    print()

print('첫 번째 반복문 실행 횟수:', count1 )
print('두 번째 반복문 실행 횟수:', count2 )
## 두 번째 for문이 첫 번째 for문 안에 들어가 있다. 이것을 중첩 제어 구조라고 한다.
## 바깥 반복이 한 번 돌 때마다 안쪽 반복이 처음부터 다시 돈다.
## 그래서 모든 나라가 출력되고 count2는 8이 된다.
## 들여쓰기 한 칸 차이로 결과가 완전히 달라지므로 주의해야 한다.


# 키오스크 매출 계산
name = ['초코칩', '감자칩', '젤리', '이온 음료', '주스', '생수', '우유']
prices = [1200, 2000, 900, 1400, 1500, 600, 700]
quantities = [10, 7, 20, 12, 16, 11, 6]
product_sales = []
total_sales = 0
for i in range(len(name)):
    sales = prices[i] * quantities[i]
    product_sales.append(sales)
print('상품별 매출은 다음과 같습니다.', product_sales, sep = '\n')
max_sales = max(product_sales)
max_index = product_sales.index(max_sales)
max_product = name[max_index]
print('최대 매출을 낸 상품은', max_product, '입니다.')
for num in product_sales:
    total_sales = total_sales + num
print('총매출은', total_sales, '원입니다.')
## max()는 리스트에서 가장 큰 값을 돌려준다.
## index()로 그 값이 몇 번째에 있는지 찾으면 상품명도 알 수 있다.
## print()에 sep = '\n'을 주면 값 사이를 줄바꿈으로 띄운다.
## 교과서에서 빈칸으로 둔 부분(반복 범위, 매출 계산, 최댓값 찾기)을 채워 넣은 코드이다.


# 상품과 고객 클래스
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self):
        self.history = []
        self.total = 0

    def buy(self, item):
        self.history.append(item)
        self.total += item.price

milk = Item('우유', 1500)
bread = Item('빵', 3000)

person1 = Customer()
person1.buy(milk)
person1.buy(bread)

for item in person1.history:
    print(item.name, item.price, '원')
print('구매 금액 합계:', person1.total, '원')
## Item은 상품명과 가격을 담는 클래스이다.
## Customer는 구매 이력(history)과 구매 금액(total)을 가진다.
## buy()는 구매한 상품을 이력에 추가하고 금액을 더하는 메서드이다.
## self.total += item.price 는 self.total = self.total + item.price 와 같다.
## 클래스 두 개가 서로 어울려 하나의 프로그램이 되는 예제이다.


# 영양 관리 앱 (읽기용 예제)
# 이 예제는 실행하지 말고 구조만 읽어 보세요. 아래 설명에 이유가 있습니다.
import csv
import tabulate

class Food:
    def __init__(self, name = None, serving = None, nutri = []):
        self.name = name
        self.serving = serving
        self.nutri = nutri

class User:
    def __init__(self):
        self.eaten_food = []
        self.nutri = []

    def save_food(self, data):
        self.eaten_food = data

class App:
    def __init__(self, food_data):
        self.nutri_name = []
        self.food_list = []
        self.nutri_name = food_data[0][2:]
        for i in range(1, len(food_data)):
            self.food_list.append(Food(food_data[i][0], food_data[i][1], food_data[i][2:]))

    def open_data(src):
        file = open(src, 'r', encoding = 'utf-8')
        result = list(csv.reader(file))
        return result

    def find_food(self, food_name):
        result = None
        for i in self.food_list:
            if food_name == i.name:
                result = i
                break
        return result

    def calc_food(self, user):
        for i in range(len(user.eaten_food)):
            food = self.find_food(user.eaten_food[i][0])
            if food == None:
                print(user.eaten_food[i][0], "음식 정보가 없습니다.")
                continue
            rate = float(user.eaten_food[i][1]) / float(food.serving)
            for j in range(len(food.nutri)):
                if len(user.nutri) < len(food.nutri):
                    user.nutri.append(float(food.nutri[j]) * rate)
                else:
                    user.nutri[j] += float(food.nutri[j]) * rate

    def show_result(user, avg):
        result = []
        for i in range(len(avg)):
            need_nutri = float(avg[i][1]) - user.nutri[i]
            if need_nutri < 0:
                need_nutri = 0
            result.append([avg[i][0], avg[i][1], round(user.nutri[i]), round(need_nutri)])
        headers = ['영양 성분명', '평균 영양소', '섭취한 영양소', '부족한 영양소']
        df = tabulate.tabulate(result, headers)
        print(df)

food_data = App.open_data('food.csv')
avg = App.open_data('average.csv')[1:]
app = App(food_data)
user1 = User()
user1.save_food(App.open_data('eatenfood.csv'))
app.calc_food(user1)
App.show_result(user1, avg)
## 이 예제는 SCIVILL python IDE 에서 실행되지 않습니다. 코드만 읽어 보세요.
## 첫째, tabulate 라이브러리를 따로 설치해야 하는데 IDE 에는 들어 있지 않다.
## 둘째, food.csv · average.csv · eatenfood.csv 세 파일이 있어야 하는데 그 파일이 없다.
## 그래서 실행하면 ModuleNotFoundError 나 FileNotFoundError 가 난다.
## Food는 음식 하나의 이름·1회 제공량·영양 성분을 담는 클래스이다.
## User는 사용자가 먹은 음식과 섭취한 영양 성분을 담는 클래스이다.
## App은 데이터를 읽고(open_data), 음식을 찾고(find_food), 영양을 더하고(calc_food),
## 결과를 표로 보여 주는(show_result) 기능을 모아 둔 클래스이다.
## calc_food는 먹은 양을 1회 제공량으로 나눈 비율만큼 영양 성분을 곱해서 더한다.
## show_result는 평균 섭취량에서 내가 먹은 양을 빼서 부족한 영양소를 구한다.
## open_data와 show_result에는 self가 없어서 App.open_data() 처럼 클래스 이름으로 바로 부른다.
## 클래스 세 개가 각자 맡은 일을 나눠 하나의 앱이 되는 구조를 눈여겨보세요.