import unittest
import TestCard
import TestDeck

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(TestCard))
suite.addTests(loader.loadTestsFromModule(TestDeck))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)