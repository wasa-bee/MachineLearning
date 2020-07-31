import random

def lotto_number_create():
    list = []
    ran_num = random.randint(1,45)
    for i in range(6):
        while ran_num in list:
            ran_num = random.randint(1, 45)
        list.append(ran_num)
    list.sort()
    return list

def do_lotto(cnt):
    for i in range(cnt):
        print(lotto_number_create())

CNT = input("게임 수를 입력하세요. (정수) : ")
do_lotto(int(CNT))




