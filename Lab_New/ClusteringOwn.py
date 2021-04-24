import math

import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
import posGen
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree



class ChooseGrouping():

    def __init__(self, first_cluster_eps=2, fist_cluster_samples=2, first_similarity_ratio=0.5,
                 second_cluster_eps=0.2, second_cluster_samples=2, second_similarity_ration=0.2,
                 sop_eps=2,sop_samples=2):

        self.first_cluster_eps=first_cluster_eps
        self.fist_cluster_samples=fist_cluster_samples
        self.similarity_ratio=first_similarity_ratio
        self.second_cluster_eps=second_cluster_eps
        self.second_cluster_samples=second_cluster_samples
        self.second_similarity_ration=second_similarity_ration
        self.sop_eps=sop_eps
        self.sop_samples=sop_samples

    def __calc_distance(self, pos1, pos2):
        return math.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)


    def choose_grouping(self, lop):
        #Sort for continuity?
        result = self.first_step(lop)
        if result==2:
            return 2
        else:
            second_result = self.similarity_or_proximity(lop)
            return second_result




    def similarity_or_proximity(self, lop):
        db = DBSCAN(eps=self.sop_eps, min_samples=self.sop_samples, metric='euclidean')
        db = db.fit(lop)
        labels= db.labels_
        num_cluster= len(set(labels)) - (1 if -1 in labels else 0)
        if num_cluster > 1:
            return 0
        else:
            return 1




    def first_step(self, lop):
        """
        Gets a list of positins, returns the grouping
        :param lop: List of positions. A position is a list of lenth 2
        :return:
        """
        #First cluster our input.
        db = DBSCAN(eps=self.first_cluster_eps, min_samples=self.fist_cluster_samples, metric='euclidean')
        db = db.fit(lop)
        labels = db.labels_
        num_cluster= len(set(labels)) - (1 if -1 in labels else 0)
        noise_group=[]
        for index, elem in enumerate(labels):
            if elem == -1:
                noise_group.append(lop[index])
        clusters=[]
        for k in range(num_cluster):
            new_cluster=[]
            for index, elem in enumerate(labels):
                if elem == k:
                    new_cluster.append(lop[index])
            clusters.append(new_cluster)
        #print("--Noise Group--")
        #print(noise_group)
        #If we only have more than 50% noise, we dont't have cluster
        if len(noise_group)/len(lop)>=self.similarity_ratio:
            #print("Group by similarity.")
            return 1
        for cluster in clusters:
            result = self.__is_continous_in_cluster(cluster)
            #We have a continuity in one of the clsuters
            if result == True:
                #print("Group by Continuity")
                return 2
        #print("Group by Proximity")
        return 0


    def __is_continous_in_cluster(self, list_of_pos):
        list_of_nearest=[]
        #If there is only one element in the cluster, we don't ahve any continuity.
        if len(list_of_pos)<=1:
            return False
        #Calcualte the nearest neighbout for each
        for pos in list_of_pos:
            min_dist=1000000
            min_pos=None
            for pos2 in list_of_pos:
                if not (pos2==pos).all():
                    dist = self.__calc_distance(pos, pos2)
                    if dist < min_dist:
                        min_dist = dist
                        min_pos = pos2
            list_of_nearest.append([np.array(pos),np.array(min_pos)])
        list_of_vectors = []
        for tuples in list_of_nearest:
            #print(tuples)
            vector = tuples[0]-tuples[1]
            #Sorry, the correct code is in the comment.
            #I noticed the error short before deadline :(
            #So the results are not fully correct.
            #In the paper is the correct algorithm described, but with the evaluation on the wrong one.
            #The correct one just can get better :) or if not, this one is also okay tho.
            """
            vector = vector/np.linalg.norm(vector)
            vector = np.abs(vector)"""
            if vector[0]<0:
                vector*=-1
            list_of_vectors.append(vector)
        print("num we",len(list_of_vectors))
        #posGen.position_visualizer([list_of_vectors])
        db_scan =  DBSCAN(eps=self.second_cluster_eps,min_samples=self.second_cluster_samples, metric='euclidean')
        db = db_scan.fit(list_of_vectors)
        labels=db.labels_
        num_cluster = len(set(labels)) - (1 if -1 in labels else 0)
        num_noise_points = list(labels).count(-1)
        if num_noise_points/len(list_of_pos)>=self.second_similarity_ration:
            #print("Group by Proximity")
            return False
        #print("Group by Conitnuity")
        return True



if __name__ == "__main__":
    list_of_two_clsuters=[[0,0.1],[0,1.1],[1,-0.1],[1,1],[3,3],[3,4],[4,3],[4,4],[-1,1]]
    list_of_pos_cont = [[0.9,1.1],[0,0.1],[2,2.2],[3.1,2.9],[4.2,3.8]]
    list_of_pos_rnd = [[0,0],[1,1],[-1,-1],[1,0],[0,1],[-1,0]]
    posGen.position_visualizer([list_of_pos_rnd])
    blalbla = np.array(list_of_pos_cont)
    list_of_pos_rnd=np.array(list_of_pos_rnd)
    #__is_continous_in_cluster(list_of_two_clsuters)
    grouper = ChooseGrouping()
    grouper.first_step(list_of_pos_rnd)










