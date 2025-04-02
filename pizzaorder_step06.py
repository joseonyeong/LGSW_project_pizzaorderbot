def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
def pizzaorder_step05():
    menus = {
        '피자': ['페퍼로니 피자', '스테이크 피자', '시푸드 피자'],
        '토핑': ['햄', '페퍼로니', '트러플', '올리브', '새우'],
        '사이드': ['치즈 오븐 스파게티', '리조또', '치킨 윙'],
        '음료': ['콜라', '스프라이트', '오렌지 쥬스']
    }
    prices = {
        '피자': [29000, 32000, 32000],
        '토핑': [500, 500, 800, 300, 800],
        '사이드': [9900, 8900, 8900],
        '음료': [1000, 1000, 1000]
    }
    order = {'피자': [], '토핑': [], '사이드':[], '음료':[]}
    categories = ['피자', '토핑', '사이드','음료']
    i = 0
    current_category = categories[i]
    order_price = 0

    while True:
        print(f"\n{current_category}를 선택하세요. 수량 추가를 위해 여러번 선택 가능합니다.")
            # 장바구니
        print(f"현재 장바구니: {order}")
            # 메뉴판
        for idx, item in enumerate(menus[current_category]):
            print(f"{idx+1}. {item} ({prices[current_category][idx]}원) ")
    
        choice = input("번호를 입력하고 Enter를 누르세요 (다음단계:n, 이전단계:p, 주문완료:f)")
        
        # 종료
        if choice.upper() == 'F':
            clear_screen()
            print('-------------')
            print('주문 내역')
            print('-------------')
            for key, value in order.items():
                print(f"{key}: {','.join(value)}")
            print(f"총 금액: {order_price}원 ")
            print("주문이 완료되었습니다. 감사합니다.")
            break
        # 다음 단계
        elif choice.upper() == 'N':
            if i < len(categories) - 1:    
                i += 1
                current_category = categories[i]
            clear_screen()
            # 이전 단계
        elif choice.upper() == 'P':
            if i > 0:
                i -= 1
                print(i)
                current_category = categories[i]
            clear_screen()
            # 숫자 제한
            # 숫자
        elif choice.isdigit():
            index = int(choice) - 1
            if int(choice) < len(menus[current_category])+1:
                order[current_category].append( menus[current_category][index] )
                print(f"선택된 메뉴: {menus[current_category][index]}")
                # i += 1
                # print(i)
                order_price += prices[current_category][index]
                clear_screen()
            else:
                clear_screen()
                print('다시 입력하세요') 
        current_category = categories[i % (len(menus))]
    return order

if __name__ == '__main__':
    print('피자 가게에 오신 것을 환영합니다.', end='\n')    
    pizzaorder_step05()