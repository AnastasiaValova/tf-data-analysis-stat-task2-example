import pandas as pd
import numpy as np
import math

chat_id = 225497605 # Ваш chat ID, не меняйте название переменной 

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = x.mean()
    
    z_1 = -math.log(1-alpha)
    z_2 = -math.log(1-p)
    
    print(z_1)
    print(z_2)
    return (z_1+loc-1/2)*2/(98*98), \
           (z_2+loc-1/2)*2/(98*98)
