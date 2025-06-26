import unittest
import networkx as nx
import numpy as np
import pandas as pd
from algorithms.alphacore import alphaCore

class TestAlphaCore(unittest.TestCase):
    def setUp(self):
        # Set random seed for reproducibility
        np.random.seed(1)
        
    def test_default_parameters(self):
        """Test with default parameters (200-node graph)"""
        g = nx.erdos_renyi_graph(200, 2/200, directed=True, seed=1)
        # Add edge weights
        for idx, (u, v, w) in enumerate(g.edges(data=True)):
            w['value'] = idx
        
        # Run alphaCore
        result = alphaCore(g)
        
        # Check output structure
        self.assertIsInstance(result, pd.DataFrame)
        self.assertEqual(list(result.columns), ['nodeID', 'alpha', 'batchID'])
        self.assertEqual(len(result), 200)
        self.assertTrue(all((result['alpha'] >= 0) & (result['alpha'] <= 1)))
        self.assertTrue(all(result['batchID'] >= 0))
        
        print(result.head())
        print(result.tail())

if __name__ == '__main__':
    unittest.main()