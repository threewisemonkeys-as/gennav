"""
    Various common geometric constructs.
"""
import numpy as np


class Point:
    """
        A Basic Point class
        Args:
            x : x-coordinate of the point (default = 0)
            y : y-coordinate of the point (default = 0)
            z : z-coordinate of the point (default = 0)
    """

    def __init__(self, x=0, y=0, z=0):

        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Point :\n\tx : {}\n\ty : {}\n\tz : {}".format(self.x, self.y, self.z)

    def __repr__(self):
        return "utils.geometry.Point({}, {}, {})".format(self.x, self.y, self.z)


class Quaternion:
    """
        Class for Quaternions
        Args :
            x : x-component of quaternion (default = 0)
            y : y-component of quaternion (default = 0)
            z : z-component of quaternion (default = 0)
            w : w-component of quaternion (default = 1)
    """

    def __init__(self, x=0, y=0, z=0, w=1):

        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return "Quaternion :\n\tx : {}\n\ty : {}\n\tz : {}\n\tw : {}".format(
            self.x, self.y, self.z, self.w
        )

    def __repr__(self):
        return "utils.geometry.Quaternion({}, {}, {}, {})".format(
            self.x, self.y, self.z, self.w
        )


class OrientationRPY:
    """
        Class for representing Orientation in terms if Roll, Pitch, Yaw
        Args:
            roll : rotation about x-axis (default = 0)
            pitch : rotation about y-axis (default = 0)
            yaw : rotation about z-axis (default = 0)
    """

    def __init__(self, roll=0, pitch=0, yaw=0):

        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw

    def __str__(self):
        return "OrientaionRPY :\n\troll : {}\n\tpitch : {}\n\tyaw : {}".format(
            self.roll, self.pitch, self.yaw
        )

    def __repr__(self):
        return "utils.geometry.OrientaionRPY({}, {}, {})".format(
            self.roll, self.pitch, self.yaw
        )


class PointPath:
    """
        A class for storing Path
        Args:
            points = class utils.geometry.Point[] (a list of utils.geometry.Point)
        Note:
            This class does not take into consideration the orientation at each point
            For such a class use utils.geometry.Path
    """

    def __init__(self, points):
        self.points = points

    def __str__(self):
        return str(self.points)

    def __repr__(self):
        return str(self.points)


class PathComplete:
    """
        Class that can be used to represent path which contains RobotStates as waypoints
        Args:
            states = class utils.geometry.RobotState[] (a list of utils.geometry.RobotState)
        Note:
            For representing path using only Points, use utils.geometry.PointPath
    """

    def __init__(self, states):
        self.states = states

    def __str__(self):
        return str(self.states)

    def __repr__(self):
        return str(self.states)


class Vector3D:
    """
        Class for representing a 3 Dimensional Vector
        Args:
            x : x-component (default = 0)
            y : y-component (default = 0)
            z : z-component (default = 0)
        Note:
            This class contains additional methods wrt to the utils.geometry.Point Class
    """

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "Vector :\n\tx : {}\n\ty : {}\n\tz : {}".format(self.x, self.y, self.z)

    def __repr__(self):
        return "utils.geometry.Vector3D({}, {}, {})".format(self.x, self.y, self.z)

    def magnitude(self):
        """
            Returns the magnitude of the vector
        """
        return np.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def unit(self):
        """
            Returns the unit vector of the vector as a Vector3D object
            Returns:
                unitVector (utils.geometry.Vector3D) : Unit vector of the given vector
        """
        if self.x == 0 and self.y == 0 and self.z == 0:
            raise ZeroDivisionError("Cannot find unit Vector of a null vector")
        else:
            return Vector3D(
                self.x / self.magnitude(),
                self.y / self.magnitude(),
                self.z / self.magnitude(),
            )

    def directionCosines(self):
        """
            Returns the direction cosines of the vector, i.e cos(alpha), cos(beta), cos(gamma)
        """
        unit = self.unit()
        return unit.x, unit.y, unit.z