import boto3

ec2_resource = boto3.resource('ec2')

# Make a list of existing volumes
all_volumes = ec2_resource.volumes.all()
volumes = [volume.volume_id for volume in all_volumes]

# Find snapshots without existing volume
snapshots = ec2_resource.snapshots.filter(OwnerIds=['self'])

for snapshot in snapshots:
    if snapshot.volume_id not in volumes:
       delete_response = ec2_client.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
