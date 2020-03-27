from unittest import TestCase, main


class SearchAlgoTest(TestCase):

    def test_import_dfs_func(self):
        from search_algorithms import dfs_recursive

    def test_call_dfs_func(self):
        from search_algorithms import dfs_recursive
        states = {
            's': ['a', 'b'],
            'a': ['b', 'c', 's'],
            'b': ['a', 's', 'g'],
            'c': ['a', 'g'],
            'g': ['a', 'g'],
        }
        start_state = 's'  # Initial state
        goal_state = 'g'

        try:
            d = dfs_recursive(states=states, start=start_state, goal=goal_state)
            self.assertIsInstance(d, list)
        except:
            self.assertEqual(False, msg="Input invalid")

    def test_dfs_1(self):
        from search_algorithms import dfs_recursive
        states = {
            's': ['a', 'b'],
            'a': ['b', 'c', 's'],
            'b': ['a', 's', 'g'],
            'c': ['a', 'g'],
            'g': ['a', 'g'],
        }
        start_state = 's'  # Initial state
        goal_state = 'g'

        res = dfs_recursive(states=states, start=start_state, goal=goal_state)
        self.assertListEqual(res, ['s', 'a', 'b', 'g'])

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

    def test_dfs_2_success(self):
        from search_algorithms import dfs_recursive
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

        res = dfs_recursive(states=states, start=start_state, goal=goal_state)
        self.assertListEqual(res, ['s', 'a', 'c', 'd', 'g'])


if __name__ == '__main__':
    main()
