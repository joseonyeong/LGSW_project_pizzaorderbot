''' step01
    숫자는 예외처리 x
    글자는 예외처리 0
    피자명 입력받고 리스트
    메뉴판엔 메뉴명(가격)으로 
    f == 종료
    
    isdigit()함수로 예외처리
'''
def pizzaorderstep01():
    order = []
    order_price = []
        #f 입력할 때까지 무한루프
    while True:
        print('피자를 선택하세요. 수량 추가를 위해 여러번 선택 가능합니다.')
        print('1. 페퍼로니 피자 (29000원)')
        print('2. 스테이크 피자 (32000원)')
        print('3. 시푸드 피자 (32000원)')
        user = input('번호를 입력하고 Enter를 누르세요. (주문완료는 f를 누르세요.): ')
            # 선택된 메뉴 출력
            # 종료
        if  user == 'f':
            break
        else:
            if user.isdigit() == True:
                user = int(user)
                    # menu와 맞는 숫자
                print('선택된 메뉴:', menus[user-1])
                order.append(menus[user-1])
                order_price.append(price[user-1])
                print('\n')
            else:
                print('숫자 입력')
    return order, order_price

if __name__ == '__main__':
    print('피자 가게에 오신 것을 환영합니다.')
    menus = ['페퍼로니 피자', '스테이크 피자', '시푸드 피자']
    price = [29000, 32000, 32000]
    
    order, order_price = pizzaorderstep01()
    print('주문 내역: ', order)
    print('가격 내역: ', order_price)