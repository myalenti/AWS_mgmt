'''
Created on Nov 22, 2016

@author: myalenti
'''


if __name__ == '__main__':
    pass

import boto3
import datetime
import getopt, sys

def getTagValue(tagName, tagArray):
    for i in tagArray:
        if i['Key'] == tagName:
            return i['Value']
        
def getInstances(prefix):
    instances = clientEc2.describe_instances( Filters=[ {'Name' : 'tag:Name', 'Values' : [ 'myalenti*' ] }] )
    print len(instances)
    for elem in instances['Reservations']:
        print(elem)
    myInstances = []
    for elem in instances['Reservations']:
        for inst in elem['Instances']:
            instId =  inst['InstanceId']
            instName = getTagValue("Name", inst['Tags'])
            #print inst['Tags']
            print(getTagValue("expire-on", inst['Tags']))
            mydate = datetime.date.today() + datetime.timedelta(30) 
            print(instId + " , " + instName + " , " + str(mydate))
            r = { "instanceId" : instId , "instName" : instName, "expireDate" : str(mydate)}
            myInstances.append(r)
    return myInstances


clientEc2 = boto3.client('ec2')
myInstances = getInstances("myalenti")
print(len(myInstances))
print(myInstances)
mydate = datetime.date.today() + datetime.timedelta(30) 
instList = []
for i in myInstances:
    instList.append( i['instanceId'])
print(instList)

resp = clientEc2.create_tags(Resources=instList, Tags=[ { "Key" : "expire-on" , "Value" : str(mydate)}])
print(resp['ResponseMetadata'])