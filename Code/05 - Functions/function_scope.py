# Function Scope
# The scope of a function refers to the frame of the program where
# the variables and parameters defined within that function can be accessed.
# It determines the visibility and lifetime of the variables within a function.


# Global variables are defined outside any function, usually at the top level of the script or module.
# They have a global scope, which means they can be accessed from anywhere within the script or module,
# including inside functions.
global_var = 100


def my_function():
    # Local variables defined inside a function have local scope.
    # They can only be accessed within the function in which they are defined.
    # They are created when the function is called. Once the function execution completes,
    # local variables are destroyed and their memory is released.
    local_var = global_var * 2
    print("Local Variable :", local_var)


# print(local_var)  # This will raise a NameError as local_var cannot be accessed outside its function.
my_function()  # Output = Local Variable : 200
print("Global Variable :", global_var)  # Output = Global Variable : 100
