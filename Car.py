def car(manufacturer,model,*color):
    
    
    """Display information about a car"""
    
    information = {"manufacturer":manufacturer,"model":model,"features":color}
    print(f"\nCar Information:\n{information}")
    return information
info = car("BMW","BMW-x6","color-RED","speed-MAX:180")
info = car("Audi","Audi-a7","color-BLACK","speed-MAX:160")
info = car("Honda","CR-v","color-BLUE","speed-MAX:150")
print(info)

