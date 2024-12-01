# Recursive Python Function to solve the Tower of Hanoi puzzle.

def TowerOfHanoi(n, start_rod, goal_rod, extra_rod):
    if n == 1:  # Base Case

        print("Move disk", n, "from", start_rod, "to", goal_rod)
        # The base case, where you simply move the disk from the
        # given start-rod to the given goal-rod, while following
        # the required rules.

    else:  # Recursive Step

        TowerOfHanoi(n-1, start_rod, extra_rod, goal_rod)
        # The idea here is that, in order to move a stack of n disks from
        # start-rod to goal-rod, you first recursively move n-1 disks
        # from the start-rod to extra-rod, using the goal-rod as an aid.

        print("Move disk", n, "from", start_rod, "to", goal_rod)
        # Then move the n(th) disk from start-rod to goal-rod.

        TowerOfHanoi(n-1, extra_rod, goal_rod, start_rod)
        # Then, again move n-1 disks recursively from the extra-rod
        # to goal-rod using the start-rod as an aid. Hence, completing
        # the puzzle while following all the rules.


# User Input
disks = int(input("Enter the number of disks: "))

TowerOfHanoi(disks, "Start-Tower", "Goal-Tower", "Extra-Tower")
# Prints the smallest required list of moves that solves the puzzle with n disks.
