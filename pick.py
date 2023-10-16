from niryo_robot_python_ros_wrapper import *
import rospy

# Initializing ROS node
rospy.init_node('niryo_robot_example_python_ros_wrapper')

# Connecting to the ROS Wrapper & calibrating if needed
niryo_robot = NiryoRosWrapper()
niryo_robot.calibrate_auto()

# Updating tool
niryo_robot.update_tool()

# Opening Gripper/Pushing Air
niryo_robot.release_with_tool()
# Going to pick pose
niryo_robot.move_pose(0.2, 0.1, 0.14, 0.0, 1.57, 0)
# Picking
niryo_robot.grasp_with_tool()
# Moving to place pose
niryo_robot.move_pose(0.2, -0.1, 0.14, 0.0, 1.57, 0)
# Placing !
niryo_robot.release_with_tool()