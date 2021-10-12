from .PhiFunction import *


class BasicPhiFunction(PhiFunction):
    """两个形状之间的Phi函数的基类"""

    def __init__(self, A, B, func_name=''):
        PhiFunction.__init__(self, A, B, 'Basic')
        for obj in [A, B]:
            if obj.ObjectType != 'BaseObject':
                raise TypeError('A and B must belong to BaseObject type')
        self.FunctionName = func_name
