from GoatGasDriver import GoatGasDriver
import time

#port, IDs
g = GoatGasDriver('COM5', [0, 1, 2, 3])
g.open_gripper(0, True)
g.open_gripper(1, True)
g.open_gripper(2, True)
g.open_gripper(3, True)
for i in range(1):
    for n in range(4):
        g.open_gripper(n, True)
    time.sleep(0.001)
    for n in range(4):
        g.open_gripper(n, False)
    time.sleep(0.001)
