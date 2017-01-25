import boto
import sys
from boto import ec2

function getUnusedVolumes() {
    connection=ec2.connect_to_region('us-east-1')
    volumes=connection.get_all_volumes()
    for volume in volumes:
       instance_id=volume.attach_data.instance_id
       if instance_id is None:
          print "Unattached Volume is ",volume
    retrun volumes
}

getUnusedVolumes 'us-east-1'
