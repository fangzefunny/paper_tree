import pickle
from tree import paper_tree 

with open('my_trees/episodic.pickle', 'rb') as handle:
    tree = pickle.load( handle)

tree.visualize_tree( 'plots/2012')