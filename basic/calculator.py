class Model:
    def __init__(self):
        self._num1 = 0
        self._num2 = 0
        self._opcode = ''

    @property
    def num1(self) -> int: return self._num1
    @num1.setter
    def num1(self,num1): self._num1 = num1

    @property
    def num2(self) -> int: return self._num2
    @num2.setter
    def num2(self, num2): self._num2 = num2

    @property
    def opcode(self) -> str: return self._opcode
    @opcode.setter
    def opcode(self, opcode): self._opcode = opcode

class Service:
    def __init__(self,payload):
        self._num1 = payload.num1
        self._num2 = payload.num2

    def add(self):
        return self._num1 + self._num2

    def min(self):
        return self._num1 - self._num2

    def mult(self):
        return self._num1 * self._num2

    def div(self):
        return self._num1 / self._num2


class Controller:

    def calc(self,num1,num2,opcode):
        model = Model()
        model.num1 = num1
        model.num2 = num2
        model.opcode = opcode
        service = Service(model)
        if opcode == '+': result = service.add()
        if opcode == '-': result = service.min()
        if opcode == '*': result = service.mult()
        if opcode == '/': result = service.div()
        return result

if __name__ == '__main__':

    def print_menu():
        print('0.Exit')
        print('1.Calculator')
        return input('Menu\n')

    while 1:
        menu = print_menu()
        if menu == '0' : break
        if menu == '1' :
            app = Controller()
            print('계산기 작동')
            num1 = int(input('첫번째 수\n'))
            opcode = input('연산자\n')
            num2 = int(input('두번째 수\n'))
            result = app.calc(num1,num2,opcode)
            print('결과 : %d ' % result)