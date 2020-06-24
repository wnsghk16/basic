class Service:
    def __init__(self):
        self._contatcs = []

    def add_concat(self, payload):
        self._contatcs.append(payload)

    def get_contact(self,payload): #name
        for i in self._contatcs:
            if(payload == i.name):
                return i

    def get_contacts(self)->[]:
        contacts = []
        for i in self._contatcs:
            contacts.append(i.to_string())
        return ','.join(contacts)

    def del_contact(self,payload): #name
        for i,t in enumerate(self._contatcs):
            if(payload == t.name):
                del self._contatcs[i]

