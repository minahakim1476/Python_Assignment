steps_input = input("enter the number of steps(separated by spaces): ")
steps = list(map(int,steps_input.split()))

highest = max(steps)
lowest = min(steps)
size = len(steps)
total = sum(steps)

avg = total / size
steps_sorted = sorted(steps , reverse=True)
print("the highest number of steps is: ", highest)
print("the lowest number of steps is: ", lowest)
print("the average number of steps is: ", avg)
print("the sorted steps in descending order are: ", steps_sorted)