import random
import numpy as np
import matplotlib.pyplot as plt

from icosalattice.UnitSpherePoint import UnitSpherePoint
import icosalattice.IcosahedronMath as icm
# from icosalattice.GeneratePointCodes import get_random_point_code



if __name__ == "__main__":
    n_points = 100000
    pcs = []
    for i in range(n_points):
        p = UnitSpherePoint.random()
        xyz = p.xyz()
        spc, l, d = icm.get_peel_coordinates_of_point(p)
        pc = icm.get_point_code_from_peel_coordinates(spc, l, d)
        pcs.append(pc)
    els = [random.uniform(-100, 100) for i in range(n_points)]
    d = {pc: el for pc, el in zip(pcs, els)}
    
    for pc, el in d.items():
        print(f"{pc},{el}")
