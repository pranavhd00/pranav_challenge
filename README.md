# pranav_challenge

# Using terraform and AWS services, a scalable and static webpage is built.

# A terraform template will handle web application deployment in AWS Auto Scaling Group behind Elastic Load Balancer and distributes traffic across the EC2 Instance in ASG. 
# Route53 Record Set record with Alias Target as a ELB DNS Name.
# Secure and scalable as incorporating Autoscaling groups and Load balancer

Steps:
1. Create ASG, Launch Config for ASg
2. Create SG for Ec2 instances
3. Create ELB
4. Create SG for ELB-
4. Route53 for DNS mapping- Record set for ELB DNS Named
5. Userdata scripts for certs and rewrites.


# Credit card validation

creditcardVal.py
