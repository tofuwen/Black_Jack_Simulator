import unittest
import TestCard
import TestDeck
import TestBoard

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(TestCard))
suite.addTests(loader.loadTestsFromModule(TestDeck))
suite.addTests(loader.loadTestsFromModule(TestBoard))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
