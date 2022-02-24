from operator import indexOf


colors = ["red", "orange", "green", "yellow"]

color1 = input("Enter Color 1: ")
color2 = input("Enter Color 2: ")
color3 = input("Enter Color 3: ")
color4 = input("Enter Color 4: ")

my_colors = [color1, color2, color3, color4]

for color in colors:
    for my_color in my_colors:
        if color == my_color:
            color_index = color.index(color)
            my_color_index = my_colors.index(my_color)

            if color_index == my_color_index:
                print(f'Correct Color at place: {color_index}')
            else:
                print(f'Correct Color But Wrong Place At: {my_color_index}')
