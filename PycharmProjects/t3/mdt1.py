import time
start_time = time.time()
npow = 10

# k = (n*(n+1))/2

# for k in range(0, npow+1):
# total = 0

# for exp in range(1, 11):
#     n = pow(10, exp)
#     res = (n*(n+1))/2
#     print(res)

total = 0
subtotal = 0
for exp in range(1, 11):
    n = pow(10, exp)
    for k in range(1, n + 1):
        subtotal += 1 / (k * (k + 1))
    total += subtotal

    print("N: 10^" + str(exp))
    print("subtotal: " + str(subtotal))
    print("total: "+str(total))
    print("--- %s seconds ---" % (time.time() - start_time))
    print()
