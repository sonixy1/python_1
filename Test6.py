def myFunc():
    print("함수를 호출함.")

def main():
    print("메인 함수가 호출됩니다.")
    myFunc()
    print("전역 변수 값", gVar)

gVar = 100

if __name__ == '__main__':
    main()