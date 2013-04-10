usage: python script/gbt.py data_filename stat_filename max_iter sample_rate learn_rate max_depth split_points

for example: python script/gbt.py data/adult.data.csv output/adult.data.stat 50 0.4 0.1 1 1000

data_filename: the csv datafile used to train and test(random split 1/3 of data as test part)

stat_filename: the file to hold ouput information about prediction accuracy and loss value in each iteration

max_iter: set the iterations in gradient boost algorithm

sample_rate: subsample rate of train data to construct a single decision tree

learn_rate: the learn rate parameter of gradient boost algorithm

max_depth: the maximum depth of a decision tree, max_depth=1 means a decision stump with depth=1

split_points: if a feature is numeric and has many distinct values, it's very slow to find a optimal split point.i use just $split_points$ values to find optimal split point of tree. 0 and negative $split_points$ means do not use the trick

Attentions:

1. the $data_filename$ is a csv formate file with a head. the feature with field name "label" is used as label of classification. you can take the files in path "data" as examples. those two dataset come frome UCI Machine Learning Repository(http://archive.ics.uci.edu/ml/datasets/Adult and http://archive.ics.uci.edu/ml/datasets/Credit+Approval). if a feature is nominal, please add some letters. for example, use A0,A1 while not 0,1. the feature hold only digits is recognized as numeric.

2. at now it is just for classification experiment. the loss function is K-class multinomial deviance.

3. the $stat_filename$ contains the run information of algorithm, the average loss per datapoint on train and test data,the accuracy of prediction for test data

4. you may feel strange about the parameter $split_points$, you can understand it at file "script/tree.py" line 81-82.


