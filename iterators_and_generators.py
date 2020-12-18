
print('Task 1 - Write a generator which computes the running average.')
def moving_average():
    points = []
    while True:
        if not points:
            mov_avg = 0
        else:
            mov_avg = sum(points) / len(points)
        input_point = yield mov_avg
        points.append(input_point)


rabbit_run = moving_average()
next(rabbit_run)
for n in (100, 200, 160):
    report = f"new point: {n} - moving average: {rabbit_run.send(n)}"
    print(report)
print(f"End of task 1.\n")
