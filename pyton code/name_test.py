##import unittest
##from app import get_ful_name
##
##class NameTest(unittest.TestCase):
##    def test_toliq_ism(self):
##        ddee = get_ful_name('alijon','valiyev','husanovich')
##        self.assertEqual(ddee,  'Alijon Valiyev Husanovich')
##unittest.main()





##import unittest
##from app import get_ful_name
##
##class NameTest(unittest.TestCase):
##    def test_toliq_ism(self):
##        ddee = get_ful_name('alijon','valiyev')
##        self.assertEqual(ddee,  'Alijon Valiyev')
##
##    def test_toliq_ism_otasi(self):
##        dff = get_ful_name('alijon','valiyev','husanovich')
##        self.assertEqual(dff,  'Alijon Valiyev Husanovich')
##import unittest
##from app import get_ful_name  
##
##class NameTest(unittest.TestCase):
##    def test_toliq_ism(self):
##        ddee = get_full_name('alijon', 'valiyev')
##        self.assertEqual(ddee, 'Alijon Valiyev')
##
##    def test_toliq_ism_otasi(self):
##        dff = get_full_name('alijon', 'valiyev', 'husanovich')
##        self.assertEqual(dff, 'Alijon Valiyev Husanovich')
##unittest.main()
##
##import unittest
##from app import son,sonn
##class Sontest(unittest.TestCase):
##    def test_son(self):
##        self.assertAlmostEqual(son(3,7,15), 15)
##    def test_min_son(self) :
##        self.assertAlmostEqual(sonn(2,8,6), 2)
##        
##        
##unittest.main()

import unittest
from app import juft
class Jufttest(unittest.TestCase):
    def tes_juft(self):
        dff = get_full_name(45,44,66,67,84,25,75,55)
        self.assertEqual(dff,  44, 66, 84)

unittest.main()
        





















