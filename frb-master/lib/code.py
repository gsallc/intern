import math
from scipy.stats import norm

class BlackModelNormal:
       
    def price_call(self,fwd,K,modVol,T):
        """ Gives Price of call option
       
        >>> model = BlackModelNormal()
        >>> price = model.price_call(0.01,0.01,1,1)
        >>> print(price)
        0.3989422804014327
        """
        sigT = modVol * math.sqrt(T)
        d = (fwd - K) / sigT 
        return (fwd - K) * norm.cdf(d) + sigT * norm.pdf(d)
    
    def price_digital_call(self,fwd,K,modVol,T):
        """ Gives Price of call option
        >>> call = BlackModelNormal()
        >>> price = call.price_digital_call(0.01,0.01,1,1)
        >>> print(price)
        0.5
        """
        sigT = modVol * math.sqrt(T)
        d = (fwd - K) / sigT 
        return 1 - norm.cdf(d)
    
    def delta(self,fwd,K,modVol,T):
        """ Gives Price of call option
        >>> call = BlackModelNormal()
        >>> delta = call.delta(0.01,0.01,1,1)
        >>> print(delta)
        0.5
        """
        return -self.price_digital_call(fwd,K,modVol,T) + 1
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

