class Pos:
    def __init__(self, x,y):
        self.x = x
        self.y = y

# code convert informations
# 
# [0-9] passage+murs    code    [0-9]
# D : départ            code      100
# A : arrivée           code      101
#

def convert_data(v):
    """Converti les données textes en nombres"""
    if v=="D":
        return 100
    elif v=="A":
        return 101
    elif v=="E":
        return 3
    else:
        return int(v)