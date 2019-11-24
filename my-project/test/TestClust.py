import unittest
import numpy as np
from citybike.CityBike import *

class testClust (unittest.TestCase):

    """
    Simple test case
    
    """
    
    def test_preprocessing(self):
        """ Test that the preprocessing works fine
            It removes all the non relevant values
        """
    
        mycluster = Clust("Brisbane_CityBike.json")
        res = mycluster.dataPreprocessing()
        self.assertEqual(res.count(), 143)
    
    def test_Kmeans(self):
        """ Check the average cost of the model"""
        mycluster = Clust("Brisbane_CityBike.json")
        avgCost = mycluster.Kmeans(mycluster.dataPreprocessing())
        self.assertEqual(round(avgCost,4),0.005)
        
        

        

if __name__ == '__main__':
    unittest.main()