def probability_of_color_in_20_picks(total_balls, balls_per_color, picks):
    probability_not_picking_color = ((total_balls - balls_per_color) / total_balls) ** picks
    probability_picking_color = 1 - probability_not_picking_color
    return probability_picking_color

def expected_number_of_distinct_colors(total_balls, balls_per_color, picks, num_colors):
    expected_distinct_colors = sum(probability_of_color_in_20_picks(total_balls, balls_per_color, picks) for _ in range(num_colors))
    return expected_distinct_colors
print(expected_number_of_distinct_colors(70, 10, 20, 7))

