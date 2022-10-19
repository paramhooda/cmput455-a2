import time

seconds = time.time()
while (time.time()-seconds)<1:
    print("Time in seconds since the epoch:", time.time()-seconds)
