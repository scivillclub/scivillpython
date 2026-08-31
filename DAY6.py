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