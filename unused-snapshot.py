import boto3

ec2 = boto3.resource('ec2', region_name='ap-south-1')

# Retrieve a list of all the self-owned snapshots in the region
snapshots = list(ec2.snapshots.filter(OwnerIds=['self']))

# Retrieve a list of all the volumes in the region
volumes = list(ec2.volumes.all())

# Create a set of all the snapshot IDs that are in use by volumes
used_snapshots = set([snapshot.snapshot_id for volume in volumes for snapshot in volume.snapshots.all()])

# Delete unused snapshots
for snapshot in snapshots:
    if snapshot.snapshot_id not in used_snapshots:
        snapshot.delete()
        print(f"Deleted unused snapshot {snapshot.snapshot_id}")
