import numpy as np
import matplotlib.pyplot as plt

class Option():
    def __init__(self, K, position, value_range):
        self.exercise = K
        self.value_range = value_range
        assert position.lower() in ['long','short'], "You're in either long or short position."
        self.position = position.lower()
        
class CallOption(Option):
    def __init__(self, K, position, value_range=100):
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
    def __init__(self, K, position, value_range=100):
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
    def __init__(self, position, value_range=100):
        assert position.lower() in ['long','short'], "You're in either long or short position."
        self.position = position.lower()
        self.value_range = value_range
    
    def payoff(self):
        xx = np.linspace(0, self.value_range, self.value_range+1)
        if self.position == 'long':
            return xx
        else:
            return -xx

class Bond():
    def __init__(self,K, position, value_range=100):
        self.debt = K
        assert position.lower() in ['long','short'], "You're in either long or short position."
        self.position = position.lower()
        self.value_range = value_range
    
    def payoff(self):
        xx = np.ones(self.value_range+1)*self.debt
        if self.position == 'long':
            return xx
        else:
            return -xx


# Strategy (A)
call_40_long = CallOption(K=40, position='long')
bond_40_long = Bond(K=40, position='long')
xx = np.linspace(0,100,101)

plt.figure(figsize=(11,9))
plt.title("(A) Payoff at option expiration", fontdict={'size':22})
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_position(('data',0))

plt.plot(xx, call_40_long.payoff()+0.2, 'r--')
plt.plot(xx, bond_40_long.payoff(), 'b--')
plt.plot(xx, call_40_long.payoff()+40.3, 'k')

plt.xlim([0,100])
plt.ylim([-10,80])
plt.xticks([])
plt.yticks([])

plt.text(40, -4, "K", fontdict={'size':20})
plt.text(-4, 40, "K", fontdict={'size':20})
plt.savefig("Strategy (A).png")


# Strategy (B)
put_40_long = PutOption(K=40, position='long')
asset_long = Asset(position='long')
xx = np.linspace(0,100,101)

plt.figure(figsize=(11,9))
plt.title("(B) Payoff at option expiration", fontdict={'size':22})
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_position(('data',0))

plt.plot(xx, put_40_long.payoff()+0.2, 'r--')
plt.plot(xx, asset_long.payoff(), 'b--')
plt.plot(xx, call_40_long.payoff()+40.3, 'k')

plt.xlim([0,100])
plt.ylim([-10,80])
plt.xticks([])
plt.yticks([])

plt.text(40, -4, "K", fontdict={'size':20})
plt.text(-4, 40, "K", fontdict={'size':20})
plt.savefig("Strategy (B).png")