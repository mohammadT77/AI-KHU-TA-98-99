from abc import ABC, abstractmethod
from collections.abc import Hashable


class State(Hashable, ABC):
    __ID: int = 0

    def __init__(self):
        State.__ID += 1
        self.__ID = State.__ID

    @property
    def id(self):
        return self.__ID

    @id.getter
    def id(self):
        return int(self.__ID)

    def __eq__(self, other):
        try:
            return other.id == self.id
        except:
            return False

    def __str__(self):
        return "<State #" + str(self.id) + ">"

    @abstractmethod
    def __hash__(self):
        return self.id


class NodeState(State):
    _name: str

    def __init__(self, name: str):
        super().__init__()
        self.name = name.upper()

    @property
    def name(self):
        return self._name

    @name.getter
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = str(name).upper()

    def __eq__(self, other):
        try:
            return other.name == self.name
        except:
            return False

    def __str__(self):
        return f"<NodeState #{self.id}: {self.name}>"

    def __hash__(self):
        return super().__hash__()


class Problem(dict):
    pass

