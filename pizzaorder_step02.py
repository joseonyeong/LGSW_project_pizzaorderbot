def pizzaorder_step02():
    order = {'피자': [], '토핑': []}
    categories = ['피자', '토핑']
    i = 0
    current_category = categories[i]
    user_order = []     # 사용자가 선택한 피자자
    order_price = []    # 사용자가 선택한 피자 가격
    order_topping = []  # 사용자가 선택한 토핑

        # 피자 가격 value값 추출
        # 토핑 가격 value값 추출
        # current_ccategory가 1번에서 루프        
    
    while True:
        print('피자를 선택하세요. 수량 추가를 위해 여러번 선택 가능합니다.')
        print('1. 페퍼로니 피자 (29000원)')
        print('2. 스테이크 피자 (32000원)')
        print('3. 시푸드 피자 (32000원)')
        user = input("번호를 입력하고 Enter를 누르세요.(주문 종료는 f):" )

            # 종료
        if user.upper() == 'F':
            break
        else:
            # 피자, 가격
                # current_category를 키값으로 추출
                # 피자 value값 추출
                # 토핑 value값 추출
                # current_ccategory가 0번에서 루프
                # current_category = '피자'
                # menu = menus[current_category] 로 사용하기
                # 메뉴판의 0번째의 값들
            menu = menus[current_category]
                # 메뉴판의 가격의 0번째 값들
            menu_price = prices[current_category]
            user = int(user)
                # menu와 맞는 숫자
            print('선택된 메뉴:', menu[user-1])
                # 메뉴 추가
            user_order.append(menu[user-1])
                # 가격 추가
            order_price.append(menu_price[user-1])
            print('\n')
            
            print('토핑을 선택하세요. 수량 추가를 위해 여러번 선택 가능합니다.')
            print('1. 햄 (500원)')
            print('2. 페퍼로니 (500원)')
            print('3. 트러플 (800원)')
            print('4. 올리브 (300원)')
            print('5. 새우 (800원)')
            user = input("번호를 입력하고 Enter를 누르세요.(주문 종료는 f):" )
            if user.upper() == 'F':
                break
            user = int(user)
            # 토핑
            i = 1
            current_category = categories[i]
            topping = menus[current_category]
            order_topping.append(topping[user-1])
            order_price.append(order_price[user-1] + menu_price[user-1]) 
            
            order['피자'] = user_order
            order['토핑'] = order_topping
    return order


if __name__ == '__main__':
    print('피자 가게에 오신 것을 환영합니다.', end='\n')
    menus = {
        '피자': ['페퍼로니 피자', '스테이크 피자', '시푸드 피자'],
        '토핑': ['햄', '페퍼로니', '트러플', '올리브', '새우']
    }
    prices = {
        '피자': [29000, 32000, 32000],
        '토핑': [500, 500, 800, 300, 800]
    }
    
    print(pizzaorder_step02())
    
# 피자 가게에 오신 것을 환영합니다.
# 피자를 선택하세요. 수량 추가를 위해 여러번 선택 가능합니다.
# 1. 페퍼로니 피자 (29000원)
# 2. 스테이크 피자 (32000원)
# 3. 시푸드 피자 (32000원)
# 번호를 입력하고 Enter를 누르세요.(주문 종료는 f):1
# 선택된 메뉴: 페퍼로니 피자


# 토핑를 선택하세요. 수량 추가를 위해 여러번 선택 가능합니다.
# 1. 햄 (500원)
# 2. 페퍼로니 (500원)
# 3. 트러플 (800원)
# 4. 올리브 (300원)
# 5. 새우 (800원)
# 번호를 입력하고 Enter를 누르세요.(주문 종료는 f):1
# 피자를 선택하세요. 수량 추가를 위해 여러번 선택 가능합니다.
# 3. 트러플 (800원)
# 4. 올리브 (300원)
# 5. 새우 (800원)
# 번호를 입력하고 Enter를 누르세요.(주문 종료는 f):1
# 피자를 선택하세요. 수량 추가를 위해 여러번 선택 가능합니다.
# 5. 새우 (800원)
# 번호를 입력하고 Enter를 누르세요.(주문 종료는 f):1
# 피자를 선택하세요. 수량 추가를 위해 여러번 선택 가능합니다.
# 피자를 선택하세요. 수량 추가를 위해 여러번 선택 가능합니다.
# 1. 페퍼로니 피자 (29000원)
# 2. 스테이크 피자 (32000원)
# 1. 페퍼로니 피자 (29000원)
# 1. 페퍼로니 피자 (29000원)
# 2. 스테이크 피자 (32000원)
# 3. 시푸드 피자 (32000원)
# 번호를 입력하고 Enter를 누르세요.(주문 종료는 f):f
# {'피자': ['페퍼로니 피자'], '토핑': ['햄']}