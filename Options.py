import numpy as np
import matplotlib.pyplot as plt

class Option():
    def __init__(self, K=60, position='long', value_range=100):
        self.exercise = K
        self.value_range = value_range
        assert position.lower() in ['long','short'], "You're in either long or short position."
        self.position = position.lower()
        
class CallOption(Option):
    def __init__(self, K=60, position='long', value_range=100):
        super().__init__(K=K, position=position, value_range=value_range) 
        
    def payoff(self):
        xx = np.linspace(0,self.value_range,self.value_range+1)
        if self.position == 'long':
            xx[xx < self.exercise] = 0
            xx[xx >= self.exercise] = xx[xx >= self.exercise] - self.exercise
        else:
            xx[xx < self.exercise] = 0
            xx[xx >= self.exercise] = self.exercise - xx[xx >= self.exercise]
            
        return xx

class PutOption(Option):
    def __init__(self, K=60, position='long', value_range=100):
        super().__init__(K=K, position=position, value_range=value_range) 
    
    def payoff(self):
        xx = np.linspace(0,self.value_range,self.value_range+1)
        if self.position == 'long':
            xx[xx <= self.exercise] = self.exercise - xx[xx <= self.exercise]
            xx[xx > self.exercise] = 0
        else:
            xx[xx <= self.exercise] = xx[xx <= self.exercise] - self.exercise
            xx[xx > self.exercise] = 0
            
        return xx

class Asset():
    def __init__(self, position='long', value_range=100):
        assert position.lower() in ['long','short'], "You're in either long or short position."
        self.position = position.lower()
        self.value_range = value_range
    
    def payoff(self):
        xx = np.linspace(0, self.value_range, self.value_range+1)
        if self.position == 'long':
            return xx
        else:
            return -xx

class Debt():
    def __init__(self,K=40, position='long', value_range=100):
        self.debt = K
        assert position.lower() in ['long','short'], "You're in either long or short position."
        self.position = position.lower()
        self.value_range = value_range
    
    def payoff(self):
        xx = np.ones(self.value_range)*self.debt
        if self.position == 'long':
            return xx
        else:
            return -xx

c_long = CallOption(position='long')
c_short = CallOption(position='short')

p_long = PutOption(position='long')
p_short = PutOption(position='short')

asset_long = Asset(position='long')
asset_short = Asset(position='short')

debt_long = Debt(position='long')
debt_short = Debt(position='short')

lst = [c_long, c_short, p_long, p_short, asset_long, asset_short, debt_long, debt_short]
for obj in lst:
    print(obj.payoff())
    print()