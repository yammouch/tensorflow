import numpy as np
import tensorflow as tf
import random

class MyTrain:
  def __init__(self):
    self.rnd = random.Random()
    self.rnd.seed(0)
    self.inp = [ np.array([0., 0.], dtype=np.float32)
               , np.array([0., 1.], dtype=np.float32)
	       , np.array([1., 0.], dtype=np.float32)
	       , np.array([1., 1.], dtype=np.float32) ]
    self.exp = [ np.array([0.], dtype=np.float32)
               , np.array([1.], dtype=np.float32)
	       , np.array([1.], dtype=np.float32)
	       , np.array([0.], dtype=np.float32) ]
    self.n_subbatch = 3

  def next(self):
    idxs = map( lambda x: self.rnd.randint(0, 3)
              , range(self.n_subbatch) )
    return ( np.array(map(lambda i: self.inp[i], idxs))
           , np.array(map(lambda i: self.exp[i], idxs)) )
