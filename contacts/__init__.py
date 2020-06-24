from contacts.controller import Controller

if __name__ == '__main__':
    def print_menu():
        print('0.Exit')
        print('1.연락처 추가')
        print('2.연락처 이름 검색')
        print('3.연락처 전체 목록')
        print('4.연락처 이름 삭제')
        return input('Menu\n')

    app = Controller()
    while 1:
        menu = print_menu()
        if menu=='0' : break
        if menu == '1':
            app.register(input('이름\n'),
                         input('전화번호\n'),
                         input('이메일\n'),
                         input('주소\n'))

            print('완료')
        if menu == '2':
            print(app.search(input('이름\n')))
        if menu == '3':
            print(app.list())
            # result = app.list()
            # print('\n'.join(str(item) for item in result))
        if menu == '4':
            app.remove(input('이름\n'))
            print('완료')
