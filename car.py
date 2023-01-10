def is_Korea_car(car):
    Korea_cars = ['КИА', 'Hyundai', 'Genesis', 'Daewoo']
    if car in Korea_cars:
        return 'Да, это корейская машина'


print(is_Korea_car('КИА'))