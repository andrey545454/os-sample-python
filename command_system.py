# лист генерируемых команд
command_list = []

# непонятный код для генерации списка команд
class Command:
   def __init__(self):
       self.__keys = []
       self.description = ''
       command_list.append(self)

   @property
   def keys(self):
       return self.__keys

   @keys.setter
   def keys(self, mas):
       for k in mas:
           self.__keys.append(k.lower())

   def process(self):
       pass