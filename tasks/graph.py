from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root
    
    def dfs(self) -> list[Node]:

        result: list = []
        vizited: list = []
        pointer: Node = self._root

        def _sub_dfs(pointer):

            if pointer not in result:
                result.append(pointer)
                vizited.append(pointer)

            if pointer.outbound:
                for node in pointer.outbound:
                    if node not in vizited:
                        pointer = node
                        _sub_dfs(node)
            return result

        return _sub_dfs(pointer)

    def bfs(self) -> list[Node]:
        result: list = []
        stack: list = []
        vizited: list = []
        pointer: Node = self._root

        while True:
            if pointer not in result:
                result.append(pointer)

            if pointer.outbound:
                for node in pointer.outbound:
                    if node not in vizited:
                        stack.append(node)
                        vizited.append(node)

            if not stack:
                break

            pointer = stack.pop(0)

        return result
