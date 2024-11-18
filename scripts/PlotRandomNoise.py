import random
import numpy as np
import matplotlib.pyplot as plt

from icosalattice.UnitSpherePoint import UnitSpherePoint
import icosalattice.IcosahedronMath as icm



if __name__ == "__main__":
    n_points = 100
    usps = [UnitSpherePoint.random() for i in range(n_points)]
    pcs = []
    for p in usps:
        spc, l, d = icm.get_peel_coordinates_of_point(p)
        pc = icm.get_point_code_from_peel_coordinates(spc, l, d)
        pcs.append(pc)
    els = [random.uniform(-100, 100) for i in range(n_points)]
    d = {pc: el for pc, el in zip(pcs, els)}
    print(d)
    