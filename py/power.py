import time

def stopwatch():
    start = time.time()
    time.perf_counter()   

    elapsed = 0
    powerConsumPtion = 369   # watts
    kilowattsPerHour = 14   # cents
    totalCost = 0

    while True:
        elapsed = time.time() - start
        mod = elapsed % 60
        minutesToHours = elapsed/60
        energy = (powerConsumPtion * minutesToHours)/1000
        totalCost = (energy*kilowattsPerHour)/100
        if round(mod) == 0:
            print ("Minutes up: %02d" % (elapsed/60))
            print("Electricity Cost: ",totalCost/100)
        time.sleep(1)  
        

    

    

stopwatch()