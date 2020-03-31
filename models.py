from abc import ABC


class State(ABC):
    __ID: int = 0

    def __init__(self):
        State.__ID += 1
        self._id = State.__ID

    @property
    def id(self):
        return self._id

    @id.getter
    def id(self) -> int:
        return self._id

    def __str__(self):
        return "<State #"+str(self.id)+">"




class NodeState(State):
    _name: str

    def __init__(self, name):
        super().__init__()
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n: str) -> None:
        self._name = str(n).upper()

    @name.getter
    def name(self) -> str:
        return self._name

    def __str__(self):
        return f"<NodeState #{self.id}: {self.name}>"  # <NodeState #1: name>

    def __eq__(self, other) -> bool:
        try:
            return other.name == self.name
        except:
            return False

    def __hash__(self) -> int:
        return self.id

class Problem:
    pass
