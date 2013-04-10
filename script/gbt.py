#!/usr/bin/env python
from data import DataSet;
from tree import construct_decision_tree;
from model import Model;
from random import uniform,sample;
from sys import argv;

def main(data_filename,stat_filename,max_iter,sample_rate,learn_rate,max_depth,split_points):
    dataset=DataSet(data_filename);
    print "Model parameters configuration:[data_file=%s,stat_file=%s,max_iter=%d,sample_rate=%f,learn_rate=%f,max_depth=%d,split_points=%d]"%(data_filename,stat_filename,max_iter,sample_rate,learn_rate,max_depth,split_points);
    dataset.describe();
    stat_file=open(stat_filename,"w");
    stat_file.write("iteration\taverage loss in train data\tprediction accuracy on test data\taverage loss in test data\n");
    model=Model(max_iter,sample_rate,learn_rate,max_depth,split_points);
    #train_data=dataset.get_instances_idset();
    #test_data=train_data;
    train_data=sample(dataset.get_instances_idset(),int(dataset.size()*2.0/3.0));
    test_data=set(dataset.get_instances_idset())-set(train_data);
    model.train(dataset,train_data,stat_file,test_data);
    #model.test(dataset,test_data);
    stat_file.close();
if __name__=="__main__":
    input_filename="data/adult_part.csv";
    input_filename="data/adult.data.csv";
    if len(argv)!=8:
        print "usage:",argv[0],"data_filename stat_filename max_iter sample_rate learn_rate max_depth split_points";
        print "for example:",argv[0],"data/adult.data.csv output/adult.data.stat 50 0.4 0.1 1 -1";
        print "#"*60;
        print "data_filename: the csv datafile used to train and test( random split 1/3 of data as test part";
        print "stat_filename: the file to hold ouput information about prediction accuracy and loss value in each iteration";
        print "max_iter: set the iterations in gradient boost algorithm";
        print "sample_rate: subsample rate of train data to construct a single decision tree";
        print "learn_rate: the learn rate parameter of gradient boost algorithm";
        print "max_depth: the maximum depth of a decision tree, max_depth=1 means a decision stump with depth=1";
        print "split_points: if a feature is numeric and has many distinct values, it's very slow to find a optimal split point.i use just $split_points$ values to find optimal split point of tree. 0 and negative $split_points$ means do not use the trick";
        print "#"*60;
    else:
        input_filename=argv[1];
        stat_filename=argv[2];
        max_iter=int(argv[3]);
        sample_rate=float(argv[4]);
        learn_rate=float(argv[5]);
        max_depth=int(argv[6]);
        split_points=int(argv[7]);
        main(input_filename,stat_filename,max_iter,sample_rate,learn_rate,max_depth,split_points);
