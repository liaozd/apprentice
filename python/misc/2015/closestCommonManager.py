#!/usr/bin/env python


class Initech(object):
    
    def __init__(self, tree_dict):
        self.tree = tree_dict
        # all manager's names
        self.nodes = self.tree.keys()

    def list_all_farthers(self, node):
        # initiate it with None, so the node_fathers[-1] works in the beginning
        node_fathers = ['None']
        tmp_tree = self.tree.copy()
        # if the employee(node) is a manager, append it to the node_fathers list
        if node in tmp_tree.keys():
            node_fathers.append(node)
        # iterate over all nodes to list all farthers squentially, the closest at front.
        while node_fathers[-1] != 'BILL':
            for key in tmp_tree:
                if node in tmp_tree[key]:
                    node_fathers.append(key)
                    tmp_tree.pop(key)
                    node = key
                    break
                else:
                    continue
        return node_fathers[1:]

    def closestCommonManager(self, node1, node2):
        node1_fathers = self.list_all_farthers(node1)
        node2_fathers = self.list_all_farthers(node2)
        # return the first shared manager
        for father in node1_fathers:
            if father in node2_fathers:
                return father

if __name__ == "__main__":
    initech = Initech({
            'BILL': ['DOM', 'SAMIR', 'MICHAEL'],
            'DOM': ['BOB', 'PETER', 'PORTER'],
            'PETER': ['MILTON', 'NINA'],
        })

    print initech.closestCommonManager('MILTON', 'NINA')
    print initech.closestCommonManager('NINA', 'PORTER')
    print initech.closestCommonManager('NINA', 'SAMIR')
    print initech.closestCommonManager('PETER', 'NINA')

    print initech.closestCommonManager('BILL', 'BILL')


