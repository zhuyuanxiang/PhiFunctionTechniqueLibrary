from .CCPhiFunction import *from .CPPhiFunction import *from .PPPhiFunction import *def build_phi_function(A, B):    DynamicGrid = {            'Circle' : {'Circle': CCPhiFunction, 'Polygon': CPPhiFunction},            'Polygon': {'Circle': CPPhiFunction, 'Polygon': PPPhiFunction}    }    if 'CustomObject' in [A.ObjectType, B.ObjectType]:        return ComplexPhiFunction(A, B)    else:        return DynamicGrid[A.ObjectName][B.ObjectName](A, B)class ComplexPhiFunction(PhiFunction):    def __init__(self, A, B):        PhiFunction.__init__(self, A, B, 'Complex')        if 'CustomObject' not in [A.ObjectType, B.ObjectType]:            raise TypeError('At least one of A or B must belong to CustomObject type')        self.FunctionName = 'Complex'        # Decompose down the tree        if A.ObjectType != 'CustomObject':            self.__init__(B, A)  # For customs to be always decomposed at first        else:            self.Operation = 'Min' if A.Operator == 'Or' else 'Max'            self.Functions = [build_phi_function(obj, B) for obj in A.Objects]    def Evaluate(self):        if self.Operation == 'Min':            return np.min([                    func.Evaluate() for func in self.Functions            ])        else:            return np.max([                    func.Evaluate() for func in self.Functions            ])