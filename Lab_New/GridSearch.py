import time
import timeit

import sklearn.metrics as skm
import DataReader as dr
import ClusteringOwn as cl
import numpy as np
import random

def test_classifier(classifier,data):
    #We have three classes prox, simi, conti

    #Iterate over the 3 classes
    pred=[]
    truth=[]
    for index, class_data in enumerate(data):
        for instance in class_data:
            print(instance)
            result = classifier.choose_grouping(instance)
            pred.append(result)
            truth.append(index)
    conf_mat= skm.confusion_matrix(truth,pred)
    #truth, pred=test_classifier_pred_truth(classifier,data)
    #conf_mat=skm.confusion_matrix(truth,pred)
    return conf_mat

def test_classifier_accuracy(classifier,data):
    truth, pred = test_classifier_pred_truth(classifier,data)
    return skm.accuracy_score(truth,pred)


def test_classifier_pred_truth(classifier,data):
    #We have three classes prox, simi, conti

    #Iterate over the 3 classes
    pred=[]
    truth=[]
    for index, class_data in enumerate(data):
        for instance in class_data:
            #print(instance)
            #result = classifier.choose_grouping(instance)
            result = classifier.similarity_or_proximity(instance)
            pred.append(result)
            truth.append(index)
    conf_mat= skm.confusion_matrix(truth,pred)
    return truth,pred
"""
BEST EPS:  5.2
BEST SAMPLES 2
BEST ACC:  0.77
"""
"""
BEST EPS:  5.1000000000000005
BEST SAMPLES 2
BEST ACC:  0.76
"""


def test_it_confusion(data):
    act_first_cluster_eps = 2.851244258613663  # random.uniform(0.1,10)
    act_fist_cluster_samples = 3
    act_first_similarity_ratio = 0.6314826064402009  # random.random()
    act_second_cluster_eps = 8.334159041251258  # random.uniform(0.1,10)
    act_second_cluster_samples = 6
    act_second_similarity_ratio = 0.25572276775505054

    act_eps = 5.2
    act_samples = 2  # random.randint(1,4)

    classifier = cl.ChooseGrouping(act_first_cluster_eps, act_fist_cluster_samples
                                   , act_first_similarity_ratio, act_second_cluster_eps
                                   , act_second_cluster_samples, act_second_similarity_ratio, act_eps,
                                   act_samples)

    res = test_classifier(classifier,data)
    print(res)

def random_search_second_part(data):
    act_first_cluster_eps = 2.851244258613663  # random.uniform(0.1,10)
    act_fist_cluster_samples = 3
    act_first_similarity_ratio = 0.6314826064402009  # random.random()
    act_second_cluster_eps = 8.334159041251258  # random.uniform(0.1,10)
    act_second_cluster_samples = 6
    act_second_similarity_ratio = 0.25572276775505054  # random.random()

    best_fce = 0.05
    best_msam = 1

    best_accuracy = 0

    for x in range(10000):
        act_eps=random.uniform(0.1,10)
        act_samples=2#random.randint(1,4)

        classifier = cl.ChooseGrouping(act_first_cluster_eps, act_fist_cluster_samples
                                       , act_first_similarity_ratio, act_second_cluster_eps
                                       , act_second_cluster_samples, act_second_similarity_ratio, act_eps,
                                       act_samples)
        acc = test_classifier_accuracy(classifier, data)
        conf_mat = test_classifier(classifier, data)
        print("BEST EPS: ", best_fce)
        print("BEST SAMPLES", best_msam)
        print("BEST ACC: ", best_accuracy)

        print(conf_mat)
        if acc > best_accuracy:
            best_accuracy = acc
            best_fce = act_eps
            best_msam = act_samples



def grid_search_second_part(data):
    act_first_cluster_eps = 2.851244258613663  # random.uniform(0.1,10)
    act_fist_cluster_samples = 3
    act_first_similarity_ratio = 0.6314826064402009  # random.random()
    act_second_cluster_eps = 8.334159041251258  # random.uniform(0.1,10)
    act_second_cluster_samples = 6
    act_second_similarity_ratio = 0.25572276775505054  # random.random()

    best_fce=0.05
    best_msam=1

    best_accuracy=0

    for act_eps in np.arange(0.05,10,0.05):
        for act_samples in np.arange(1,10,1):
            classifier = cl.ChooseGrouping(act_first_cluster_eps, act_fist_cluster_samples
                                           , act_first_similarity_ratio, act_second_cluster_eps
                                           , act_second_cluster_samples, act_second_similarity_ratio,act_eps,act_samples)
            acc = test_classifier_accuracy(classifier, data)
            conf_mat=test_classifier(classifier, data)
            print(conf_mat)
            if acc > best_accuracy:
                best_accuracy=acc
                best_fce=act_eps
                best_msam=act_samples

    print("BEST EPS: ",best_fce)
    print("BEST SAMPLES", best_msam)
    print("BEST ACC: ",best_accuracy)










def random_search(data):
    best_first_cluster_eps = 0
    best_fist_cluster_samples = 0
    best_first_similarity_ratio = 0
    best_second_cluster_eps = 0
    best_second_cluster_samples = 0
    best_second_similarity_ratio = 0

    act_first_cluster_eps = 0
    act_fist_cluster_samples = 0
    act_first_similarity_ratio = 0
    act_second_cluster_eps = 0
    act_second_cluster_samples = 0
    act_second_similarity_ratio = 0

    higehest_acc = 0

    """
    Highest Acc:  0.7133333333333334
    1 EPS:  2.826386669554388
    1 SAMPLES:  3
    1 FSR:  0.8164853356186913
    2 EPS:  5.712296150805398
    2 SAMPLES:  6
    2 RATIO:  0.15615417471881532
    """
    """
    Highest Acc:  0.7266666666666667
    1 EPS:  3.114935645363625
    1 SAMPLES:  3
    1 FSR:  0.5577789286179985
    2 EPS:  5.979129532094208
    2 SAMPLES:  6
    2 RATIO:  0.6897123534285481
    """
    """
    Fixed samples
    Highest Acc:  0.74
    1 EPS:  2.851244258613663
    1 SAMPLES:  3
    1 FSR:  0.6314826064402009
    2 EPS:  8.334159041251258
    2 SAMPLES:  6
    2 RATIO:  0.25572276775505054
    """

    for x in range(100000):
        act_first_cluster_eps = 2.851244258613663 #random.uniform(0.1,10)
        act_fist_cluster_samples = 3
        act_first_similarity_ratio =0.6314826064402009 # random.random()
        act_second_cluster_eps = 8.334159041251258 #random.uniform(0.1,10)
        act_second_cluster_samples = 6
        act_second_similarity_ratio = 0.25572276775505054# random.random()

        classifier = cl.ChooseGrouping(act_first_cluster_eps, act_fist_cluster_samples
                                       , act_first_similarity_ratio, act_second_cluster_eps
                                       , act_second_cluster_samples, act_second_similarity_ratio)
        acc = test_classifier_accuracy(classifier, data)
        print("Actual Accuracy: ", acc)
        print("Highest Acc: ", higehest_acc)
        print(test_classifier(classifier,data))
        if acc > higehest_acc:
            higehest_acc = acc
            best_first_cluster_eps = act_first_cluster_eps
            best_fist_cluster_samples = act_fist_cluster_samples
            best_first_similarity_ratio = act_first_similarity_ratio
            best_second_cluster_eps = act_second_cluster_eps
            best_second_cluster_samples = act_second_cluster_samples
            best_second_similarity_ratio = act_second_similarity_ratio
        print("1 EPS: ", best_first_cluster_eps)
        print("1 SAMPLES: ", best_fist_cluster_samples)
        print("1 FSR: ", best_first_similarity_ratio)
        print("2 EPS: ", best_second_cluster_eps)
        print("2 SAMPLES: ", best_second_cluster_samples)
        print("2 RATIO: ", best_second_similarity_ratio)






def grid_search(data):
    """
    Does gridsearch of the parameters
    :param classifier: classifier
    :param data: data as list of lists of lists here list with 3 elements representing the classes
    :return: best params
    """
    best_first_cluster_eps=0
    best_fist_cluster_samples=0
    best_first_similarity_ratio=0
    best_second_cluster_eps=0
    best_second_cluster_samples=0
    best_second_similarity_ratio=0

    higehest_acc=0
    #First Cluster EPS
    for fceps in np.arange(0.5,8,0.5):
        print("FCEPS: ",fceps)
        #First Cluster samples
        for fcs in np.arange(1,10,1):
            print("FCS: ",fcs)
            #First similarity ratio
            for fsr in np.arange(0,1,0.1):
                #Second Cluster eps:
                for sce in np.arange(0.5,8,0.5):
                    #Second cluster samples
                    for scs in np.arange(1,5,1):
                        #Second cluster ratio
                        for scr in np.arange(0,1,0.1):
                            start = time.time()
                            classifier = cl.ChooseGrouping(fceps,fcs,fsr,sce,scs,scr)
                            acc = test_classifier_accuracy(classifier,data)
                            print("Actual Accuracy: ",acc)
                            print("Highest Acc: ",higehest_acc)
                            #print(test_classifier(classifier,data))
                            if acc > higehest_acc:
                                higehest_acc=acc
                                best_first_cluster_eps=fceps
                                best_fist_cluster_samples=fcs
                                best_first_similarity_ratio=fsr
                                best_second_cluster_eps=sce
                                best_second_cluster_samples=scs
                                best_second_similarity_ratio=scr
                                print("1 EPS: ", best_first_cluster_eps)
                                print("1 SAMPLES: ", best_fist_cluster_samples)
                                print("1 FSR: ", best_first_similarity_ratio)
                                print("2 EPS: ", best_second_cluster_eps)
                                print("2 SAMPLES: ", best_second_cluster_samples)
                                print("2 RATIO: ", best_second_similarity_ratio)
                            end = time.time()
                            print(end - start)
                            print("Calc Per sec: ",1/(end-start))
    print("1 EPS: ",best_first_cluster_eps)
    print("1 SAMPLES: ", best_fist_cluster_samples)
    print("1 FSR: ",best_first_similarity_ratio)
    print("2 EPS: ",best_second_cluster_eps)
    print("2 SAMPLES: ",best_second_cluster_samples)
    print("2 RATIO: ",best_second_similarity_ratio)



def get_class(data_point):
    act_first_cluster_eps = 2.851244258613663  # random.uniform(0.1,10)
    act_fist_cluster_samples = 3
    act_first_similarity_ratio = 0.6314826064402009  # random.random()
    act_second_cluster_eps = 8.334159041251258  # random.uniform(0.1,10)
    act_second_cluster_samples = 6
    act_second_similarity_ratio = 0.25572276775505054

    act_eps = 5.2
    act_samples = 2  # random.randint(1,4)

    classifier = cl.ChooseGrouping(act_first_cluster_eps, act_fist_cluster_samples
                                   , act_first_similarity_ratio, act_second_cluster_eps
                                   , act_second_cluster_samples, act_second_similarity_ratio, act_eps,
                                   act_samples)
    print(len(data_point[0]))
    res =classifier.choose_grouping(data_point[0])
    return res


if __name__=="__main__":
    inp = dr.read_in_directory("other")
    print(inp)
    print(get_class(inp))



    #prox=dr.read_in_directory("prox-test")
    #simi=dr.read_in_directory("simi-test")
    #conti=dr.read_in_directory("conti-test")

    #random.shuffle(prox)
    #prox=prox[:100]

    #random.shuffle(simi)
    #simi=simi[:100]

    #random.shuffle(conti)
    #conti=conti[:100]

    #data=[prox,simi]
    #data=[prox,simi,conti]
    #data = [dr.read_in_directory("test_dir_prox"),dr.read_in_directory("test_dir_sim"),dr.read_in_directory("test_dir_cont")]
    #data is an array with arrays
    #classifier = cl.ChooseGrouping(0.1,1,0.1,0.1,1,0.1)
    #test_result=test_classifier(classifier,data)
    #print(test_result)
    #grid_search(data)
    #random_search_second_part(data)
    #test_it_confusion(data)





