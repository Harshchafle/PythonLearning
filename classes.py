class Points(object):
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def print_point(self):
    print('x=',self.x,' y=',self.y)
p1=Points("A","B")
p1.print_point()

for i,x in enumerate(['A','B','C']):
    print(i,2*x)

class Points(object):
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def print_point(self):
    print('x=',self.x,' y=',self.y)
p2=Points(1,2)
p2.x='A'
p2.print_point()

def step(x):
    if x>0:
        y=1
    else:
        y=0
    return y