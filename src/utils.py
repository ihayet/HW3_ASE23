import math

the = {}
o_file = None

Seed=937162211
def rint(lo, hi):
    return math.floor(0.5 + rand(lo, hi))

def setSeed(val):
  global Seed
  Seed = val

def rand(lo, hi):
  global Seed
  Seed = (16807 * Seed) % 2147483647
  return lo + (hi-lo) * Seed / 2147483647

def rnd(n, nPlaces=3):
  return round(n, nPlaces)


def getThe():
  global the 
  return the

def setThe(options):
  global the
  the = options

def get_ofile():
  global o_file
  if o_file is None:
    o_file = open('etc/out', 'w', encoding='utf-8')
    
  return o_file

def any(t):
  if t is not None:
    return t[rint(0, len(t)-1)]
  else:
    return math.inf

def many(t, sample_size):
  u = []
  for i in range(0, sample_size):
    val = any(t)
    if val is not math.inf:
      u.append(val)
  return u

def cosine(a, b, c):
  x1 = (a**2 + c**2 - b**2)/(2*c)
  x2 = max(0, min(1, x1))
  y = (a**2 - x2**2)**0.5
  return x2, y
