# Function Scope
# The scope of a function refers to the frame of the program where
# the variables and parameters defined within that function can be accessed.
# It determines the visibility and lifetime of the variables within a function.


# Global variables are defined outside any function, usually at the top level of the script or module.
# They have a global scope, which means they can be accessed from anywhere within the script or module, including inside functions.
global_var = 100


def my_function():
    # Local variables defined inside a function have local scope.
    # They can only be accessed within the function in which they are defined.
    # They are created when the function is called. Once the function execution completes,
    # local variables are destroyed and their memory is released.
    local_var = global_var * 2
    print(f"Local Variable = {local_var}")


# print(local_var)  # This will raise a NameError as local_var cannot be accessed outside its function.
my_function()  # Output : Local Variable = 200
print(f"Global Variable = {global_var}")  # Output : Global Variable = 100

"""
Scope resolution in Python follows the LEGB rule, which stands for Local, Enclosing, Global and Built-in.
1. Local : Refers to the innermost scope, which is the current function.

2. Enclosing : Refers to any enclosing functions. If a function is nested inside another function, 
the inner function can access variables from the outer function's scope.

3. Global : Refers to the module-level scope. Variables defined at the top level of a script or module are 
in the global scope and can be accessed from anywhere within that script or module.

4. Built-in : Refers to the built-in scope, which contains built-in functions and exceptions provided by Python.
These are always available and can be accessed from any scope.

So when a variable is referenced in a function, Python first looks for it in the local scope. 
If it is not found there, it looks in the enclosing scopes (if any), then in the global scope
and finally in the built-in scope. If the variable is not found in any of these scopes, a NameError is raised.
"""