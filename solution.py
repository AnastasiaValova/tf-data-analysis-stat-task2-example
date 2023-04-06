import pandas as pd
import numpy as np

chat_id = 225497605 # Ваш chat ID, не меняйте название переменной 

def solution(p: float, x: np.array) -> tuple:
    t = 98
    alpha = 1 - p
    min = (-x).min()
   
    z_2 = -np.log(1-p)/x.size    
    
    return 2*(-min-1/2)/(t*t), 2*(z_2-min-1/2)/(t*t)
