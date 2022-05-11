import math
import numpy as np

class Donut:
    def __init__(self,Coordinates, radiusMin, radiusMaj):
        self._Coordinates = Coordinates
        self._radiusMin = radiusMin
        self._radiusMaj = radiusMaj
        self._K1 = 7.5
        self._K2 = 5
    
    def PointProjected(self, theta, phi, Pitch, Roll):
        temp = self._radiusMaj + self._radiusMin*np.sin(theta)
        cosB = np.cos(Pitch)
        sinB = np.sin(Pitch)
        cosA = np.cos(Roll)
        sinA = np.sin(Roll)
        sinPhi = np.sin(phi)
        cosPhi = np.cos(phi)
        sinTheta = np.sin(theta)
        cosTheta = np.cos(theta)
        x = temp*(cosB*cosPhi + sinA*sinB*sinPhi) - self._radiusMin*cosA*sinB*sinTheta
        y = temp*(cosPhi*sinB - cosB*sinA*sinPhi) + self._radiusMin*cosA*sinB*sinTheta
        z = cosA*temp*sinPhi + self._radiusMin*sinA*sinTheta

        Luminance = cosPhi*cosTheta*sinB - cosA*cosTheta*sinPhi - sinA*sinTheta + cosB*(cosA*sinTheta - cosTheta*sinA*sinPhi)
        ooz = 1/z
        xdash = int(50 + self._K1*ooz*x)
        ydash = int(50 + self._K1*ooz*y)
        Luminance *= 8
        return (xdash,ydash,int(Luminance))

    def __str__(self):
        phiSpacing = 0.02
        thetaSpacing = 0.07
        output = np.ndarray(shape=(100,100))
        for phi in [x*phiSpacing for x in range(157)]:
            for theta in [x*thetaSpacing for x in range(45)]:
                val = self.PointProjected(phi,theta,0,1)
                try:
                    output[val[0],val[1]] = ".,-~:;=!*#$@"[val[2]]
                except:
                    pass
        return output

obj = Donut(None,1,2)
                    
print(obj)
    
