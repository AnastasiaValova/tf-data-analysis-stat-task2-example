import pandas as pd
import numpy as np
import math

chat_id = 225497605 # Ваш chat ID, не меняйте название переменной 

def solution(p: float, x: np.array) -> tuple:
    t = 98
    alpha = 1 - p
    min = x.min()
    
    z_1 = -math.log(1-alpha)/len(x)
    z_2 = -math.log(1-p)/len(x)
    
    return (z_1+min-1/2)*2/(t*t), \
           (z_2+min-1/2)*2/(t*t)
