import random
random.randint(1,5)
list = ["H", "E", 1, "L", 0]
Hello = random.choice(list)
print(Hello)
weeks = 16
classes = 5
tuition = 6000
classes_per_week = 4
cost_per_week = (tuition / classes) / weeks
cost_per_class = classes_per_week/cost_per_week
print("Cost per week:", cost_per_week)
print("Here's the cost for this class!", cost_per_class)
print(weeks, type(weeks))
print(classes, type(classes))
print(tuition, type(tuition))
print(classes_per_week, type(classes_per_week))
print(cost_per_week, type(cost_per_week))
print(cost_per_class, type(cost_per_class))
