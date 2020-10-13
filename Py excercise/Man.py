class Man:
    def __init__(self,name,prefix):
      self.prefix = prefix
      self.name = name
      print("Initialized!!")
    def hello(self):
      print('hello,' + self.prefix + '.' + self.name + '!!')

    def goodbye(self):
      print('goodbye,' + self.prefix + '.' + self.name + '!!')

m = Man('QYQ','Genius')
m.hello()
m.goodbye()
