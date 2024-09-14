def assert_all_cases(self, test_cases, test_function, transform_result_function = lambda x: x):
    for t in test_cases:
        if not isinstance(t[0], tuple):
            inputs = (t[0],)
        else:
            inputs = t[0]

        self.assertEqual(
            transform_result_function(test_function(*inputs)),
            t[1]
        )
