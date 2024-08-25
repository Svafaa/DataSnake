class Config:
    def __init__(self,linesize,pagesize,colsep,spoolname,spooltype):
        self.linesize = linesize
        self.pagesize = pagesize
        self.colsep = colsep
        self.spoolname = spoolname
        self.spooltype = spooltype
    
    def spool_config(self):
        '''
            Função para analisar se o spool está configurado como txt ou csv e montar o spool.
        '''
        if self.spooltype == 'txt': 
            return f'SET LINESIZE {self.Linesize}\nSET PAGESIZE {self.Pagesize}\nSET COLSEP "{self.Pagesize}"\nSET TRIMSPOOL ON\nSET ECHO OFF\n SET FEEDBACK OFF\nSPOOL {self.spoolname}'

        elif self.spooltype == 'csv':
            return f'SET LINESIZE {self.Linesize}\nSET PAGESIZE 0\n SET HEADSEP 0\n SET COLSEP ","\n SET FEEDBACK OFF\n SPOOL {self.spoolname}'