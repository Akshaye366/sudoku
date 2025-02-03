class config:

    DEFAULTCOLOUR = '#F2F2F2'
    COLOURS = ['#F2F2F2', '#9d72ab', '#9d72ab', '#64a154', '#e34444']
    DIFFICULTIES = ['Easy', 'Medium', 'Hard']
    username = None

    @classmethod
    def setUsername(self, name):
        self.username = name

    @classmethod
    def getUsername(self):
        return self.username
    
    @classmethod
    def removeUsername(self):
        self.username = None