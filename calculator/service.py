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