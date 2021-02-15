import numpy as np
import random
from scipy.integrate import odeint

class DoublePendulum(object):
  # code based on:  
  def __init__(self, m1, m2, l1, l2, g, initial_state, origin=(0,0)):
    self.m1 = m1
    self.m2 = m2
    self.l1 = l1
    self.l2 = l2
    self.g = g
    self.origin = origin 

 
    if initial_state == "random":
      self.theta1 = random.uniform(-2*np.pi, 2*np.pi)
      self.theta2 = random.uniform(-2*np.pi, 2*np.pi)
    else:
      self.theta1 = initial_state[0]
      self.theta2 = initial_state[1]

    self.v1 = 0
    self.v2 = 0

    self._setup()

  def _setup(self):
    self.x1 = self.l1*np.sin(self.theta1) + self.origin[0]
    self.y1 = -self.l1*np.cos(self.theta1) + self.origin[1]

    self.x2 = self.x1 + self.l1*np.sin(self.theta2)
    self.y2 = self.y1 - self.l1*np.cos(self.theta2)

  def derive(self, u, t):
    ret = np.zeros(4)

    c = np.cos(u[0] - u[2])
    s = np.sin(u[0] - u[2])
  
    ret[0] = u[1]
    ret[1] = (self.m2*self.g*np.sin(u[2])*c - self.m2*s*(self.l1*c*u[1]**2 + self.l2*u[3]**2) - (self.m1+self.m2)*self.g*np.sin(u[0]) )/(self.l1*(self.m1+self.m2*s**2))
    ret[2] = u[3]
    ret[3] = ((self.m1+self.m2)*(self.l1*u[1]**2*s - self.g*np.sin(u[2]) + self.g*np.sin(u[0])*c) + self.m2*self.l2*u[3]**2*s*c)/(self.l2*(self.m1+self.m2*s**2))

    return ret

  def trajectory(self, u0, time):
    sol = odeint(self.derive, u0, time)

    self.theta1 = sol[:, 0]
    self.theta2 = sol[:, 2]
    
    self._setup()



if __name__ == "__main__":
  dp = DoublePendulum(1,1,1,1,9.81, "random")
  dp.trajectory([dp.theta1, 0, dp.theta2, 0], np.linspace(0,30,700))
  print(dp.x1)  
   
