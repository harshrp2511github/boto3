import controller.aws.ec2 as ec2

def ec2data():
    myec2 = ec2.EC2()
    myec2.displayEC2Details()


if __name__ == "__main__":
    ec2data()
