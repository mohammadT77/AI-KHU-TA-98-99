from unittest import TestCase, main


class AlgoTest(TestCase):

    def test_import_dfs_r(self):
        from search_algorithms import dfs_recursive

    def test_call_dfs_r(self):
        from search_algorithms import dfs_recursive as dfs_r
        res = dfs_r(states=None, start=None, goal=None)
        self.assertIsInstance(res, list)

    def test_dfs_r_success(self):
        from search_algorithms import dfs_recursive as dfs_r
        states = {
            's': ['a', 'b', 'c'],
            'a': ['b', 's'],
            'b': ['s', 'a', 'd'],
            'd': ['c', 'b']
        }
        start_state = 's'
        goal_state = 'd'

        res = dfs_r(states=states, start=start_state, goal=goal_state)
        self.assertListEqual(res, ['s', 'a', 'b', 'd'])

    def test2_dfs_r_success(self):
        from search_algorithms import dfs_recursive as dfs_r
        states = {
            's': ['a', 'b', 'd'],
            'a': ['s', 'c'],
            'b': ['s', 'd'],
            'c': ['d', 'a', 'g'],
            'd': ['s', 'a', 'c', 'g', 'b'],
            'g': ['a', 'g'],
        }
        start_state = 's'  # Initial state
        goal_state = 'g'

        res = dfs_r(states=states, start=start_state, goal=goal_state)
        self.assertListEqual(res, ['s', 'a', 'c', 'd', 'g'])

    def test_dfs_2_failure(self):
        from search_algorithms import dfs_recursive
        states = {
            's': ['a', 'b', 'd'],
            'a': ['s', 'c'],
            'b': ['s', 'd'],
            'c': ['d', 'a', 'g'],
            'd': ['b', 's', 'a', 'c', 'g'],
            'g': ['a', 'g'],
        }
        start_state = 's'  # Initial state
        goal_state = 'g'

        # res = dfs_recursive(states=states, start=start_state, goal=goal_state)
        self.assertRaises(Exception, dfs_recursive, states, start_state, goal_state)

    # def test_dfs_nodeState_1_success(self):
    #     from search_algorithms import dfs_recursive as dfs_r
    #     from models import NodeState
    #     S = NodeState("start")
    #     A = NodeState("a")
    #     B = NodeState("b")
    #     C = NodeState("c")
    #     D = NodeState("d")
    #     G = NodeState("goal")
    #
    #
    #     states = {
    #         S: [A, B, D],
    #         A: [S, C],
    #         B: [S, D],
    #         C: [D, A, G],
    #         D: [S, A, C, G, B],
    #         G: [A, G],
    #     }
    #     start_state = S  # Initial state
    #     goal_state = G
    #
    #     res = dfs_r(states=states, start=start_state, goal=goal_state)
    #     # print([str(r) for r in res])
    #     # print(res)
    #     # print([S, A, C, G])
    #     # print([str(r) for r in [S, A, C, G]])
    #     self.assertListEqual(res, [S, A, C, D, G])
    #
    # def test_dfs_nodeState_1_failure(self):
    #     from search_algorithms import dfs_recursive
    #     from models import NodeState
    #     S = NodeState("start")
    #     A = NodeState("a")
    #     B = NodeState("b")
    #     C = NodeState("c")
    #     D = NodeState("d")
    #     G = NodeState("goal")
    #     states = {
    #         S.name: [A, B, D],
    #         A.name: [S, C],
    #         B.name: [S, D],
    #         C.name: [D, A, G],
    #         D.name: [B, S, A, C, G],
    #         G.name: [A, G],
    #     }
    #     start_state = S  # Initial state
    #     goal_state = G
    #
    #     # res = dfs_recursive(states=states, start=start_state, goal=goal_state)
    #     self.assertRaises(Exception, dfs_recursive, states, start_state, goal_state)


# class StateTest(TestCase):
#
#     def test_import_state(self):
#         from models import State
#
#     def test_create_state_failure(self):
#         from models import State
#         try:
#             State()
#             self.assert_(False, "Abstract class couldn't have instance")
#         except:
#             pass


# class NodeTest(TestCase):
#
#     def test_import_node_class(self):
#         from models import NodeState
#
#     def test_create_node_success(self):
#         from models import NodeState
#         name = 'S'
#         n = NodeState(name)
#         print(n)
#         self.assertEqual(n.name, name)
#
#     def test_create_node_failure(self):
#         from models import NodeState
#         name = 's'
#         n = NodeState(name)
#         print(n)
#         self.assertNotEqual(n.name, name)
#
#     def test_node_eq_success(self):
#         from models import NodeState
#         self.assertEqual(NodeState("s"), NodeState('S'))
#
#     def test_node_eq_failure(self):
#         from models import NodeState
#         self.assertFalse(NodeState("s") == NodeState('S1'))
#         self.assertNotEqual(NodeState("s"), NodeState('S1'))
#
#     def test_state_hash(self):
#         from models import NodeState
#         name = 'A'
#         n = NodeState(name)
#         # print(n)
#         # print(hash(n))
#         self.assertEqual(n.id, hash(n))


if __name__ == '__main__':
    main()
