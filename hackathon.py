def getLocalWind(self,y,x):
    W = getDirSpeed(y,x)[0]
    w_to = getDirSpeed(y,x)[1]
    w_from = (w_to + 180) % 360
    return W, w_to, w_from

def getRelAngle(self,y,x,boat_dir_deg):
    raw = abs(boat_dir_deg - getLocalWind(y,x)[2])
    rel_angle = min(raw, 360 - raw)
    return rel

def checkNoGo(self,y,x,boat_dir_deg):
    if getRelAngle(y,x,boat_dir_deg) < NO_GO_ANGLE:
        return True
    else:
        return False

def getSpeedFactor(self,y,x,boat_dir_deg):
    speed_factor = polarFactor(getRelAngle(y,x,boat_dir_deg))
    return speed_factor

def polarFactor(self,rel_deg):
    if rel_deg >= 30 and rel_deg < 60:
        f = 1.0
    elif rel_deg >= 60 and rel_deg < 90:
        f = 0.95
    elif rel_deg >= 90 and rel_deg < 135:
        f = 0.85
    elif rel_deg >= 135 and rel_deg <= 180:
        f = 0.70
    else:
        f = 0
    return f
    
