
def season(month):
    if month > 2 and month < 6:
        print("spring")
    elif month > 5 and month < 9:
        print("summer")
    elif month > 8 and month < 12: 
        print("fall")
    else :
        print("winter")
 

n = int(input("좋아하는 달을 입력하세요."))

season(n)
