import getpass

def Login(user):
    check = 0
    while check == 0:
        print("════════ LOG IN ════════")
        id = input("id : ")
        pw = getpass.getpass("pw : ")
        
        for i in range(len(user)):
            if id == user[i][0] and pw == user[i][1]:
                check = 1
                now_user = i
                print("로그인 성공\n")
                
                #로그인 중인 사용자 표시
                print(f"{user[now_user][0]}님 반가워요!")
        if check == 0:
            print("id / password를 확인해 주세요")
    return now_user