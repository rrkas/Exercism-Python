from typing import List


class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id

    def __repr__(self):
        return '{} {}'.format(self.parent_id, self.record_id)

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []

    def add_node(self, node):
        self.children.append(node)


def BuildTree(records):
    # print('\t'.join(map(str, records)))
    records.sort(key=lambda r:  r.record_id)
    # print('\t'.join(map(str, records)))
    nodes = {}
    for r_id in range(len(records)):
        r = records[r_id]
        if r_id != r.record_id or (r.record_id != 0 and r.parent_id >= r.record_id) or (r.record_id == 0 and r.parent_id != r.record_id):
            raise ValueError(' ')
        node = Node(r.record_id)
        nodes[r.record_id] = node
        if r.record_id > 0:
            p = nodes[r.parent_id]
            p.add_node(node)
    return nodes[0] if len(nodes) > 0 else None


if __name__ == '__main__':
    records = [
        Record(6, 2),
        Record(0, 0),
        Record(3, 1),
        Record(2, 0),
        Record(4, 1),
        Record(5, 2),
        Record(1, 0)
    ]
    BuildTree(records)