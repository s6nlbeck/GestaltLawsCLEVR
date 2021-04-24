import math
import numpy as np
import random
#import matplotlib.pyplot as plt

def remove_positions(list_of_lists: list):
    relative_delition=0.15
    new_lol=[]
    for list_ac in list_of_lists:
        new_pos_l = []
        for pos in list_ac:
            ran_val = random.random()
            if ran_val>relative_delition:
                new_pos_l.append(pos)
        new_lol.append(new_pos_l)
    print(new_lol)
    return new_lol

def create_quader():
    print("--------------------QUADER")
    pos_0=np.array([0.0,0.0])
    pos_C=(random.uniform(2,7), random.uniform(2,-7))
    pos_B=(pos_C[1]*-1,pos_C[0])
    B=np.array(pos_B)
    C=np.array(pos_C)
    right=B-C
    left = np.array([-C,B])
    solution = np.linalg.solve(left, right)
    end=C+solution*B
    pos=[]
    pos.append(pos_0)
    pos.append(B)
    pos.append(end)
    pos.append(C)
    distance_all = np.linalg.norm(B)
    num_steps = np.floor_divide(distance_all,random.uniform(2,4))
    num_steps = int(num_steps)
    interpolate=[]
    #Calculate the interpolated elements
    for index, position in enumerate(pos):
        print(position)

        #Calc the vector between the points
        if index < 3:
            vec = pos[index + 1] - position
            distance = np.linalg.norm(vec)
            step_size = distance/num_steps
            for num_elem in range(num_steps-1):
                intpos = (position+(vec/num_steps)) + (vec/num_steps) * num_elem
                interpolate.append(intpos)
        else:
            vec = pos[0] - position
            distance = np.linalg.norm(vec)
            step_size = distance / num_steps
            for num_elem in range(num_steps-1):
                intpos = (position+(vec/num_steps)) + (vec/num_steps) * num_elem
                interpolate.append(intpos)
    pos+=interpolate

    rand_vec_translation = np.array([random.uniform(-7,7-distance_all),random.uniform(-7,7-distance_all)])
    for dings in pos:
        dings+=rand_vec_translation
    return pos

def create_circle():
    print("-----------------CIRCLE")
    num_steps= random.randint(7,10)
    step_size = (math.pi * 2) / num_steps

    steps=np.arange(0.0,math.pi*2,step_size)

    radius_x=random.uniform(2,9)
    radius_y=radius_x
    pos=[]
    for step in steps:
        pos.append(np.array([math.cos(step)*radius_x,math.sin(step)*radius_y]))
    max_rad = max(radius_y,radius_y)
    translation_y = random.uniform(-7 ,7)
    translation_x = random.uniform(-7, 7)
    trans = np.array([translation_x, translation_y])
    for elem in pos:
        elem+=trans
    return pos

def create_line():
    pos = []
    num_elements =  random.randint(3,7)
    distance = random.uniform(1.5, 4)
    pos.append(np.array([0.0,0.0]))
    """ last_cos=random.uniform(0,2*math.pi)
    last_sin=random.uniform(0,2*math.pi)"""
    theta = random.uniform(0,2*math.pi/4)


    for elem in range(num_elements):
        """new_cos = last_cos + random.uniform(-0.5,0.5)
        new_sin = last_sin + random.uniform(-0.5,0.5)
        new_pos = pos[elem] + np.array([math.cos(new_cos)*distance,math.sin(new_sin)*distance])
        last_sin=new_sin
        last_cos = new_cos"""
        new_theta = theta + random.uniform(-0.3, 0.3)
        new_pos = pos[elem] + np.array([math.cos(new_theta) * distance, math.sin(new_theta) * distance])
        #new_pos=pos[elem]+np.array([0.25,0.25])+np.array([random.uniform(-0.1,0.1),random.uniform(-0.1,0.1)])
        #new_pos= (new_pos/np.linalg.norm(new_pos-pos[elem]))*0.3
        theta = new_theta
        pos.append(new_pos)
        print("Length: ",np.linalg.norm(pos[elem]-new_pos))

    translation_y = random.uniform(-7,0)
    translation_x = random.uniform(-7,0)
    trans = np.array([translation_x,translation_y])
    for elem in pos:
        elem +=trans

    return pos

"""def position_visualizer(list_of_lists):
    colormap = plt.cm.get_cmap('hsv', 5)

    color = 0
    for list in list_of_lists:
        color+=1
        for index, position in enumerate(list):
            if index<4:
                plt.scatter(position[0], position[1], c="black")
            else:
                plt.scatter(position[0],position[1],c=colormap(color))
    plt.xlim(-3,3)
    plt.ylim(-3,3)
    plt.show()"""

def create_random_element():
    rnd= random.randint(0,1)
    if rnd ==1:
        return create_circle()
    else:
        return create_quader()

def create_random_figures(num_figures):
    figs = []
    for i in range(num_figures):
        figs.append(create_random_element())
    return figs

def pos_by_closure(num_elems):
    figs = create_random_figures(num_elems)
    rmvd = remove_positions(figs)
    return numpy_to_normal(rmvd)

def pos_by_continiuty(num_lines):
    figs = []
    for x in range(num_lines):
        figs.append(create_line())
    return numpy_to_normal(figs)

def pos_by_good_fig(num_objs):
    objs = []
    for i in range(num_objs):
        objs.append(create_random_element())
    return numpy_to_normal(objs)


def numpy_to_normal(list_of_lists):
    new_l = []
    for liste in list_of_lists:
        obj_list = []
        for elem in liste:
            obj_list.append(elem.tolist())
        new_l.append(obj_list)
    return new_l

"""def position_visualizer(list_of_lists):
    colormap = plt.cm.get_cmap('hsv', 5)

    color = 0
    for list in list_of_lists:
        color+=1
        for index, position in enumerate(list):
            plt.scatter(position[0],position[1],c=colormap(color))
    #plt.xlim(-3,3)
    #plt.ylim(-3,3)
    plt.show()
"""




if __name__ =="__main__":
    liste  = []
    lsite = pos_by_continiuty(5)
    #position_visualizer(lsite)










