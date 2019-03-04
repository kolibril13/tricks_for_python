import timeit
# Print the execution time
print(timeit.timeit('[n**2 for n in range(10) if n%2==0]', number=10000))
