class ActualUser:
    def __init__(self):
        self.last_user = 0

    def __call__(self, last: int):
        self.last_user = last
        
    def __int__(self):
        return self.last_user
    
    
actual_user = ActualUser()
