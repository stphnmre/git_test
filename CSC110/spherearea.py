def sphere_area(radius):
    area=4*3.1415*radius**2
    return round(area,2)

def sphere_volume(radius):
    volume=round((1/3)*sphere_area(radius)*radius,2)
    return volume

def main():
    print(sphere_area(.75))
    print(sphere_volume(.75))

main()