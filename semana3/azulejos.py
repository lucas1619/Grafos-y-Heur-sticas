import random
import math
color = 0
def azulejos():
  global color
  piso = [[0 for x in range(8)] for x in range(8)]
  piso[random.randint(0, 7)][random.randint(0, 7)] = color
  def tieneColor(xo, xn, yo, yn):
    for y in range(yo, yn+1):
      for x in range(xo, xn + 1):
        if piso[x][y] > 0:
          return True
    return False      
  def divide(xo, xn, yo, yn):
    if xn == xo and yn == yo:
      return
    global color
    infxn = math.trunc((xo + xn)/2)
    infyn = math.trunc((yo + yn)/2)
    supxn = infxn + 1
    supyn = infyn + 1
    color += 1
    if tieneColor(xo, infxn, yo, infyn) == False:
      piso[infxn][infyn] = color
    if tieneColor(supxn, xn, yo, infyn) == False:
      piso[supxn][infyn] = color
    if tieneColor(xo, infxn, supyn, yn) == False:
      piso[infxn][supyn] = color
    if tieneColor(supxn, xn, supyn, yn) == False:
      piso[supxn][supyn] = color
    divide(xo, infxn, yo, infyn)
    divide(supxn, xn, yo, infyn)
    divide(xo, infxn, supyn, yn)
    divide(supxn, xn, supyn, yn)
  divide(0, 7, 0, 7)
  for x in piso:
    for y in x:
      print(f'{y}\t', end="")
    print('')      
azulejos()