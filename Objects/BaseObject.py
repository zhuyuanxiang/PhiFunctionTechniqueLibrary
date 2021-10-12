from .PhiObject import *


class BaseObject(PhiObject):
    """圆形、多边形、矩形的公共基类"""

    def __init__(self,
                 origin,
                 rotation=0,
                 obj_name='',
                 inv=False):
        PhiObject.__init__(self, origin, rotation, 'BaseObject', inv)
        self.ObjectName = obj_name
        self.Curves = None

    def SetMetrices(self, r):
        pass

    def GetMetrices(self):
        pass
