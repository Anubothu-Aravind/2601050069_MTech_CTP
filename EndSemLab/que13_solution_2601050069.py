import time
import tracemalloc

N = 1_000_000
threshold = 75

#list based
def list_based(marks):
    return [mark for mark in marks if mark > threshold]

def generator_based(marks):
    for mark in marks:
        if mark > threshold:
            yield mark

marks = [i % 101 for i in range(N)]

tracemalloc.start()
start_time = time.perf_counter()

list_result = list_based(marks)

list_time = time.perf_counter() - start_time
current, list_peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

tracemalloc.start()
start_time = time.perf_counter()

generator_result = generator_based(marks)
generator_count = sum(1 for _ in generator_result)

generator_time = time.perf_counter() - start_time
current, generator_peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

list_count = len(list_result)

print("\nList-based processing:")
print("Number of elements processed:", list_count)
print("Execution time: {:.6f} seconds".format(list_time))
print("Peak additional memory: {:.2f} MB".format(
    list_peak_memory / (1024 * 1024)
))

print("\nGenerator-based processing:")
print("Number of elements processed:", generator_count)
print("Execution time: {:.6f} seconds".format(generator_time))
print("Peak additional memory: {:.2f} MB".format(
    generator_peak_memory / (1024 * 1024)
))
