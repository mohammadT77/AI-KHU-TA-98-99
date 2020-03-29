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


if __name__ == '__main__':
    main()
