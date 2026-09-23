# Vacuum Cleaner - Simple Reflex Agent

roomA = int(input("Enter condition of Room A (0-Clean, 1-Dirty): "))
roomB = int(input("Enter condition of Room B (0-Clean, 1-Dirty): "))

vacuum = int(input("Enter vacuum position (0-A, 1-B): "))
steps = int(input("Enter number of steps: "))

for i in range(steps):

    if vacuum == 0:
        print("\nVacuum is in Room A")

        if roomA == 1:
            print("Room A is DIRTY -> SUCK")
            roomA = 0
        else:
            print("Room A is CLEAN -> MOVE to Room B")
            vacuum = 1

    else:
        print("\nVacuum is in Room B")

        if roomB == 1:
            print("Room B is DIRTY -> SUCK")
            roomB = 0
        else:
            print("Room B is CLEAN -> MOVE to Room A")
            vacuum = 0

print("\nFinal Condition:")
print("Room A:", "CLEAN" if roomA == 0 else "DIRTY")
print("Room B:", "CLEAN" if roomB == 0 else "DIRTY")