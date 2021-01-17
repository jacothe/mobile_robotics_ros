
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point, Quaternion, PoseStamped
from nav_msgs.msg import Path


def create_line_strip(nodes_path):
    marker = Marker()
    marker.header.frame_id = "map"
    marker.ns = "navigation"
    marker.id = 0
    marker.type = Marker.LINE_STRIP
    marker.action = Marker.ADD
    marker.scale.x = 0.3
    marker.color.a = 0.5
    marker.color.b = 1.0
    marker.pose.orientation = Quaternion(0, 0, 0, 1)
    marker.points.clear()
    for node in nodes_path:
        marker.points.append(Point(node.x + 0.5, node.y+ 0.5, 0.0))
    return marker

def create_marker(coord):
    marker = Marker()
    marker.header.frame_id = "map"
    marker.ns = "navigation"
    marker.id = 0
    marker.type = Marker.CUBE
    marker.action = Marker.ADD
    marker.scale.x = 1
    marker.scale.y = 1
    marker.scale.z = 0.2
    marker.color.a = 1.0
    marker.color.r = 1.0
    marker.pose.orientation = Quaternion(0, 0, 0, 1)
    marker.pose.position.x = coord[0] + 0.5
    marker.pose.position.y = coord[1] + 0.5
    return marker

def build_path_message(node_path):
    msg = Path()
    msg.header.frame_id = "map"
    for node in node_path:
        pose = PoseStamped()
        pose.pose.position.x = node.x
        pose.pose.position.y = node.y
        pose.pose.position.z = 0
        pose.pose.orientation = Quaternion(0, 0, 0, 1)
        msg.poses.append(pose)

    return msg
