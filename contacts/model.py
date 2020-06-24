class Model:
    def __init__(self):
        self._name='',
        self._phone=''
        self._email=''
        self._addr=''

    @property
    def name(self)->str: return self._name
    @name.setter
    def name(self,name): self._name = name

    @property
    def phone(self)->str: return self._phone
    @phone.setter
    def phone(self,phone): self._phone = phone

    @property
    def email(self)->str: return self._email
    @email.setter
    def email(self,email): self._email = email

    @property
    def addr(self)->str: return self._addr
    @addr.setter
    def addr(self,addr): self._addr = addr

    def __str__(self)->str:
        return '[이름 : %s, 전화번호 : %s, 이메일 : %s, 주소 : %s]' % (self._name, self._phone,self._email,self._addr)

    def to_string(self)->str:
        return '\n[이름 : {}, 전화번호 : {}, 이메일 : {}, 주소 : {}]'.format(self._name, self._phone,self._email,self._addr)