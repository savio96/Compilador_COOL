from classe import *
class ExprParenteses(Class):
    def __init__(self, string):
        super().__init__()
        self.expr=string

    def mostrar(self,string):
        print("( "+string+ " )")