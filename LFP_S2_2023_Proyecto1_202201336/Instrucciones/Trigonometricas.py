from Abstract.Abstract  import Expression
import math



class Trigonometricas(Expression):

    def __init__(self, left, right, operation_type, fila, columna):
        self.left = left
        self.right = right
        self.operation_type = operation_type
        super().__init__(fila, columna)

    def operate(self, arbol):
        left_value = ''
        right_value = ''
        print(self.operation_type.operate(arbol))
        if self.left is not None:
            left_value = self.left.operate(arbol)

        if self.operation_type.operate(arbol) == 'seno':
            radians = math.radians(left_value)
            return math.sin(radians)
        elif self.operation_type.operate(arbol) == 'coseno':
            radians = math.radians(left_value)
            return math.cos(radians)
        elif self.operation_type.operate(arbol) == 'tangente':
            radians = math.radians(left_value)
            return math.tan(radians)
        elif self.operation_type.operate(arbol) == 'inverso':
            return 1 / left_value
        else:
            return None

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()