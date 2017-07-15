import math
import itertools
import matplotlib.pyplot as plt

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

def chase(dt, s, relerr):
    i = 0
    for p1, p2 in steps(dt, s):
        yield (i * dt, p1, p2)
        i += 1
        if abs(p1[0] - p2[0]) < relerr * p2[0]:
            break

def plotdy(dt, s, relerr):
    ts, dys = [], []
    for t, p1, p2 in chase(dt, s, relerr):
        ts.append(t)
        dys.append(p2[1] - p1[1])
    plt.plot(ts, dys)
    plt.ylabel("dy")
    plt.xlabel("t")
    plt.show()

def plot(dt, s, relerr):
    p1s, p2s = [], []
    for _, p1, p2 in chase(dt, s, relerr):
        p1s.append(p1)
        p2s.append(p2)
    plt.plot([p[0] for p in p1s], [p[1] for p in p1s],
              marker='x', markevery=int(1.0/dt))
    plt.plot([p[0] for p in p2s], [p[1] for p in p2s])
    plt.title('Pursuit Curve for 7/7/17 Riddler Express')
    summary = 'at {0:.3f} s, predator ({1:.3f}, {2:.3f}), prey ({3:.3f}, {4:.3f})'
    plt.xlabel(summary.format(len(p1s) * dt,
                              p1s[-1][0], p1s[-1][1],
                              p2s[-1][0], p2s[-1][1]))
    plt.show()
