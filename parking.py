from random import choice

# Assume that 50/50 chance that soneone will leave or enter a spot
# Assume that a car will leave from a random spot, or enter into a random open spot.
# The configurations that returns us to normal is the following
# [None, None, None, None, None]
# [None, None, None, None, X]
# [X, None, None, None, None]
# [X, None, None, None, X]
# The assumption is that if there is space, a car will park comfortably over parking tightly.
# And cars will always attempt to fit into a tight space.

winning_configurations = [[0, 1, 2, 3, 4], [0, 1, 2, 3], [1, 2, 3, 4], [1, 2 ,3]]

def check_configurations(free_spots):
    if free_spots in winning_configurations:
        return False
    return True

def free_spots(cars):
    free_spots = [idx for idx, i in enumerate(cars) if i is None]
    return free_spots

def taken_spots(cars):
    taken = [idx for idx, i in enumerate(cars) if i is not None]
    return taken

def car_leave(cars):
    if choice([True, False]):
        taken = taken_spots(cars)
        if taken:
            car_idx = choice(taken)
            cars[car_idx] = None
    return cars

def car_arrived(cars):
    if choice([True, False]):
        free = free_spots(cars)
        if free:
            car_idx = choice(free)
            cars[car_idx] = current_idx
    return cars

def run_simulation(cars, current_idx):
    while(check_configurations(free_spots(cars))):
        current_idx += 1
        cars = car_leave(cars)
        if not check_configurations(free_spots(cars)):
            break
        cars = car_arrived(cars)
    return cars, current_idx



cars_transitioning = []
for i in range(1000):
    # Nones are empty spaces
    print(i)
    cars = [1, 2, 3, 4, 5]
    current_idx = 5
    final_configuration, current_idx = run_simulation(cars, current_idx)
    cars_transitioning.append(current_idx)
print(cars_transitioning)
print(sum(cars_transitioning)/len(cars_transitioning))


