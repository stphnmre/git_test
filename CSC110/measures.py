def feet_to_inches(feet):
    x=feet*12
    return round(x)

def feet_to_meters(feet):
    x=feet/3.281
    return round(x,2)

def main():
    print( feet_to_inches(1) ) # 12
    print( feet_to_inches(2.5) ) # 30
    print( feet_to_inches(5.4) ) # 65
    print( feet_to_meters(1) ) # 0.3
    print( feet_to_meters(5) ) # 1.52
    print( feet_to_meters(20) ) # 6.1

main()


