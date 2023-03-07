# Try and Except

In Python, try and except are used together to implement error handling in your code. 

The basic idea is that you put code that might raise an exception (i.e., an error) inside a **try block**, and then handle any **exceptions** that are raised in the corresponding except block. 

### a basic example of handling input - TRY THIS OUT
```
while True:
    try:
        num = int(input("Enter a number: "))
        print("You entered:", num)
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
```
In this example, the user is prompted to enter a number. The input() function is used to get the user's input as a string, which is then converted to an integer using the int() function. If the user enters a string that cannot be converted to an integer, a ValueError is raised. The try-except block catches the ValueError and prints an error message, prompting the user to enter a valid integer. The loop continues until the user enters a valid integer, at which point the loop is exited and the program prints the number the user entered.

### Here's an more complex example:


```
try:
    # code that might raise an exception goes here
    result = 1 / 0
except ZeroDivisionError:
    # code to handle the exception goes here
    print("Error: cannot divide by zero")
    ```

In this example, we try to divide 1 by 0, which would normally raise a **ZeroDivisionError** exception. 

We put this code inside a try block, and then define an except block that catches the ZeroDivisionError exception and prints an error message.

If an exception is raised **inside the try block**, Python immediately stops executing that block and jumps to the corresponding except block. 

In this way, we can handle errors gracefully in our code and avoid crashes or other unexpected behavior.

It's also possible to have multiple except blocks for different types of exceptions, or to have an else block that runs if no exceptions are raised. Here's another example:

```
try:
    # code that might raise an exception goes here
    result = int("hello")
except ValueError:
    # code to handle the ValueError exception goes here
    print("Error: invalid input")
except Exception as e:
    # code to handle any other type of exception goes here
    print("Error:", str(e))
else:
    # code to run if no exceptions are raised goes here
    print("Success!")
```

In this example, we try to convert the string "hello" to an integer using the int() function, which would raise a ValueError exception. We define an except block to handle this specific type of exception, and another except block to handle any other type of exception that might occur. We also define an else block to run if no exceptions are raised.

**You will see that the unitTestTemplate uses a TRY-EXCEPT method**