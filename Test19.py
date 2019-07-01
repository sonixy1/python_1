tel1 = "010-4088-0"  # 검사할 1번째 번호
tel2 = "010-4088-0166"  # 검사할 2번째 번호

def para2_func(v1, v2):
    result = v1 + v2
    return result

def Tel_check(tel):  # 전화번호 양식에 맞는지 확인 기능 함수
    tel = tel.replace('-', '')  # 전화번호에서 - 빼기
    if len(tel) == 11: # 11자리이면 양식에 맞음
        return print("핸드폰 전화번호 형식에 맞음")
    else: # 양식에 맞지 않음
        return print("핸드폰 전화번호 형식에 맞지 않음")

if __name__ == "__main__":  # Main 함수

    Tel_check(tel1) # tel1 번호 확인용 함수 호출
    Tel_check(tel2) # tel2 번호 확인용 함수 호출
