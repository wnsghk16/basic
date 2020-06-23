class Service:
    def __init__(self):
        self._contatcs = []

    def add_concat(self, payload):
        self._contatcs.append(payload)

    def get_contact(self,payload): #name
        for i in self._contatcs:
            if(payload == i.name):
                print(i)

    def get_contacts(self):
        for i in self._contatcs:
            print(i)

    def del_contact(self,payload): #name
        cnt = 0
        for i in self._contatcs:
            if(payload == i.name):
                del self._contatcs[cnt]
            cnt += 1

