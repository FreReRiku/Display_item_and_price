def calc():
    total_item_info = []
    i = 0
    total_price = 0

    number_y_n = int(input("計算を始めます。1を入力してください。\n"))
    while number_y_n == 1:
        item_name = input("商品名を入力してください：")
        item_price = int(input("購入した商品の価格を入力してください："))
        item_info = {item_name: item_price}
    
        total_price += item_price
    
        total_item_info.append(item_info)
        print("入力した内容は以下の通りです\n")
        print(item_info)

        print("入力を完了しますか？\n")
        number_y_n = int(input("続けるなら1を終了するならその他のキーを入力してください\n"))

        print("今回入力した内容は以下の通りです")

        for i in range(len(total_item_info)):
            print(total_item_info[i])

    print("総額は以下の通りです")
    print(total_price)

calc()

