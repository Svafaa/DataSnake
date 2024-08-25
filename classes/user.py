class User:
    def __init__(self,login,password,dbase):
        self.Login = login
        self.Password = password
        self.Dbase = dbase
    
    def create_connection(self):
        return f'sqlplus {self.Login}/{self.Password}@{self.Dbase}'