import numpy as np
import matplotlib

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
        xx = np.linspace(0,100,101)
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
        xx = np.linspace(0,100,101)
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
    
    def payoff(self):
        return np.linspace(0,100,101)

c_long = CallOption(position='long')
c_short = CallOption(position='short')

p_long = PutOption(position='long')
p_short = PutOption(position='long')

print(p_long.payoff())
