import lib.code as code
from scipy.stats import norm
import pytest


class TestModel(object):
    
    def test_price(self):
        model = code.BlackModelNormal()
        assert model.price_call(0.01,0.01,1,1) == norm.pdf(0)  
       
    def test_digital(self):
        model = code.BlackModelNormal()
        assert model.price_digital_call(0.01,0.01,1,1) == 0.5
		
    def test_delta(self):
        model = code.BlackModelNormal()
        assert model.delta(0.01,0.01,1,1) == 0.5
        