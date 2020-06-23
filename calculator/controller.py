from calculator.model import Model
from calculator.service import Service

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




