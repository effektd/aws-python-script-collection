# Remove all associated rules for default security groups

This is a very simple and straightforward python script that will remove all ingress and egress rules for all AWS VPC default security groups in an account (and the region in which it is run).

The main reason for performing this is for compliance reasons, as the `default` security group should generally never be used for AWS services and should be subsequently locked down by default.

## How to use it

- Navigate to the parent directory containing `clean_default_sgs.py`
- Login to your AWS account and set the AWS region in which you wish to remove all default rules from
- Run the following command `python clean_default_sgs.py`
- The script will then remove any associated rules for all security groups named `default`
- **NOTE**: The script will handle default security groups not having ingress or egress rules to be revoked
- **NOTE**: A user cannot define a security group with a **group name** of `default`, this ensures that the default security group is compliant and secure for every VPC within an account