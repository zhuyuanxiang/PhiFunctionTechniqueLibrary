import numpy as np


class PhiObject:
    """所有Phi函数处理形状的公共基类"""
    def __init__(self,
                 origin,    # 原始的图片数据
                 rotation=0,
                 obj_type='',
                 inv=False):
        self.Origin = np.array(origin, dtype='float64')
        self.Rot = rotation
        self.ObjectType = obj_type
        self.sgn = 1
        if inv:
            self.Inverse()

    def Inverse(self):
        self.sgn *= -1

    def _Outline1d(self, u):
        pass

    def Outline(self, u):
        if len(np.shape(u)) == 1:   # 一维形状
            return self._Outline1d(u)
        elif len(np.shape(u)) == 2: # 二维形状
            return np.apply_along_axis(self._Outline1d, 1, u)

    def Locate(self, u):  # u - 3d vector
        self.Translate((u[0], u[1]))
        self.Rotate(u[2])

    def Translate(self, dest=None, delta=None):
        pass

    def Rotate(self, teta, pol=None):
        pass

    def SetMetrices(self):
        pass
