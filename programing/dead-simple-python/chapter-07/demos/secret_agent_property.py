class SecretAgent:
    
    _codeword = None
    
    def __init__(self, codename):
        # 初始化实例属性
        self.codename = codename
        self._secrets = []
        
    def __del__(self):
        print(f"Agent {self.codename} has been disavowed!")
        
    def remember(self, secret):
        self._secrets.append(secret)
        
    @classmethod
    def inform(cls, codeword):
        cls._codeword = codeword
        
    @staticmethod
    def inquire(question):
        print("I konw nothing.")
        
    @classmethod
    def _encrypt(cls, message, *, decrypt=False):
        # 声明了一个加密解密的类方法，结合类属性`_codeword`对传入的message字符串进行加密解密
        code = sum(ord(c) for c in cls._codeword)
        if decrypt:
            code = -code
        return "".join(chr(ord(m) + code) for m in message)
    
    @property
    def secret(self):
        return self._secrets[-1] if self._secrets else None
    
    @secret.setter
    def secret(self, value):
        self._secrets.append(self._encrypt(value))
        
    @secret.deleter
    def secret(self):
        self._secrets = []