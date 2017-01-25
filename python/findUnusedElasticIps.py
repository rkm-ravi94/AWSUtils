import boto
from boto import ec2
conn = ec2.connect_to_region('us-east-1')
addrs = conn.get_all_addresses()
for a in addrs:
   if a.instance_id is None:
      print a.public_ip


findElasticIps = FindElasticIps('us-east-1')
elasitcIps = findElasticIps.getElasticIps()
