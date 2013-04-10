#!/usr/bin/env python

class DataSet:
    def __init__(self,filename):  ## just for csv data format
        line_cnt=0;
        self.instances=dict();
        self.distinct_valueset=dict();  ## just for real value type
        for line in open(filename):
            if line=="\n":
                continue;
            fields=line[:-1].split(",");
            if line_cnt==0:  ## csv head
                self.field_names=tuple(fields);
                # for debug
                # print "field names:",fields;
            else:
                if len(fields)!=len(self.field_names):
                    print "wrong fields:",line;
                    raise ValueError("fields number is wrong!");
                if line_cnt==1: ## determine the value type
                   self.field_type=dict();
                   for i in range(0,len(self.field_names)):
                       valueSet=set();
                       try:
                           float(fields[i]);
                           self.distinct_valueset[self.field_names[i]]=set();
                       except ValueError:
                           valueSet.add(fields[i]);
                       self.field_type[self.field_names[i]]=valueSet;
                self.instances[line_cnt]=self.__construct_instance__(fields);
            line_cnt=line_cnt+1;
    def __construct_instance__(self,fields):
        instance=dict();
        for i in range(0,len(fields)):
            field_name=self.field_names[i];
            real_type_mark=self.is_real_type_field(field_name);
            if real_type_mark:
                try:
                    instance[field_name]=float(fields[i]);
                    self.distinct_valueset[field_name].add(float(fields[i]));
                except ValueError:
                    raise ValueError("the value is not float,conflict the value type at first detected");
            else:
                instance[field_name]=fields[i];
                self.field_type[field_name].add(fields[i]);
        return instance;
    def describe(self):
        info="features:"+str(self.field_names)+"\n";
        info=info+"\n dataset size="+str(self.size())+"\n";        
        for field in self.field_names:
            info=info+"description for field:"+field;
            valueset=self.get_distinct_valueset(field);
            if self.is_real_type_field(field):
                info=info+" real value, distinct values number:"+str(len(valueset));
                info=info+" range is ["+str(min(valueset))+","+str(max(valueset))+"]\n";
            else:
                info=info+" enum type, distinct values number:"+str(len(valueset));
                info=info+" valueset="+str(valueset)+"\n";
            info=info+"#"*60+"\n";
        print info;
    def get_instances_idset(self):
        return self.instances.keys();
    def is_real_type_field(self,name):
        if name not in self.field_names:
             raise ValueError(" field name not in the dictionary of dataset");
        # return (name in self.distinct_valueset);
        return len(self.field_type[name])==0;
    def get_label_size(self,name="label"):
        if name not in self.field_names:
            raise ValueError(" there is no class label field!");
        return len(self.field_type[name]);
    def get_label_valueset(self,name="label"):
        if name not in self.field_names:
            raise ValueError(" there is no class label field!");
        return self.field_type[name];
    def size(self):
        return len(self.instances);
    def get_instance(self,Id):
        if not Id in self.instances:
            raise ValueError("Id not in the instances dict of dataset");
        return self.instances[Id];
    def get_attributes(self):
        field_names=[x for x in self.field_names if x!="label"];
        return tuple(field_names);
    def get_distinct_valueset(self,name):
        if not name in self.field_names:
            raise ValueError("the field name not in the dataset field dictionary");
        if self.is_real_type_field(name):
            return self.distinct_valueset[name];
        else:
            return self.field_type[name];

if __name__=="__main__":
    from sys import argv;
    data=DataSet(argv[1]);
    print "instances size=",len(data.instances);
    print data.instances[1];
