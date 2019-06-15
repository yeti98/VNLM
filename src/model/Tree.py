class TreeNode:
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value


class Tree:
    def __init__(self, keys, labels):
        '''
        Initial probability tree. Each node have a unique value which is a pair of prob and two child nodes.
        :param keys: list values.
        :param labels: list labels.
        '''
        self.mapper = {}
        self.root = TreeNode()
        for key, label in zip(keys, labels):
            self.insert(key, self.root)
            self.mapper[key] = label

    def insert(self, prob_pair, node):
        '''
        Insert a node to tree
        :param prob_pair: pair of two number between [0.0 ; 1.0]
        :param node: starting node when insert action activated
        :return: None
        '''
        left_value, right_value = prob_pair
        current_node = node
        while current_node.value:
            cur_left_value, cur_right_value = current_node.value
            if right_value <= cur_left_value:
                current_node = current_node.left
            elif left_value >= cur_right_value:
                current_node = current_node.right
            else:
                raise Exception("Insert Error...")
        current_node.value = prob_pair
        current_node.left = TreeNode()
        current_node.right = TreeNode()

    def get_label(self, number):
        node = self.search(number, self.root)
        return self.mapper[node.value]

    def search(self, number, root):
        current_node = root
        cur_left_value, cur_right_value = current_node.value
        while number < cur_left_value or number > cur_right_value:
            if number < cur_left_value:
                current_node = cur_left_value.left
            elif number > cur_right_value:
                current_node = current_node.right
            cur_left_value, cur_right_value = current_node.value
        return current_node
