# Revoke all associated ingress/egress rules for default security groups

This is a very simple and straightforward python script that will remove all ingress and egress rules for all AWS VPC default security groups in an AWS account (and the region in which the script is run).

The main reason for performing this is for compliance reasons, as the `default` security group should generally never be used for AWS services and should be subsequently locked down by default.

## How to use it

- Open a terminal window
- Navigate to the parent directory containing the `revoke_default_sgs.py` script
- Login (or be logged into) to your AWS account and set the AWS region in which you wish to execute this script
- Run the following command `python revoke_default_sgs.py`
- The script will then remove any associated ingress/egress rules for all security groups named `default`
- **NOTE**: The script will handle default security groups not having ingress or egress rules to be revoked
- **NOTE**: A user cannot define a security group with a **group name** of `default`, this ensures that the default security group is compliant and secure for every VPC within an account

## Example print output


**Both ingress and egress rules detected and removed**
```
[Security Group: sg-09acfaa7029c5d72a] Ingress rules have been deleted
[Security Group: sg-09acfaa7029c5d72a] Egress rules have been deleted
[Security Group: sg-0d42ac3037d8e7db9] Ingress rules have been deleted
[Security Group: sg-0d42ac3037d8e7db9] Egress rules have been deleted
```
**Only egress rules detected and removed**
```
[Security Group: sg-09acfaa7029c5d72a] No ingress rules to be removed
[Security Group: sg-09acfaa7029c5d72a] Egress rules have been deleted
[Security Group: sg-0d42ac3037d8e7db9] No ingress rules to be removed
[Security Group: sg-0d42ac3037d8e7db9] Egress rules have been deleted
```
**One ingress and one egress rule detected and removed**
```
[Security Group: sg-09acfaa7029c5d72a] Ingress rules have been deleted
[Security Group: sg-09acfaa7029c5d72a] No egress rules to be removed
[Security Group: sg-0d42ac3037d8e7db9] No ingress rules to be removed
[Security Group: sg-0d42ac3037d8e7db9] Egress rules have been deleted
```
**No rules detected to be removed**
```
[Security Group: sg-09acfaa7029c5d72a] No ingress rules to be removed
[Security Group: sg-09acfaa7029c5d72a] No egress rules to be removed
[Security Group: sg-0d42ac3037d8e7db9] No ingress rules to be removed
[Security Group: sg-0d42ac3037d8e7db9] No egress rules to be removed
```