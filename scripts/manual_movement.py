import urpy as urpy


robot = urpy.UniversalRobot()

input_str = ""

while input_str != "q":
    input_str = input()
    pose = robot.get_pose()

    if input_str.find("x") == 0:
        input_str = input_str.replace("x", "")
        if input_str.find("+") == 0:
            pose.x += int(input_str)
        elif input_str.find("=") == 0:
            input_str = input_str.replace("=", "")
            pose.x = int(input_str)

    if input_str.find("y") == 0:
        input_str = input_str.replace("y", "")
        if input_str.find("+") == 0:
            pose.y += int(input_str)
        elif input_str.find("=") == 0:
            input_str = input_str.replace("=", "")
            pose.y = int(input_str)
    
    if input_str.find("z") == 0:
        input_str = input_str.replace("z", "")
        if input_str.find("+") == 0:
            pose.z += int(input_str)
        elif input_str.find("=") == 0:
            input_str = input_str.replace("=", "")
            pose.z = int(input_str)
            
    if input_str.find("rx") == 0:
        input_str = input_str.replace("rx", "")
        if input_str.find("+") == 0:
            pose.rx += float(input_str)
        elif input_str.find("=") == 0:
            input_str = input_str.replace("=", "")
            pose.rx = float(input_str)

    if input_str.find("ry") == 0:
        input_str = input_str.replace("ry", "")
        if input_str.find("+") == 0:
            pose.ry += float(input_str)
        elif input_str.find("=") == 0:
            input_str = input_str.replace("=", "")
            pose.ry = float(input_str)
    
    if input_str.find("rz") == 0:
        input_str = input_str.replace("rz", "")
        if input_str.find("+") == 0:
            pose.rz += float(input_str)
        elif input_str.find("=") == 0:
            input_str = input_str.replace("=", "")
            pose.rz = float(input_str)

    robot.move_to(target_pose=pose, wait=False)