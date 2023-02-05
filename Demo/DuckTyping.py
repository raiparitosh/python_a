                               # Duck Typing Demo
# you are passing an object of a class in a method, so the method does not bother which class object you are passing as an argument 
# in that method, the thing which matters is the method which you are calling by that object should be present in that class

                          # Example 1

class VSCode:

    def execute(self):
        print("Complie")
        print("Run")

class MyEditor:

    def execute(self):
        print("Spell Check")
        print("Convention check")
        print("Compile")
        print("Run")

class Notepad:
    def show(self):
        print("Showing")        

class Laptop:

    def code(self,ide):
        print("Coding...")

        ide.execute()

lap1 = Laptop()
# ide = VSCode()
ide = MyEditor()
# ide = Notepad()

lap1.code(ide)

                                   #  Example 2

# class Winapp:
#     def play(self):
#         print("Winapp se Playing")

# class Spotify:
#     def play(self):
#         print("Spotify se Playing")

# class WindowsMediaPlayer:
#     def hang(self):
#         print("Haging")

# def doSomething(player):
#     player.play()                  

# obj = Winapp()
# obj1 = Spotify()
# obj2 = WindowsMediaPlayer()                        

# doSomething(obj1)