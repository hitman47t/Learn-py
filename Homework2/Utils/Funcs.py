def getSpeed(time, distance):
    try:
        return distance/time
    except ZeroDivisionError:
        return None