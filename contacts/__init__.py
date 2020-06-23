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
            name = str(input('이름\n'))
            phone = str(input('전화번호\n'))
            email = str(input('이메일\n'))
            addr = str(input('주소\n'))
            app.register(name,phone,email,addr)
            print('완료')
        if menu == '2':
            app.search(input('이름\n'))
        if menu == '3':
            app.list()
        if menu == '4':
            app.remove(input('이름\n'))
            print('완료')
