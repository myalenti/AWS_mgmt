'''
Created on Nov 22, 2016

@author: myalenti
'''


if __name__ == '__main__':
    pass

import boto3
import datetime
import getopt, sys
#Setting Defaults
days=10
pattern='myalenti*'
try:
    opts, args = getopt.getopt(sys.argv[1:], "d:")
except getopt.GetoptError:
    print "You provided invalid command line switches."
    #usage()
    exit(2)

    
for opt, arg in opts:
    #print "Tuple is " , opt, arg
    if opt in ("-d"):
        days=int(arg)
    else:
        print "Invalid Parameters detected"
        #usage()
        exit(2)    

def getTagValue(tagName, tagArray):
    for i in tagArray:
        if i['Key'] == tagName:
            return i['Value']
        
def getInstances(prefix):
    instances = clientEc2.describe_instances( Filters=[ {'Name' : 'tag:Name', 'Values' : [ prefix ] }] )
    #print("Found the following number of instances to update: " + str(len(instances)))
    myInstances = []
    for elem in instances['Reservations']:
        for inst in elem['Instances']:
            instId =  inst['InstanceId']
            instName = getTagValue("Name", inst['Tags'])
            #print inst['Tags']
            #print(getTagValue("expire-on", inst['Tags']))
            mydate = getTagValue("expire-on", inst['Tags']) 
            print(instId + " , " + instName + " , " + mydate)
            r = { "instanceId" : instId , "instName" : instName, "expireDate" : mydate}
            myInstances.append(r)
    return myInstances


clientEc2 = boto3.client('ec2')
myInstances = getInstances(pattern)
mydate = datetime.date.today() + datetime.timedelta(days) 
instList = []
for i in myInstances:
    instList.append( i['instanceId'])
#print(instList)

resp = clientEc2.create_tags(Resources=instList, Tags=[ { "Key" : "expire-on" , "Value" : str(mydate)}])
print(resp['ResponseMetadata'])
myInstances = getInstances(pattern)