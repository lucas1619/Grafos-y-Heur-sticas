import random
import math
from PIL import Image, ImageDraw
color = 0
def azulejos():
  global color
  elevacion = int(input("Ingresa el exponente de 2: "))
  lado = 2 ** elevacion
  piso = [[0 for x in range(lado)] for x in range(lado)]
  piso[random.randint(0, lado - 1)][random.randint(0, lado - 1)] = color
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
  divide(0, lado - 1, 0, lado - 1)
  colores = []
  for x in range(color):
    colores.append({
        'red': random.randint(0, 255),
        'green' : random.randint(0, 255),
        'blue' : random.randint(0, 255)
    })
  tam = int(input("inserta el tamaño de los cuadrados: "))    
  im = Image.new('RGB', (tam*lado, tam*lado), (128, 128, 128))
  draw = ImageDraw.Draw(im)
  for x, a in enumerate(piso):
    for y, b in enumerate(a):
      draw.rectangle((x*tam, y*tam,tam*(x + 1), tam*(y + 1)), fill=(colores[b - 1]['red'], colores[b - 1]['green'], colores[b - 1]['blue']), outline=(colores[b - 1]['red'], colores[b - 1]['green'], colores[b - 1]['blue']))
  name = input("Ingresa el nombre que le pondras a tu imagen:")
  im.save(f'{name}.jpg', quality=95)      
azulejos()