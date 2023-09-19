x = float(input())
y = float(input())
h = float(input())

door = 1.2 * 2
windows = (1.5 * 1.5) * 2
back_and_front_walls_sqm = (x * x) * 2 - door
side_walls_sqm = (x * y) * 2 - windows
roof_sqm = (2 * (x * y)) + (2 * (1/2 * x * h))
green_paint_liters = (back_and_front_walls_sqm + side_walls_sqm) / 3.4
red_paint_liters = roof_sqm / 4.3
print("%.2f" % green_paint_liters)
print("%.2f" % red_paint_liters)