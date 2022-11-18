from collections import Counter
import matplotlib.pyplot as plt
import sys


class mc_carthy:
    sys.setrecursionlimit(10000)
    c = Counter('repts')
    
    def mc_carthy_91(self, number: int) -> int:
        mc_carthy.c['repts'] += 1

        if number > 100:
            return number - 10 
        else:
            return self.mc_carthy_91(self.mc_carthy_91(number + 11))
            
    def get_number_of_repts(self, number):
        mc_carthy.c['repts'] = 0
        self.mc_carthy_91(number)    
        return mc_carthy.c['repts']


mc = mc_carthy()

range = range(-100, 200)

plot_data = [mc.get_number_of_repts(x) for x in range]
plt.plot(range, plot_data)
plt.show()



