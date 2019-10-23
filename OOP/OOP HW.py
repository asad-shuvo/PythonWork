class Line():
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    def distannce(self):
        y=(coor2[0]-coor1[0])**2+(coor2[1]-coor1[1])**2
        y=y**.5
        return y
    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])

coor1=(3,2)
coor2=(8,10)
line1=Line(coor1,coor2)
print(line1.slope())
print(line1.distannce())


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height=height
        self.radius=radius

    def volume(self):
        return 3.14*self.radius**2*self.height
        #v=pi*r**2*H


    def surface_area(self):
        return 2*3.14*self.radius*self.height+2*3.14*self.radius**2

c=Cylinder(2,3)
print(c.volume())
print(c.surface_area())