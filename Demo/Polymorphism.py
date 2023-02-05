                      # Method Overriding Demo

class OS1:

    def call(self):
        print("Calling 15")

    def getNotification(self):
        print("Notification on Top, 15")

class OS2(OS1):
    
    def getNotification(self):
        print("Notification at Bottom, 16")

class Iphone:

    def getOSVersion(self,os):
        os.getNotification()

    def callkaro(self,os):
        os.call()    

obj = Iphone()
os = OS2() 
obj.getOSVersion(os)   
obj.callkaro(os)                         

