'''
Created on 2017/03/17

@author: ktsuchi
'''
import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances(Filters=[
    {'Name': 'tag:'+'OnTimeStartStopInstance', 'Values': ['1']}
])

instancelist = []

for reservation in (response["Reservations"]):
    for instance in reservation["Instances"]:
        instancelist.append(instance["InstanceId"])

if len(instancelist) == 0:
    returnmsg = 'No resources !'
else:
    returnmsg = ec2.stop_instances(
        InstanceIds=instancelist
    )

print returnmsg

