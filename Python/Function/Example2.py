def calculate_area(dimension1,dimension2,shape="triangle"):
    '''
    :param dimension1: In case of triangle it is "base". For rectangle it is "length".
    :param dimension2: In case of triangle it is "height". For rectangle it is "width".
    :param shape: Either "triangle" or "rectangle"
    :return: Area of a shape
    '''
    if shape=="triangle":
        area=1/2*(dimension1*dimension2) # Triangle area is : 1/2(Base*Height)
    elif shape=="rectangle":
        area=dimension1*dimension2 # Rectangle area is: Length*Width
    else:
        print("Error: Input shape is neither triangle nor rectangle.")
        area=None # If user didn't supply "triangle" or "rectangle" as shape then return None
    return area

base=10
height=5
triangle_area=calculate_area(base,height,"triangle")
print("Area of triangle is:",triangle_area)


length=20
width=30
rectangle_area=calculate_area(length,width,"rectangle")
print("Area of rectangle is:",rectangle_area)


