import math
import itertools

def steps(dt, s):
  p1 = (0, 0)
  p2 = (100, 0)
  stepSize = s * dt
  while True:
    yield (p1, p2)
    deltaP = (p2[0] - p1[0], p2[1] - p1[1])
    normDeltaP = math.sqrt(deltaP[0]**2 + deltaP[1]**2)
    p1 = (p1[0] + stepSize * deltaP[0] / normDeltaP,
          p1[1] + stepSize * deltaP[1] / normDeltaP)
    p2 = (100, p2[1] + stepSize)


def chase(dt, s, err):
    for p1, p2 in steps(dt, s):
        if abs(p1[0] - p2[0]) < err:
            return (p1, p2)
