from math import log
max_iterations,current_value,count,previous_value = 100000000,90,0,0

lower_bound =log(1.23, 10)
upper_bound =log(1.24, 10)

def calculate_difference(current_value):
    log_value = log(2, 10) * current_value
    difference = (log_value - int(log_value))
    return difference

while(count < 678910):
    difference = calculate_difference(current_value)
    if difference >= upper_bound:
        current_value += 93
    elif difference < lower_bound:
        current_value += 196
    else:
        count += 1
        previous_value = current_value
        current_value += 196
#Increments by either 289,196 or 485 which is basically increment by 196 or 196+93 or 196+196+93
print(previous_value)
