import boto3

ec2 = boto3.client('ec2', region_name='ap-south-1')

# Retrieve a list of all the self-owned AMIs in the region
images = ec2.describe_images(Owners=['self'])['Images']

# Retrieve a list of all the instances and launch configurations in the region
instances = ec2.describe_instances()['Reservations']
launch_configs = boto3.client('autoscaling', region_name='ap-south-1').describe_launch_configurations()['LaunchConfigurations']

# Create a set of all the AMI IDs that are in use by instances or launch configurations
used_amis = set()
for instance in instances:
    for i in instance['Instances']:
        used_amis.add(i['ImageId'])
for lc in launch_configs:
        used_amis.add(lc['ImageId'])
print(used_amis)

# Create a list of all the self-owned AMIs that are not in use by any instances or launch configurations
unused_amis = []
for image in images:
    if image['ImageId'] not in used_amis:
    ec2.deregister_image(ImageId=image['ImageId'])
    print(f"Deleted unused AMI {image['ImageId']}")
