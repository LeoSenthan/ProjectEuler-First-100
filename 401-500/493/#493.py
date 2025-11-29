def probability_of_color_in_20_picks(total_balls, balls_per_color, picks):
    probability_not_picking_color = ((total_balls - balls_per_color) / total_balls) ** picks
    probability_picking_color = 1 - probability_not_picking_color
    return probability_picking_color

def expected_number_of_distinct_colors(total_balls, balls_per_color, picks, num_colors):
    expected_distinct_colors = sum(probability_of_color_in_20_picks(total_balls, balls_per_color, picks) for _ in range(num_colors))
    return expected_distinct_colors
print(expected_number_of_distinct_colors(70, 10, 20, 7))

#Probability Not Picked = 1 - 60Choose20/70choose20
#7*(1 - 60Choose20/70choose20)
from math import factorial
def choose(a,b):
    return(factorial(a)/((factorial(b)*factorial(a-b))))
print(7*(1-choose(60,20)/choose(70,20)))