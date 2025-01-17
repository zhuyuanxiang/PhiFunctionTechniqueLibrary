from .BasicPhiFunction import *
import numpy as np


class PPPhiFunction(BasicPhiFunction):
    """多边形与多边形之间的Phi函数"""

    def __init__(self, A, B):
        if (A.ObjectName != 'Polygon') | (B.ObjectName != 'Polygon'):
            raise TypeError('A and B must be a pair of Polygons')
        BasicPhiFunction.__init__(self, A, B, 'PP')

    def Evaluate(self):
        self.Value = np.max([
                np.max([
                        np.min(np.apply_along_axis(cur, 1, self.B.Vertices))
                        for cur in self.A.Curves
                ]),
                np.max([
                        np.min(np.apply_along_axis(cur, 1, self.A.Vertices))
                        for cur in self.B.Curves
                ])
        ])
        return self.Value
