if __name__ == '__main__':
    user_year = int(input('輸入一個年份以判別是否為閏年: '))
    if user_year % 400 == 0 or (user_year % 4 == 0 and user_year % 100 != 0):
        print(str(user_year) + '是閏年。')
    else:
        print(str(user_year) + '不是閏年。')

    input('輸入 Enter 鍵結束...')


'''

輸入一個年份以判別是否為閏年: 2020
2020是閏年。
輸入 Enter 鍵結束...

'''
