
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


print(f"Task 2 - Write a generator frange, which behaves like range but accepts float values.")
def frange(start=None, stop=None, step=1):

    assert stop is not None
    assert isinstance(stop, (float, int,))
    if start:
        assert isinstance(start, (float, int,))
    if step != 1:
        assert start or start == 0
    assert isinstance(step, (float, int,))
    assert step != 0

    if step > 0:
        if not start:
            assert stop > 0
            start = 0
            while start < stop:
                yield start
                start += step
        elif start:
            assert start < stop
            while start < stop:
                yield start
                start += step
    else:
        assert stop > start
        while stop > start:
            yield stop
            stop += step


# gen = frange(stop=5)
# gen = frange(start=-5)
# gen = frange(start=0)
# gen = frange(start=1)
# gen = frange(start=0, stop=1)
# gen = frange(start=0, stop=1, step=-1)
# gen = frange(start=0, stop=1, step=2)
# gen = frange(start=0, stop=5, step=1)
# gen = frange(start=0, stop=5, step=2)
# gen = frange(start=5, stop=1, step=2)
# gen = frange(start=5, stop=1, step=-1)
# gen = frange(start=0, stop=5, step=-1)
# gen = frange(start=-3, stop=5, step=-1)
# gen = frange(start=-3, stop=5, step=1)
# gen = frange(start=-3, stop=5, step=1)

# gen = frange(stop=5.5)
# gen = frange(start=0, stop=5, step=1.1)
# gen = frange(start=0, stop=5, step=-1.1)
# gen = frange(start=0.1, stop=5)
# gen = frange(start=0.1, stop=5, step=0.05)
# gen = frange(start=0.1, stop=5, step=0.05)
# gen = frange(start=0.1, stop=5, step=-0.05)
# gen = frange(start=0.1, stop=5, step=-0.05)

gen = frange(start=-3.6, stop=1.5, step=-0.5)

try:
    while True:
        print(next(gen))
except StopIteration:
    print('Generator is exhausted.')

print(f"End of task 2.\n")