# ==============================
# 6. 리스트
# ==============================


# 리스트
fruits = ["사과", "바나나", "포도"]

print(fruits)
## 리스트는 여러 개의 값을 하나의 변수에 저장할 수 있는 자료구조이다.


# 리스트 저장방식
numbers = [10, 20, 30]
names = ["민수", "철수", "영희"]
data = ["민수", 17, 175.5, True]

print(numbers)
print(names)
print(data)
## 리스트는 대괄호([])를 이용하여 생성하며, 각 값은 쉼표(,)로 구분한다.
## 리스트는 서로 다른 자료형을 함께 저장할 수 있다.


# 리스트 인덱싱
fruits = ["사과", "바나나", "포도"]
## fruits는 ["사과", "바나나", "포도"]라는 리스트를 저장한 변수이다.
## Python의 변수에는 숫자, 문자열뿐만 아니라 리스트도 저장할 수 있다.


# 리스트 값 출력
print(fruits[0])    # 첫 번째 값 → 사과
print(fruits[1])    # 두 번째 값 → 바나나
print(fruits[2])    # 세 번째 값 → 포도
## 리스트의 인덱스는 0부터 시작한다.


# 음수 인덱싱
print(fruits[-1])   # 맨 마지막 값 → 포도
print(fruits[-2])   # 뒤에서 두 번째 → 바나나
print(fruits[-3])   # 뒤에서 세 번째 → 사과
## 음수 인덱스를 이용하면 리스트의 뒤쪽부터 값을 가져올 수 있다.


# 리스트 슬라이싱
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # 1번부터 3번까지 → [20, 30, 40]
print(numbers[:3])    # 처음부터 2번까지 → [10, 20, 30]
print(numbers[2:])    # 2번부터 끝까지 → [30, 40, 50]
print(numbers[-2:])   # 뒤에서 두 개 → [40, 50]
## 리스트[시작:끝]은 시작 위치부터 끝 위치 바로 앞까지 잘라 새로운 리스트를 만든다.
## 끝 위치의 값은 포함되지 않는다.
## 시작을 비우면 처음부터, 끝을 비우면 마지막까지를 의미한다.
## 잘라내도 원래 리스트는 그대로 남는다.


# 리스트 값 변경
fruits[1] = "딸기"
print(fruits)
## 리스트는 특정 위치의 값을 변경할 수 있다.


# 리스트 값 추가 - append()
fruits.append("수박")
print(fruits)
## append()는 리스트의 마지막에 값을 추가한다.


# 리스트 특정 위치에 추가 - insert()
fruits.insert(1, "복숭아")
print(fruits)
## insert(위치, 값)은 원하는 위치에 값을 추가한다.


# 리스트 값 삭제 - remove()
fruits.remove("사과")
print(fruits)
## remove()는 지정한 값을 리스트에서 삭제한다.


# 리스트 값 삭제 - pop()
fruits.pop(0)
print(fruits)
## pop()은 특정 위치의 값을 삭제한다.


# 리스트 길이
print(len(fruits))
## len()은 리스트에 들어 있는 값의 개수를 반환한다.


# 리스트에 값이 있는지 확인
if "포도" in fruits:
    print("포도가 있습니다.")

if "망고" not in fruits:
    print("망고가 없습니다.")
## in과 not in을 이용하여 리스트에 값이 있는지 확인할 수 있다.


# 리스트 값 개수 세기 - count()
numbers = [1, 2, 3, 2, 5, 2]
print(numbers.count(2))   # 2가 몇 개 있는지 → 3
print(numbers.count(7))   # 리스트에 없는 값 → 0
## count()는 리스트 안에 그 값이 몇 개 있는지 센다.
## 리스트에 없는 값을 넣으면 0이 나온다.


# 값의 위치 찾기 - index()
print(fruits.index("포도"))   # 포도가 몇 번째에 있는지 → 2
## index()는 찾는 값이 몇 번째에 있는지 알려 준다.
## 인덱스는 0부터 시작하므로 세 번째 값이면 2가 나온다.
## 같은 값이 여러 개 있으면 가장 앞에 있는 위치만 알려 준다.


# 리스트와 for문
for fruit in fruits:
    print(fruit)
## for문을 이용하여 리스트의 값을 하나씩 가져올 수 있다.


# 리스트 정렬
numbers = [5, 2, 8, 1, 4]
numbers.sort()
print(numbers)
## sort()는 리스트의 값을 오름차순으로 정렬한다.


# 리스트 역순
numbers.reverse()
print(numbers)
## reverse()는 리스트의 순서를 반대로 뒤집는다.


# 리스트로 변환 - list()
numbers = list(range(1, 6))
letters = list("파이썬")

print(numbers)
print(letters)
## list()는 다른 자료형을 리스트로 바꾼다.
## list(range(1, 6))은 range()가 만든 1부터 5까지의 값을 리스트로 만든다.
## 문자열을 넣으면 글자를 하나씩 나눈 리스트가 된다.


# ==============================
# 7. 자료구조
# ==============================


# 2차원 리스트
scores = [
    [90, 80, 70],
    [85, 95, 100],
    [70, 75, 80]
]

print(scores)
print(scores[0])
print(scores[0][1])
## scores는 2차원 리스트를 저장한 변수이다.
## 리스트 안에 또 다른 리스트를 저장할 수 있으며, 이를 2차원 리스트라고 한다.
## scores를 출력하면 안쪽의 리스트를 포함한 전체 리스트가 출력된다.
## scores[0]은 첫 번째 안쪽 리스트인 [90, 80, 70]을 의미한다.
## scores[0][1]은 첫 번째 리스트에서 두 번째 값인 80을 의미한다.
## 2차원 리스트에서도 인덱스는 0부터 시작한다.


# 2차원 리스트와 for문
for student in scores:
    print(student)
## for문을 이용하여 2차원 리스트 안의 리스트를 하나씩 가져올 수 있다.


# 중첩 for문과 2차원 리스트
for student in scores:
    for score in student:
        print(score)
## 중첩 for문을 이용하면 2차원 리스트 안의 모든 값을 하나씩 가져올 수 있다.


# 튜플
numbers = (10, 20, 30)

print(numbers)
print(numbers[0])
## 튜플(tuple)은 여러 개의 값을 순서대로 저장하는 자료구조이다.
## 튜플은 일반적으로 소괄호(()) 안에 값을 쉼표(,)로 구분하여 생성한다.


# 튜플과 리스트의 차이
numbers = (10, 20, 30)
## 예를 들어 numbers[0] = 100과 같이 튜플의 값을 변경할 수 없다.
## 튜플은 한 번 생성하면 저장된 값을 변경할 수 없다.
## 리스트는 값을 변경할 수 있지만 튜플은 값을 변경할 수 없다.


# 딕셔너리
student = {
    "이름": "민수",
    "나이": 17,
    "점수": 90
}

print(student)
## 딕셔너리(dict)는 key와 value를 한 쌍으로 저장하는 자료구조이다.
## 딕셔너리는 중괄호({})를 이용하여 생성한다.


# 딕셔너리 값 출력
print(student["이름"])
print(student["나이"])
print(student["점수"])
## 딕셔너리는 인덱스 대신 key를 이용하여 value를 가져온다.


# 딕셔너리 값 변경
student["점수"] = 95
print(student)
## 이미 존재하는 key에 새로운 값을 저장하면 기존 value가 변경된다.


# 딕셔너리 값 추가
student["반"] = 3
print(student)
## 존재하지 않는 새로운 key에 값을 저장하면 새로운 항목이 추가된다.


# 딕셔너리 값 삭제
del student["나이"]
print(student)
## del을 이용하여 딕셔너리의 특정 항목을 삭제할 수 있다.


# 딕셔너리에 key가 있는지 확인
if "주소" in student:
    print("주소 정보가 있습니다.")
else:
    print("주소 정보가 없습니다.")
## in을 이용하여 딕셔너리에 특정 key가 있는지 확인할 수 있다.


# 딕셔너리와 for문
for key in student:
    print(key, student[key])
## for문을 이용하여 딕셔너리의 key를 하나씩 가져올 수 있다.


# 튜플과 딕셔너리의 차이
person_tuple = ("영희", 16, 95)

person_dict = {
    "이름": "영희",
    "나이": 16,
    "점수": 95
}

print(person_tuple[2])
print(person_dict["점수"])
## 튜플은 값의 위치인 인덱스를 이용하여 값을 가져온다.
## 딕셔너리는 값에 붙인 key를 이용하여 값을 가져온다.


# 학급 성적 관리
names = ["민수", "영희", "철수"]
scores = [
    [90, 80, 70],
    [85, 95, 100],
    [70, 75, 80]
]

for i in range(len(names)):
    total = 0

    for score in scores[i]:
        total = total + score

    print(names[i], "총점:", total, "평균:", total / len(scores[i]))
## len(names)는 학생 수와 같으므로 range()에 넣어 학생 번호를 만들 수 있다.
## names[i]와 scores[i]는 같은 번호의 학생 이름과 점수를 가리킨다.
## 안쪽 for문은 한 학생의 점수를 하나씩 더해 총점을 구한다.
## total / len(scores[i])는 점수 개수로 나눈 평균이다.