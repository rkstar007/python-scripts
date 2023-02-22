import boto3

# Create an EC2 client
ec2 = boto3.client('ec2')

# Get a list of all EBS volumes
volumes = ec2.describe_volumes()

# Filter the list to include only volumes that are not attached to any instances
unattached_volumes = [v for v in volumes['Volumes'] if len(v['Attachments']) == 0]

# Delete each unattached volume
for v in unattached_volumes:
    volume_id = v['VolumeId']
    print(f"Unattached volume found: {volume_id}")
    print(f"Deleting volume {volume_id}...")
    response = ec2.delete_volume(VolumeId=volume_id)
    print(f"Response: {response}")
  
