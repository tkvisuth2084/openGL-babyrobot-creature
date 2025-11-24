"""
Model our creature and wrap it in one class.
First version on 09/28/2021

:author: micou(Zezhou Sun)
:version: 2021.2.1

----------------------------------

Modified by Daniel Scrivener 09/2023
"""

from Component import Component
from Point import Point
import ColorType as Ct
from Shapes import Cube
from Shapes import Cylinder
from Shapes import Sphere
import numpy as np



        
    


class ModelLinkage(Component):
    """
    Define our linkage model
    """

    ##### TODO 2: Model the Creature
    # Build the class(es) of objects that could utilize your built geometric object/combination classes. E.g., you could define
    # three instances of the cyclinder trunk class and link them together to be the "limb" class of your creature. 
    #
    # In order to simplify the process of constructing your model, the rotational origin of each Shape has been offset by -1/2 * dz,
    # where dz is the total length of the shape along its z-axis. In other words, the rotational origin lies along the smallest 
    # local z-value rather than being at the translational origin, or the object's true center. 
    # 
    # This allows Shapes to rotate "at the joint" when chained together, much like segments of a limb. 
    #
    # In general, you should construct each component such that it is longest in its local z-direction: 
    # otherwise, rotations may not behave as expected.
    #
    # Please see Blackboard for an illustration of how this behavior works.

    components = None
    contextParent = None

    def __init__(self, parent, position, shaderProg, display_obj=None):
        super().__init__(position, display_obj)
        self.contextParent = parent

        linkageLength = 0.5
        link1 = Cube(Point((0, 0, 0)), shaderProg, [0.2, 0.2, linkageLength], Ct.DARKORANGE1)
        link2 = Cube(Point((0, 0, linkageLength)), shaderProg, [0.2, 0.2, linkageLength], Ct.DARKORANGE2)
        link3 = Cube(Point((0, 0, linkageLength)), shaderProg, [0.2, 0.2, linkageLength], Ct.DARKORANGE3)
        link4 = Cube(Point((0, 0, linkageLength)), shaderProg, [0.2, 0.2, linkageLength], Ct.DARKORANGE4)

        self.addChild(link1)
        link1.addChild(link2)
        link2.addChild(link3)
        link3.addChild(link4)

        self.componentList = [link1, link2, link3, link4]
        self.componentDict = {
            "link1": link1,
            "link2": link2,
            "link3": link3,
            "link4": link4
        }


class babyRobot(Component):

    components = None
    contextParent = None

    def __init__(self, parent, position, shaderProg, display_obj=None):
        super().__init__(position, display_obj)
        self.contextParent = parent

        #Initialize Cube shape for robot's head
        head = Cube(Point((0,1.3,0)), shaderProg, [1.2,1.2,1.2], Ct.PINK)
        self.addChild(head) 
    

        stick = Cylinder(Point((0,0.6,0)), shaderProg, [0.1, 0.2, 0.1], Ct.SOFTRED)
        head.addChild(stick) #add elements that belong to head 

        ball = Sphere(Point((0, 0.3, 0)), shaderProg, [0.08,0.08,0.08], Ct.PINK)
        stick.addChild(ball)

        lips = Cylinder(Point((0,-0.2, 0.4)), shaderProg, [0.16, 0.17, 0.2], Ct.SOFTRED)
        head.addChild(lips)

    
    
        #body
        body = Cube(Point((0,0,0)), shaderProg, [1.2,1.2,1.2], Ct.PINK)
        self.addChild(body)

        button = Sphere(Point((-0.35, 0.35, 0.6)), shaderProg, [0.06,0.06,0.06], Ct.RED)
        body.addChild(button)

        tummy = Cube(Point((0,0,0.45)), shaderProg, [0.8,0.5,0.5], Ct.SOFTRED)
        body.addChild(tummy)

        


        #neck
        neck = Cylinder(Point((0,0.7,0)), shaderProg, [0.4, 0.4, 0.4], Ct.SOFTRED)
        self.addChild(neck)

        #eyes
        eye_left = Sphere(Point((-0.3, 0.1, 0.5)), shaderProg, [0.2,0.2,0.2], Ct.BLACK)
        eye_right = Sphere(Point((0.3, 0.1, 0.5)), shaderProg, [0.2,0.2,0.2], Ct.BLACK)

        head.addChild(eye_left)
        head.addChild(eye_right)

        lash1_l = Cylinder(Point((-0.1,0.1,0)), shaderProg, [0.02, 0.02, 0.25], Ct.BLACK)
        lash2_l = Cylinder(Point((0.1,0.1,0)), shaderProg, [0.02, 0.02, 0.25], Ct.BLACK)
        lash1_r = Cylinder(Point((-0.1,0.1,0)), shaderProg, [0.02, 0.02, 0.25], Ct.BLACK)
        lash2_r = Cylinder(Point((0.1,0.1,0)), shaderProg, [0.02, 0.02, 0.25], Ct.BLACK)

        eye_left.addChild(lash1_l)
        eye_left.addChild(lash2_l)
        eye_right.addChild(lash1_r)
        eye_right.addChild(lash2_r)

        #ears
        ear_l = Sphere(Point((-0.6, 0, 0)), shaderProg, [0.2,0.2,0.2], Ct.SOFTRED)
        ear_r = Sphere(Point((0.6, 0, 0)), shaderProg, [0.2,0.2,0.2], Ct.SOFTRED)

        head.addChild(ear_l)
        head.addChild(ear_r)


        #rightarm
        shoulder_r = Sphere(Point((0.6, 0.25, 0)), shaderProg, [0.2,0.2,0.2], Ct.SOFTRED)
        upper_arm_r = Cylinder(Point((0, 0, 0.3)), shaderProg, [0.15, 0.15, 0.2], Ct.PINK)
        elbow_r = Sphere(Point((0, 0, 0.25)), shaderProg, [0.15,0.15,0.15], Ct.SOFTRED)
        forearm_r = Cylinder(Point((0, 0, 0.2)), shaderProg, [0.15, 0.15, 0.2], Ct.PINK)
        wrist_r = Sphere(Point((0, 0, 0.3)), shaderProg, [0.15,0.15,0.15], Ct.SOFTRED)
        hand_r = Cube(Point((0,0,0.1)),shaderProg, [0.3,0.3,0.3], Ct.SOFTRED)


         
        body.addChild(shoulder_r)
        shoulder_r.addChild(upper_arm_r)
        upper_arm_r.addChild(elbow_r)
        elbow_r.addChild(forearm_r)
        forearm_r.addChild(wrist_r)
        wrist_r.addChild(hand_r)

        #leftarm
        shoulder_l = Sphere(Point((-0.6, 0.25, 0)), shaderProg, [0.2,0.2,0.2], Ct.SOFTRED)
        upper_arm_l = Cylinder(Point((0, 0, 0.3)), shaderProg, [0.15, 0.15, 0.2], Ct.PINK)
        elbow_l = Sphere(Point((0, 0, 0.25)), shaderProg, [0.15,0.15,0.15], Ct.SOFTRED)
        forearm_l = Cylinder(Point((0, 0, 0.2)), shaderProg, [0.15, 0.15, 0.2], Ct.PINK)
        wrist_l = Sphere(Point((0, 0, 0.3)), shaderProg, [0.15,0.15,0.15], Ct.SOFTRED)
        hand_l = Cube(Point((0,0,0.1)),shaderProg, [0.3,0.3,0.3], Ct.SOFTRED)


         
        body.addChild(shoulder_l)
        shoulder_l.addChild(upper_arm_l)
        upper_arm_l.addChild(elbow_l)
        elbow_l.addChild(forearm_l)
        forearm_l.addChild(wrist_l)
        wrist_l.addChild(hand_l)


        #rightleg
        hip_r = Sphere(Point((0.3, -0.4, 0.1)), shaderProg, [0.3,0.3,0.3], Ct.SOFTRED)
        thigh_r = Cylinder(Point((0, 0, 0.2)), shaderProg, [0.2,0.2,0.2], Ct.PINK)
        knee_r = Sphere(Point((0, 0, 0.3)), shaderProg, [0.2,0.2,0.2], Ct.SOFTRED)
        calf_r = Cylinder(Point((0, 0, 0.1)), shaderProg, [0.2,0.2,0.2], Ct.PINK)
        ankle_r = Sphere(Point((0, 0, 0.3)), shaderProg, [0.2,0.2,0.2], Ct.SOFTRED)
        feet_r = Cube(Point((0, 0,0.2)),shaderProg, [0.4,0.4,0.4], Ct.SOFTRED)

        body.addChild(hip_r)
        hip_r.addChild(thigh_r)
        thigh_r.addChild(knee_r)
        knee_r.addChild(calf_r)
        calf_r.addChild(ankle_r)
        ankle_r.addChild(feet_r)

        #leftleg
        hip_l = Sphere(Point((-0.3, -0.4, 0.1)), shaderProg, [0.3,0.3,0.3], Ct.SOFTRED)
        thigh_l = Cylinder(Point((0, 0, 0.2)), shaderProg, [0.2,0.2,0.2], Ct.PINK)
        knee_l = Sphere(Point((0, 0, 0.3)), shaderProg, [0.2,0.2,0.2], Ct.SOFTRED)
        calf_l = Cylinder(Point((0, 0, 0.1)), shaderProg, [0.2,0.2,0.2], Ct.PINK)
        ankle_l = Sphere(Point((0, 0, 0.3)), shaderProg, [0.2,0.2,0.2], Ct.SOFTRED)
        feet_l = Cube(Point((0, 0,0.2)),shaderProg, [0.4,0.4,0.4], Ct.SOFTRED)

        body.addChild(hip_l)
        hip_l.addChild(thigh_l)
        thigh_l.addChild(knee_l)
        knee_l.addChild(calf_l)
        calf_l.addChild(ankle_l)
        ankle_l.addChild(feet_l)

        #windup key
        key_base = Sphere(Point((0, 0, -0.6)), shaderProg, [0.3,0.3,0.3], Ct.YELLOW)
        key_stem = Cylinder(Point((0, 0, -0.2)), shaderProg, [0.2,0.2,0.3], Ct.YELLOW)
        key_connect = Cylinder(Point((0, 0, -0.2)), shaderProg, [0.2,0.2,0.3], Ct.YELLOW)
        key_top = Sphere(Point((0, 0.4, -0.2)), shaderProg, [0.3,0.3,0.1], Ct.YELLOW)
        key_bot = Sphere(Point((0, -0.4, -0.2)), shaderProg, [0.3,0.3,0.1], Ct.YELLOW)

        body.addChild(key_base)
        key_base.addChild(key_stem)
        key_stem.addChild(key_connect)
        key_connect.addChild(key_top)
        key_connect.addChild(key_bot)




        self.componentList = [head, neck, body, shoulder_r, elbow_r, wrist_r, hand_r, shoulder_l, elbow_l, wrist_l, hip_l, knee_l,ankle_l, hip_r, knee_r, ankle_r, key_base]
        self.componentDict = {
            "head": head,
            "neck": neck,
            "body": body,
            "shoulder_r": shoulder_r,
            "elbow_r": elbow_r,
            "wrist_r": wrist_r,
            "hip_l": hip_l,
            "hip_r": hip_r,
            "knee_l": knee_l,
            "kneel_r": knee_r,
            "key_base": key_base

        }




        ##### TODO 4: Define creature's joint behavior
        # Requirements:
        #   1. Set a reasonable rotation range for each joint,
        #      so that creature won't intersect itself or bend in unnatural ways
        #   2. Orientation of joint rotations for the left and right parts should mirror each other.


        #limits for head
        head.setRotateExtent(head.uAxis, -10,10)  
        head.setRotateExtent(head.vAxis, -20,20)  
        head.setRotateExtent(head.wAxis, -30,30)  

        #limits for neck
        neck.setRotateExtent(neck.uAxis, -10,10)
        neck.setRotateExtent(neck.vAxis, -20,20)
        neck.setRotateExtent(neck.wAxis, -10,10)

        #limits for body
        body.setRotateExtent(body.uAxis, -10,10)  
        body.setRotateExtent(body.vAxis, -20,20)  
        body.setRotateExtent(body.wAxis, -30,30) 
        


        shoulder_r.setRotateExtent(shoulder_l.uAxis, -90, 90)
        shoulder_r.setRotateExtent(shoulder_l.vAxis, -90, 90)
        shoulder_r.setRotateExtent(shoulder_l.wAxis, -90, 90)

        shoulder_l.setRotateExtent(shoulder_l.uAxis, -90, 90)
        shoulder_l.setRotateExtent(shoulder_l.vAxis, -90, 90)
        shoulder_l.setRotateExtent(shoulder_l.wAxis, -90, 90)

        elbow_r.setRotateExtent(elbow_l.uAxis, -120, 120)
        elbow_r.setRotateExtent(elbow_l.vAxis, 0, 90)
        elbow_r.setRotateExtent(elbow_l.wAxis, -90, 90)

        elbow_l.setRotateExtent(elbow_l.uAxis, -120, 120)
        elbow_l.setRotateExtent(elbow_l.vAxis, -90, 0)
        elbow_l.setRotateExtent(elbow_l.wAxis, -90, 90)

        hip_r.setRotateExtent(hip_r.uAxis, -10, 180)
        hip_r.setRotateExtent(hip_r.vAxis, -90, 90)
        hip_r.setRotateExtent(hip_r.wAxis, -90, 90)

        hip_l.setRotateExtent(hip_l.uAxis, -10, 180)
        hip_l.setRotateExtent(hip_l.vAxis, -90, 90)
        hip_l.setRotateExtent(hip_l.wAxis, -90, 90)
        
        knee_r.setRotateExtent(knee_r.uAxis, 0, 110)
        knee_r.setRotateExtent(knee_r.vAxis, -90, 90)
        knee_r.setRotateExtent(knee_r.wAxis, -90, 90)
        
        knee_l.setRotateExtent(knee_l.uAxis, 0, 110)
        knee_l.setRotateExtent(knee_l.vAxis, -90, 90)
        knee_l.setRotateExtent(knee_l.wAxis, -90, 90)

        ankle_l.setRotateExtent(ankle_l.uAxis, -20, 10)
        ankle_r.setRotateExtent(ankle_r.uAxis, -10, 20)

        key_base.setRotateExtent(key_base.uAxis, 0, 1)
        key_base.setRotateExtent(key_base.vAxis, 0, 1)
        key_base.setRotateExtent(key_base.wAxis, -180, 180)





        




        
        


        

