from joblib import Parallel, delayed
import multiprocessing
import time

start_time = time.time()

# what are your inputs, and what operation do you want to
# perform on each input. For example...

def processInput(i):
    for i in range(0, 10000):
        i += 1


N = 7000
num_cores = multiprocessing.cpu_count()
print(num_cores)
results = Parallel(n_jobs=num_cores)(delayed(processInput)(i) for i in range(N))

print( f"--- In Parallel \t {(time.time() - start_time)} seconds ---")

results2 = []

start_time = time.time()
for i in range(N):
    results2.append(processInput(i))
print(f"--- Nur ein Kern \t {(time.time() - start_time)} seconds ---")