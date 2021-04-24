import math
import numpy as np
import matplotlib.pyplot as plt
import random

def remove_positions(list_of_lists: list):
    relative_delition=0.15
    new_lol=[]
    for list_ac in list_of_lists:
        new_pos_l = []
        for pos in list_ac:
            ran_val = random.random()
            if ran_val>relative_delition:
                print("True")
                new_pos_l.append(pos)
        new_lol.append(new_pos_l)
    print(new_lol)
    return new_lol

def create_quader():
    pos_0=np.array([0.0,0.0])
    pos_C=(random.uniform(0,1.5), random.uniform(0,-1.5))
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
    num_steps = np.floor_divide(distance_all,0.5)
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

    rand_vec_translation = np.array([random.uniform(-3,1.5),random.uniform(-1.5,1.5)])
    for dings in pos:
        print(dings)
        dings+=rand_vec_translation
    return pos

def create_circle():

    num_steps= random.randint(5,10)
    step_size = (math.pi * 2) / num_steps

    steps=np.arange(0.0,math.pi*2,step_size)

    radius_x=random.uniform(0.80,1.2)
    radius_y=random.uniform(0.80,1.2)
    pos=[]
    for step in steps:
        pos.append(np.array([math.cos(step)*radius_x,math.sin(step)*radius_y]))

    max_rad = max(radius_y,radius_y)
    print(max_rad)
    translation_y = random.uniform(-3+max_rad ,3-max_rad)
    translation_x = random.uniform(-3+max_rad, 3-max_rad)
    trans = np.array([translation_x, translation_y])
    print(trans)
    for elem in pos:
        print(elem)
        elem+=trans
        print(elem)
    return pos

def create_line():
    pos = []
    num_elements =  random.randint(4,10)
    distance = random.uniform(0.3, 1)
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

    translation_y = random.uniform(-3,1)
    translation_x = random.uniform(-3,1)
    trans = np.array([translation_x,translation_y])
    for elem in pos:
        elem +=trans

    return pos

def position_visualizer(list_of_lists):
    colormap = plt.cm.get_cmap('hsv', 12)
    color = 0
    print("Num list", len(list_of_lists))
    print("Len first list", len(list_of_lists[0]))
    for list in list_of_lists:
        color+=1
        for index, position in enumerate(list):
             plt.scatter(position[0],position[1],c=colormap(color))
    plt.xlim(-5,5)
    plt.ylim(-5,5)
    plt.show()

def create_random_element():
    rnd= random.randint(0,2)
    if rnd == 0:
        return create_line()
    elif rnd ==1:
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
    return rmvd

def pos_by_continiuty(num_lines):
    figs = []
    for x in range(num_lines):
        figs.append(create_line())
    return figs




if __name__ =="__main__":
    liste  = []
    liste.append(create_circle())
    removed = remove_positions(liste)
    print(removed)
    position_visualizer(removed)








