#!/usr/bin/env python
from random import sample,uniform;
from sys import argv;

def simulate_data(x1,x2,y1,y2,num):
    data=[];
    leftBottom=0;
    while num>0:
        x=uniform(0,x2);
        y=uniform(0,y2);
        label="+";
        if x<x1 and y<y1:
            label="-";
            leftBottom=leftBottom+1;
        data.append([x,y,label]);
        num=num-1;
    print "generate LeftBottom=%d"%(leftBottom);
    return data;

if __name__=="__main__":
    if len(argv)!=2:
        print "useage:",argv[0],"number";
    else:
        data=simulate_data(0.6,1,0.8,1,int(argv[1]));
#    print data;
        outfile=open("data/simulation.csv","w");
        content="x,y,label\n";
        for instance in data:
            content=content+str(instance[0])+","+str(instance[1])+","+instance[2]+"\n";
        outfile.write(content);
        outfile.close();
