class myClass:
    a = 'She is cute girls.'

    @classmethod
    def classMethod(self):
        print(self.a)
    
    @staticmethod
    # a variable not allowe becouse it's fix without static method 
    # And not allow to perameters 
    def staticMethod():
        # print(self.a)
        print('She is only one for me')

m = myClass()

m.classMethod()
m.staticMethod()