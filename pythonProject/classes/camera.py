from math import sin, cos, radians

from pyrr import Vector3, Matrix44, vector, vector3

from const import MOVE_STEP
from utils import normalize_value

__all__ = [
    'camera'
]


class Camera:
    def __init__(self, pos):
        self.camera_pos = Vector3(pos)
        self.camera_front = Vector3([0.0, 0.0, -1.0])
        self.camera_up = Vector3([0.0, 1.0, 0.0])
        self.camera_right = Vector3([1.0, 0.0, 0.0])

        self.mouse_sensitivity = 0.25
        self.yaw = -90.0
        self.pitch = 0.0

    def get_view_matrix(self):
        # print('44:', Matrix44.look_at(self.camera_pos, self.camera_pos + self.camera_front, self.camera_up))
        # print('la:', self.look_at(self.camera_pos, self.camera_pos + self.camera_front, self.camera_up))
        return Matrix44.look_at(self.camera_pos, self.camera_pos + self.camera_front, self.camera_up)
        # return self.look_at(self.camera_pos, self.camera_pos + self.camera_front, self.camera_up)

    def move_forward(self):
        self.camera_pos += self.camera_front * MOVE_STEP

    def move_backward(self):
        self.camera_pos -= self.camera_front * MOVE_STEP

    def move_right(self):
        self.camera_pos += self.camera_right * MOVE_STEP

    def move_left(self):
        self.camera_pos -= self.camera_right * MOVE_STEP

    def rotate_up_down(self, offset):
        self.pitch += offset
        # self.pitch = normalize_value(self.pitch, -45.0, 45.0)
        self.update_camera_vectors()

    def rotate_left_right(self, offset):
        self.yaw += offset
        self.update_camera_vectors()

    def update_camera_vectors(self):
        front = Vector3([0.0, 0.0, 0.0])
        front.x = cos(radians(self.yaw)) * cos(radians(self.pitch))
        front.y = sin(radians(self.pitch))
        front.z = sin(radians(self.yaw)) * cos(radians(self.pitch))

        self.camera_front = vector.normalise(front)
        self.camera_right = vector.normalise(vector3.cross(self.camera_front, Vector3([0.0, 1.0, 0.0])))
        self.camera_up = vector.normalise(vector3.cross(self.camera_right, self.camera_front))

    def look_at(self, position, target, world_up):
        zaxis = vector.normalise(position - target)
        # 3.Get positive right axis vector
        xaxis = vector.normalise(vector3.cross(vector.normalise(world_up), zaxis))
        # 4.Calculate the camera up vector
        yaxis = vector3.cross(zaxis, xaxis)

        # create translation and rotation matrix
        translation = Matrix44.identity()
        translation[3][0] = -position.x
        translation[3][1] = -position.y
        translation[3][2] = -position.z

        rotation = Matrix44.identity()
        rotation[0][0] = xaxis[0]
        rotation[1][0] = xaxis[1]
        rotation[2][0] = xaxis[2]
        rotation[0][1] = yaxis[0]
        rotation[1][1] = yaxis[1]
        rotation[2][1] = yaxis[2]
        rotation[0][2] = zaxis[0]
        rotation[1][2] = zaxis[1]
        rotation[2][2] = zaxis[2]
        return translation * rotation


camera = Camera([0.0, 4.0, 40.0])
