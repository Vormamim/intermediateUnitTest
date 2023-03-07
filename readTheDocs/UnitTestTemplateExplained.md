# Let's examine the test cases we're running

In the **TestCalculateSum class**, there are four test cases defined using the **self.assertEqual()** method. 

Each test case consists of two arguments: the first argument is a call to the calculate_sum() function with two input parameters, and the second argument is the expected output value.

For example, the first test case is:
```self.assertEqual(calculate_sum(2, 3), 5)```

So we can then also use

```self.assertEqual(calculate_sum(-1, 1), 0)``

So then we run the test, it loads the function we create in main.
Main then returns a value to the test which passes or fails

This is a simple example of a unit test

