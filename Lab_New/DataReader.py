import json
import numpy as np
import matplotlib.pyplot as plt
import os


def read_file_extract_positions(path):
    print("Read "+path)
    file = open(path,"r")
    data = json.load(file)
    file.close()

    positions=[]
    objs=data["objects"]
    for obj in objs:
        coors=obj["3d_coords"]
        x=coors[0]
        y=coors[1]
        vec = np.array([x,y])
        positions.append(vec)

    return positions

def list_of_points_visualizer(lop):
    for pos in lop:
        plt.scatter(pos[0],pos[1])

    plt.xlim(-7,7)
    plt.ylim(-7,7)
    plt.show()

def read_in_directory(path):
    directory = os.listdir(path)
    list_of_lists=[]
    for file in directory:
        if file.endswith(".json"):
            pos=read_file_extract_positions(path+"/"+file)
            list_of_lists.append(pos)
    print(str(len(directory))+" files read.")
    return list_of_lists

def load_classes():
    prox = read_in_directory("proximity")
    simi = read_in_directory("similarity")
    conti = read_in_directory("continuity")
    return [prox,simi,conti]





if __name__ =="__main__":
    dir_path= "test_dir_cont"
    testdata=read_in_directory(dir_path)










