class User():
  
    def  __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def name(self):
        print( self.first_name + self.last_name)
User1 = User("Александр","Иванов")

print(User1.first_name)
print(User1.last_name)
print("Меня зовут", User1.first_name, User1.last_name)