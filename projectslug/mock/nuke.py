"""Mock Nuke module for testing purposes."""

from typing import List


class Node:
    def __init__(self, name: str):
        self.node_name = name

    def name(self) -> str:
        return f'{self.node_name}1'

    def Class(self) -> str:
        return self.node_name

    def selectOnly(self):
        pass


def allNodes() -> List[Node]:
    return [
        Node(n)
        for n in ('Merge', 'Viewer', 'Grade', 'Shuffle', 'Roto', 'Write', 'Read')
    ]


def toNode(node: str) -> Node:
    return Node(node)


def zoomToFitSelected():
    pass


def nodesSelected() -> bool:
    return True
