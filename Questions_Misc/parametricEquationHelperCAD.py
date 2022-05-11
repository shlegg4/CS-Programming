import math

class Point:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y

def Polarize(p1 : Point, p2 : Point):
    dx = abs(p1.x - p2.x)
    dy = abs(p1.y - p2.y)
    dist = (dx**2 + dy**2)**0.5
    angle = math.atan(dy/dx)
    angle = angle*(180/math.pi)
    print("Distance : {0} , Angle : {1}".format(dist,angle))





points = []
start = 0
stop = 1
step = 0.1
points.append(Point(0,0))
for t in range(int(start*1/step),int(stop*1/step),1):
    t = step*t
    xValue = 30.3161 * (math.cos(0.9020 * t) + 0.9020 * t * math.sin(0.9020 * t))
    yValue = 30.3161 * (math.sin(0.9020 * t) - 0.9020 * t * math.cos(0.9020 * t))
    points.append(Point(xValue,yValue))


for i in range(len(points)-1):
    p1 = points[i]
    p2 = points[i+1]
    Polarize(p1,p2)