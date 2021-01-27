class Robot:
    def greet(self):
        print('Hello Viraj')

class RobotChild(Robot):
    def greet(self):
        print('Hello Scott')

# Instantiate RobotChild Class
child = RobotChild()
# Invoke Greet method from RobotChild class
child.greet()
