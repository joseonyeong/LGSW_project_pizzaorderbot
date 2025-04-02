def pizzaorder_step03():
    order = {'피자': [], '토핑': []}
    categories = ['피자', '토핑']
    i = 0
    current_category = categories[i]

    while True:
        print(f"\n{current_category}를 선택하세요. 수량 추가를 위해 여러번 선택 가능합니다.")
            # 메뉴판
        for idx, item in enumerate(menus[current_category]):
            print(f"{idx+1}. {item} ({prices[current_category][idx]}원) ")
        
        choice = input("번호를 입력하고 Enter를 누르세요 (다음단계:n, 이전단계:p, 주문완료:f)")
            # 종료
        if choice.upper() == 'F':
            break
            # 숫자
        if choice.isdigit():
            index = int(choice) - 1
            order[current_category].append( menus[current_category][index] )
            print(f"선택된 메뉴: {menus[current_category][index]}")
            i += 1
            # 다음 단계
        elif choice.upper() == 'N':
            if i < len(categories) - 1:    
                i += 1
                current_category = categories[i]
            # 이전 단계
        elif choice.upper() == 'P':
            if i > 0:
                i -= 1
                current_category = categories[i]
        current_category = categories[i % (len(menus))]
    return order


if __name__ == '__main__':
    print('피자 가게에 오신 것을 환영합니다.', end='\n')
    menus = {
        '피자': ['페퍼로니 피자', '스테이크 피자', '시푸드 피자'],
        '토핑': ['햄', '페퍼로니', '트러플', '올리브', '새우'],
    }
    prices = {
        '피자': [29000, 32000, 32000],
        '토핑': [500, 500, 800, 300, 800],
    }
    
    print(pizzaorder_step03())
    
    
