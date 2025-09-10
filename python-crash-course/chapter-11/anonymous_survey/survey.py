class AnonymousSurvey:
    """声明一个匿名类，存储调查问卷"""
    
    def __init__(self, question):
        """初始化，记录提问和回答"""
        self.question = question
        self.responses = []
        
    def store_response(self, response):
        """存储新增回答问卷"""
        self.responses.append(response)
        
    def show_result(self):
        """遍历展示问卷和结果"""
        print(self.question)
        for response in self.responses:
            print(f"\t{response}")
