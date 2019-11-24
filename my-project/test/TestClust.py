import unittest
from citybike.CityBike import *

class testClust (unittest.TestCase):

    """
    Simple test case
    
    """
    
    def test_preprocessing(self):
    
        mycluster = Clust("Brisbane_CityBike.json")
        res = mycluster.dataPreprocessing()
        self.assertEqual(res.count(), 143)
    
    def test_Kmeans(self):
        
        mycluster = Clust("Brisbane_CityBike.json")
        res = mycluster.Kmeans(mycluster.dataPreprocessing())
        print (res.count())
        
        

        

if __name__ == '__main__':
    unittest.main()