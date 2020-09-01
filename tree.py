import os
import hashlib
import pickle

from graphviz import Digraph
from IPython.display import display, Image
from graphviz import Digraph


class paper_tree:

    def __init__( self, root_val = None, children = list()):
        self.root_val = root_val
        self.children = children
        
    def add_child( self, sub_tree, reason):
        if self.root_val: 
            self.children.append( [reason, sub_tree])
        else:
            raise Exception( "Unable to add children, due to root's value is None")
    
    def to_dict( self):
        if len( self.children):
            def preorder( root):
                sub_dict = dict()
                if root: 
                    subsub_dict = dict()
                    sub_dict[ root.root_val] = subsub_dict
                    for child in root.children:
                        reason, sub_tree = child
                        if len( sub_tree.children):
                            subsub_dict[ reason] = preorder( sub_tree)
                        else: 
                            subsub_dict[ reason] = sub_tree.root_val
                return sub_dict
            return preorder( self)
        else: 
            return self.root_val
        
    def visualize_tree(self, name):
        self.root_idx = '0'
        tree = self.to_dict( )
        g = Digraph( "G", filename=name, format='pdf', strict=False)
        root_label = list( tree.keys())[0]
        g.attr('node', shape='box')
        g.node("0", root_label)
        self._sub_plot(g, tree, "0")
        g.view()

    def _sub_plot( self, g, tree, parent_idx):
        root_label = list(tree.keys())[0]
        sub_tree = tree[root_label]
        for reason in sub_tree.keys():
            if isinstance( tree[root_label][ reason], dict):
                self.root_idx = str(int( self.root_idx) + 1)
                g.node(self.root_idx, list( tree[ root_label][reason].keys())[0])
                g.edge(parent_idx, self.root_idx, reason)
                self._sub_plot(g, tree[root_label][ reason], self.root_idx)
            else:
                self.root_idx = str(int( self.root_idx) + 1)
                g.node(self.root_idx, tree[ root_label][ reason])
                g.edge( parent_idx, self.root_idx, reason)

if __name__ == '__main__':

    P4f94fe08cc3662adf220254e197e706a735c003b = paper_tree( root_val = 
    "2011 Daw Model-based influences on humans choice and striatal prediction errors", children = list())
    Pbfa4ac610dffaab0b654d0f8c50dd4807d27c0df = paper_tree( root_val = 
    "2016 Kool When does model-based control pay off", children = list())
    P16502e2c487ac9a9b8a76a54eddeb92c5313f9b9 = paper_tree( root_val = 
    "2017 Wang Learning to reinforcement learn", children = list())
    Pecfabbb91cc2b6efa499390b3c6a1fa93e0f482b = paper_tree( root_val = 
    "2019 Ritter Meta-reinforcement learning with episodic recall", children = list())

    P4f94fe08cc3662adf220254e197e706a735c003b.add_child( sub_tree = 
    Pbfa4ac610dffaab0b654d0f8c50dd4807d27c0df, reason = 'improve experiment')

    P4f94fe08cc3662adf220254e197e706a735c003b.add_child( sub_tree = 
    P16502e2c487ac9a9b8a76a54eddeb92c5313f9b9 , reason = 'add lstm')

    P16502e2c487ac9a9b8a76a54eddeb92c5313f9b9.add_child( sub_tree = 
    Pecfabbb91cc2b6efa499390b3c6a1fa93e0f482b, reason = 'add episodic control')

    P4f94fe08cc3662adf220254e197e706a735c003b.visualize_tree( 'plots/2012')

    with open('my_trees/episodic.pickle', 'wb') as handle:
        pickle.dump(P4f94fe08cc3662adf220254e197e706a735c003b, handle)