# es2sy: Esha Saigal
#tr2bx : Tianze Ren
Pi = 3.14
def surface_area(r,h):
    surfacearea = (2 * Pi * r * h) + ((2*Pi) * (r**2))
    return surfacearea
#this function calculates the surface area

def volume(r,h):
    cylvolume = (Pi * (r **2) *h)
    return cylvolume
#this function calculates the cylinder's volume

def lateral_area(r,h):
    lateralarea = 2 * Pi * r * h
    return lateralarea

#this function calculates the cylinder's lateral area

def base_area(r,h):
    basearea = Pi * (r**2)
    return basearea

#this function calculates the cylinder's base area

def print_cylinder (r,h):
    print("Radius :3")
    print("Height : 4")
    print ("Surface area: " + str(surface_area(3,4)))
    print ("Volume: " + str(volume(3,4)))
    print ("Lateral area: " + str(lateral_area(3,4)))
    print ("Base area : " + str(base_area(3,4)))

print_cylinder(3,4)

