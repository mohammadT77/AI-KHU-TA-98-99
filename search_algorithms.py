from typing import Dict, List


def dfs_recursive(states: Dict[str, List[str]], start: str, goal: str, closed=None) -> List[str]:
    if closed is None:
        closed = []
    # print('states:', states)
    # print('start:', start)
    # print('goal:', goal)
    # print('closed:', closed)
    if start == goal:
        return [goal]

    childes = states.pop(start)
    # print('childes:', childes)
    closed.append(start)
    # print('new_closed:', closed)

    while childes[0] in closed:
        childes.pop(0)

    # print('new_child:', childes)
    # print('new_start:', childes[0])
    res = dfs_recursive(states, childes[0], goal, closed)
    res.insert(0, start)
    return res
