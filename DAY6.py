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


# 여러 줄을 파일에 저장하기
file = open("students.txt", "w", encoding="utf-8")

file.write("민수\n")
file.write("영희\n")
file.write("철수\n")

file.close()
## \n은 줄을 바꾸는 줄바꿈 문자이다.
## write()를 여러 번 사용하여 여러 내용을 파일에 저장할 수 있다.


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