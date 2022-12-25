import numpy as np
import matplotlib

class Option():
    def __init__(self, K=60):
        self.exercise = K

class CallOption(Option):
    def __init__(self, K=60, position='long'):
        super().__init__(K) 
        assert position.lower() in ['long','short'], "You're in either long or short position."
        self.position = position.lower()
    
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
    def __init__(self, K=60, position='long'):
        super().__init__(K)
        assert position.lower() in ['long','short'], "You're in either long or short position."
        self.position = position.lower()
    
    def payoff(self):
        xx = np.linspace(0,100,101)
        if self.position == 'long':
            xx[xx <= self.exercise] = self.exercise - xx[xx <= self.exercise]
            xx[xx > self.exercise] = 0
        else:
            xx[xx <= self.exercise] = xx[xx <= self.exercise] - self.exercise
            xx[xx > self.exercise] = 0
            
        return xx

c_long = CallOption(position='long')
c_short = CallOption(position='short')

p_long = PutOption(position='long')
p_short = PutOption(position='long')

print(p_long.payoff())
