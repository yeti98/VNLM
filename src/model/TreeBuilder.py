import random

from src.model.Tree import Tree


class TreeBuilder():
    def __init__(self, probabilities, labels):
        self.tree = Tree(keys=self.create_keys(probabilities), labels=labels)

    def random_label(self):
        rd_01 = random.random()
        return self.tree.get_label(rd_01)

    def create_keys(self, probabilities):
        keys_list = []
        cur_prob = 0.0
        for prob in probabilities:
            new_key = (cur_prob, cur_prob+prob)
            cur_prob += prob
            keys_list.append(new_key)
        return keys_list