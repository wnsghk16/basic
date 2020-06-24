class Model:
    def __init__(self):
        self._url=""
        self._parser=""
        self._path=""
        self._api=""

    @property
    def url(self)->str: return self._url
    @url.setter
    def url(self,url): self._url = url

    @property
    def parser(self)->str: return self._parser
    @parser.setter
    def parser(self,parser): self._parser = parser

    @property
    def path(self)->str: return self._path
    @path.setter
    def path(self,path): self._path = path

    @property
    def api(self)->str: return self._api
    @api.setter
    def api(self,api): self._api = api