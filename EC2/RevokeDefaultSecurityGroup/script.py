import json
import boto3
from botocore.exceptions import ClientError

if __name__ == "__main__":

    ec2_client = boto3.client('ec2')
    ec2_resource = boto3.resource('ec2')

    default_security_groups = ec2_client.describe_security_groups(
        Filters=[{'Name': 'group-name', 'Values': ['default']}])

    for default_group in default_security_groups['SecurityGroups']:
        group_id = default_group['GroupId']
        security_group_obj = ec2_resource.SecurityGroup(group_id)

        # Revoke All Ingress
        try:
            security_group_obj.revoke_ingress(
                IpPermissions=security_group_obj.ip_permissions)
            print("[Security Group: {}] All detected ingress rules have been removed".format(group_id))
        except ClientError as e:
            if e.response['Error']['Code'] == 'MissingParameter':
                print("[Security Group: {}] No ingress rules to be removed".format(group_id))
            else:
                print("[Security Group: {}] An unexpected error occurred".format(group_id))

        # Revoke All Egress
        try:
            security_group_obj.revoke_egress(
                IpPermissions=security_group_obj.ip_permissions_egress)
            print("[Security Group: {}] All detected egress rules have been removed".format(group_id))
        except ClientError as e:
            if e.response['Error']['Code'] == 'MissingParameter':
                print("[Security Group: {}] No egress rules to be removed".format(group_id))
            else:
                print("[Security Group: {}] An unexpected error occurred".format(group_id))
