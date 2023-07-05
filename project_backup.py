import sys

# argv의 리스트 길이가 2보다 작다면 (파일명을 입력하지 않았다면) filename="students.txt"로 지정
if len(sys.argv) < 2 :
    filename = "students.txt"
else :  # 아니라면 filename에는 입력값을 넣어줌
    filename = sys.argv[1]

    
# read모드로 오픈    
fr = open(filename, "r")
FileContent = fr.read().split()
print("값 읽어들이기 (1행으로 출력)")
print(FileContent)

# 빈 list를 만들고 5행으로 나눠줌
print("빈 list를 만들고 5행으로 나눠줌")

FileContent_list = []

for i in range(0, len(FileContent), 5):
    FileContent_list.append(FileContent[i:i+5])

for i in range(len(FileContent_list)):
    print(FileContent_list[i])

# 성+이름 합치기 ( 1번 인덱스(성) + 2번 인덱스(이름) 합친 후에 2번 인덱스 삭제
print("성 + 이름 합치기")
for i in range(len(FileContent_list)):
    FileContent_list[i][1] = FileContent_list[i][1]+" "+FileContent_list[i][2]
    del(FileContent_list[i][2])
    print(FileContent_list[i])

    
# Dict 형태로 다시 저장

stu_dict = {i[0]: None for i in FileContent_list} # list의 0번째 열만 key 값으로 넣어주기
# for i in range(len(FileContent_list)):
#     stu_dict = {FileContent_list[i][0] : None }

print("sdafsdafsda")
print(stu_dict)
# for key, value in stu_dict.items():
#     print(key, *value)  

#stu_dict = {'20180001': None, '20180002': None, '20180007': None, '20180009': None, '20180011' : None}

i = 0
for key in stu_dict.keys():
    stu_dict[key] = FileContent_list[i][1:]
    i += 1

print("중간출력 (dict 형태)")
print("Student Name Midterm Final Average Grade")
print("----------------------------------------")
for key, value in stu_dict.items():
    print(key, *value)    
    
    
# 평균 계산하기
# def calcul_avg(a, b):
#     hap = a+b
#     avg = hap/2
#     return avg

# print("평균 계산해서 넣어주기")
# for i in range(len(FileContent_list)):
#     avg1 = calcul_avg(int(FileContent_list[i][2]),int(FileContent_list[i][3]))
#     FileContent_list[i].append(avg1)
#     print(FileContent_list[i])

for key in stu_dict.keys():  # 평균값이 들어갈 index 3의 빈자리 생성
    stu_dict[key].append(None)


def calcul_avg(m_index, f_index, ccc_list):
    hap = int(ccc_list[m_index]) + int(ccc_list[f_index])
    avg = hap/2
    ccc_list[3] = avg
    return ccc_list

print("평균 계산해서 넣어주기")
for key in stu_dict.keys():
    calcul_avg(1,2,stu_dict[key])

for key, value in stu_dict.items():
    print(key, *value)

#for key in stu_dict.keys():
    
# 학점 추가해주기
# def calcul_grade(a) :
#     for i in range(len(a)):
#         if a[i][4] >= 90 :
#             a[i].append("A")
#         elif a[i][4] >= 80 :
#             a[i].append("B")
#         elif a[i][4] >= 70 :
#             a[i].append("C")
#         elif a[i][4] >= 60 :
#             a[i].append("D")
#         else :
#             a[i].append("F")
#     return (a[i])

for key in stu_dict.keys():  # 학점이 들어갈 index 4의 빈자리 생성
    stu_dict[key].append(None)

def calcul_grade(a) :    
    if a[3] >= 90 :
        a[4] = "A"
    elif a[3] >= 80 :
        a[4] = "B"
    elif a[3] >= 70 :
        a[4] = "C"
    elif a[3] >= 60 :
        a[4] = "D"
    else :
        a[4] = "F"
    return (a)

print("학점 추가해주기")

for key in stu_dict.keys():
    calcul_grade(stu_dict[key])

for key, value in stu_dict.items():
    print(key, *value)


# print("학점 추가해주기")
# calcul_grade(FileContent_list)
# for i in range(len(FileContent_list)):
#     print(FileContent_list[i])

# 평균 내림차순 정렬해주기
print("평균 내림차순으로 정렬")
stu_dict = dict(sorted(stu_dict.items(), key=lambda x: x[1][3], reverse=True))
"""sorted(정렬할 데이터, key=정렬할 기준값, reverse = (true면 내림차순 false면 오름차순))"""

for key, value in stu_dict.items():
    print(key, *value)
     
    
# Dict 형태로 다시 저장
# stu_dict = {'20180001': None, '20180002': None, '20180007': None, '20180009': None, '20180011' : None}

# i = 0
# for key in stu_dict.keys():
#     stu_dict[key] = sorted_list[i][1:]
#     i += 1

# print("중간출력 (dict 형태)")
# print("Student Name Midterm Final Average Grade")
# print("----------------------------------------")
# for key, value in stu_dict.items():
#     print(key, *value)


    
# 1. show (전체 학생 정보 출력)
def command_show(parameter_dict) :
    sorted_dict = dict(sorted(parameter_dict.items(), key=lambda x: x[1][3], reverse=True))
    print("Student Name Midterm Final Average Grade")
    print("----------------------------------------")
    for key, value in sorted_dict.items():
        print(key, *value)

# 2. search (특징 학생 검색)
def command_search(parameter_dict) :
    input_id = input("학번을 입력해주세요 : ")
    
    if input_id in parameter_dict.keys(): 
        print(input_id, *parameter_dict[input_id])
    else :
        print("NO SUCH PERSON")
    

# 3. changescore (점수 수정)  
def command_changescore(parameter_dict) :
    input_id = input("Student ID : ")

    if input_id in parameter_dict.keys():  # key값 안에 input_id가 있으면
        input_exam = input("Mid/Final? ")
        input_exam = input_exam.lower()

        if input_exam == "mid" :  # 시험이 중간고사일 경우
            input_score = input("Input new score: ")
            input_score = int(input_score)

            if input_score >= 0 | input_score <= 100 :  # 0~100 일 경우에만 값 출력
                print("Student Name Midterm Final Average Grade")
                print("----------------------------------------")
                print(input_id, *parameter_dict[input_id])
                parameter_dict[input_id][1] = input_score
                calcul_avg(1,2,parameter_dict[input_id])
                calcul_grade(parameter_dict[input_id])
                print("Score change.")
                print(input_id, *parameter_dict[input_id])

        elif input_exam == "final" :   # 시험이 기말고사일 경우
            input_score = input("Input new score: ")
            input_score = int(input_score)

            if input_score >= 0 | input_score <= 100 :  # 0~100 일 경우에만 값 출력
                parameter_dict[input_id][2] = input_score
                calcul_avg(1,2,parameter_dict[input_id])
                calcul_grade(parameter_dict[input_id])
                print("Student Name Midterm Final Average Grade")
                print("----------------------------------------")
                print(input_id, *parameter_dict[input_id])

    else :   # key값 안에 input_id가 없으면 "NO SUCH PERSON" 출력
        print("NO SUCH PERSON")

# def command_changescore(a) :
#     input_id = input("Student ID : ")

#     if input_id in stu_dict.keys():  # key값 안에 input_id가 있으면
#         input_exam = input("Mid/Final? ")
#         input_exam = input_exam.lower()

#         if input_exam == "mid" :  # 시험이 중간고사일 경우
#             input_score = input("Input new score: ")
#             input_score = int(input_score)

#             if input_score >= 0 | input_score <= 100 :  # 0~100 일 경우에만 값 출력
#                 stu_dict[input_id][1] = input_score
#                 calcul_avg(1,2,stu_dict[input_id])
#                 calcul_grade(stu_dict[input_id])
#                 print("Student Name Midterm Final Average Grade")
#                 print("----------------------------------------")
#                 print(input_id, *stu_dict[input_id])

#         elif input_exam == "final" :   # 시험이 기말고사일 경우
#             input_score = input("Input new score: ")
#             input_score = int(input_score)

#             if input_score >= 0 | input_score <= 100 :  # 0~100 일 경우에만 값 출력
#                 stu_dict[input_id][2] = input_score
#                 calcul_avg(1,2,stu_dict[input_id])
#                 calcul_grade(stu_dict[input_id])
#                 print("Student Name Midterm Final Average Grade")
#                 print("----------------------------------------")
#                 print(input_id, *stu_dict[input_id])

#     else :   # key값 안에 input_id가 없으면 "NO SUCH PERSON" 출력
#         print("NO SUCH PERSON")       
        
        
def command_add(parameter_dict) :            
    input_id = input("Student ID : ")
    
    if input_id in parameter_dict.keys(): # 기존의 학생과 겹치면 에러문 출력
        print("ALREADY EXISTS.")
    
    else : # 기존의 학생이 아니라면 값을 계속 입력받음
        input_name = input("Name : ")
        input_mid_score = input("Midterm Score : ")
        input_final_score = input("Final Score : ")
        
        parameter_dict[input_id] = [input_name, input_mid_score, input_final_score, None, None]
        avg1 = calcul_avg(1,2,parameter_dict[input_id])
        grade1 = calcul_grade(parameter_dict[input_id])
        
        print("Student added.")
        print(input_id, *parameter_dict[input_id])

def command_searchgrade(parameter_dict):
    input_grade = input("Grade to search : ") 
    input_grade = input_grade.upper()
    if input_grade in ["A","B","C","D","F"]:
        if input_grade in [i[4] for i in parameter_dict.values()] :
            for key, value in parameter_dict.items():
                if input_grade in value:
                    print(key, *value)
        else :
            print("NO RESULT")
    else :
        pass 
        
def command_remove(parameter_dict):    
    if len(parameter_dict) <= 0 :
        print("List is empty.")
    else :
        input_id = input("Student ID : ")
        if input_id in parameter_dict.keys():
            parameter_dict.pop(input_id)
            print("Student removed.")
        else :
            print("NO SUCH PERSON.")
                       
def command_quit(parameter_dict):
    input_YorN = input("Save data?[yes/no] ")
    input_YorN = input_YorN.lower()
    if input_YorN == "yes" :
        input_filename = input("File name: ")
        
        f = open(input_filename, "w")
        
        for key, value in parameter_dict.items():
            data = str(key) + "\t" + "\t".join(str(i) for i in value[:-2]) + "\n"
            f.write(data)         
                
    elif input_YorN == "no" :
        pass
    else :
        print("Yes 또는 No 값을 입력해주세요.")
    



while True:
    # 0. input 값 받아오기
    input_command = input("# ")
    input_command = input_command.lower()  # 대문자 넣어도 소문자로 받기
    # input 값에 따라 맞는 함수 출력
    if input_command == "show" :
        command_show(stu_dict)
    elif input_command == "search" :
        command_search(stu_dict)
    elif input_command == "changescore" :
        command_changescore(stu_dict)
    elif input_command == "add" :
        command_add(stu_dict)
    elif input_command == "searchgrade" :
        command_searchgrade(stu_dict)
    elif input_command == "remove" :
        command_remove(stu_dict)
    elif input_command == "quit":
        command_quit(stu_dict)
        break
    else:
        print("wrong input!")
        
# # input 값에 따라 맞는 함수 출력
# if input_command == "show" :
#     command_show(input_command)
    
# elif input_command == "search" :
#     command_search(input_command)
# elif input_command == "changescore" :
#     command_changescore(input_command)
# elif input_command == "add" :
#     command_add(input_command)
#     break
# else:
#     print("wrong input!")









