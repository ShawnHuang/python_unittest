#try:
#    import rstr
#except ImportError as e:
#    print "rstr not found, please try `pip install rstr` to install."
#    exit(1)
#foo = rstr.digits(12)
#bar = rstr.xeger(r'[A-Z]\d[A-Z] \d[A-Z]\d')
#print foo
#print bar

import unittest
from package.tests.client import ClientTestCase

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ClientTestCase('test_get_google'))
    suite.addTest(ClientTestCase('test_patch_google'))
    unittest.TextTestRunner(verbosity=2).run(suite)
