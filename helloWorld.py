class HelloWorld:
    def __init__(self, message):
        self.message = message
    def printMessage(self):
        print(self.message)

world = HelloWorld("hi there!")
world.printMessage()