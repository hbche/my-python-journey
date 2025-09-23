class SecretAgent:
    # 初始化类属性
    _codeword = ""
    
    # 初始化器，初始化实例属性
    def __init__(self, codename):
        self.codename = codename
        self._secrets = []
        
    # 实例方法
    def remember(self, secret):
        self._secrets.append(secret)
        
    @classmethod
    def inform(cls, codeword):
        cls._codeword = codeword
        
    @staticmethod
    def inquire(question):
        print("I konw nothing.")