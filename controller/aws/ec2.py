import csv
import boto3
from utils.otalogger import OtaLogger

# get details about EC2 instances, volumes, key-pairs and security groups..
class EC2:
    def __init__(self):
        lobj = OtaLogger()
        self.logger = lobj.getLogger()
        self.aKey = input("Enter AWS Account's Access Key: ")
        self.sKey = input("Enter AWS Account's Secret Key: ")
        self.region = input("Enter AWS Account's Region: ")
        self.outputFile = './output/ec2-details.csv'

    def  displayEC2Details(self):
        # establish connection to AWS EC2..
        ec2 = boto3.resource(
            'ec2',
            aws_access_key_id=self.aKey,
            aws_secret_access_key=self.sKey,
            region_name=self.region
        )

        # open an empty csv file in the output directory..
        try:
            with open(self.outputFile, "w") as my_empty_csv:
                print("Created ec2-details.csv file in /output directory")
        except Exception as e:
            self.logger.critical(str(e))
            print(e)

        # EC2 INSTANCE DETAILS
        # append row of headings to csv file..
        try:
            toAdd = ["Instance_ID", "Instance_Type", "Instance_PublicIpv4", "Instance_AMI", "Instance_State"]
            with open(self.outputFile, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(toAdd)
        except Exception as e:
            self.logger.critical(str(e))
            print(e)

        # traverse through each running ec2 machine and append details to csv file..
        noOfEc2 = 0
        try:
            for instance in ec2.instances.all():
                noOfEc2 += 1
                fields = [instance.id, instance.instance_type, instance.public_ip_address, instance.image.id,
                          instance.state]
                with open(self.outputFile, 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(fields)
        except Exception as e:
            self.logger.critical(str(e))
            print(e)

        # append total no of ec2 instance running to the csv file..
        try:
            toAdd = ["Total no of Instances", noOfEc2]
            with open(self.outputFile, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(toAdd)
        except Exception as e:
            self.logger.critical(str(e))
            print(e)

        # append blank rows to csv file..
        try:
            with open(self.outputFile, 'a') as f:
                writer = csv.writer(f)
                writer.writerow([])
                writer.writerow([])
        except Exception as e:
            self.logger.critical(str(e))
            print(e)

        # VOLUMES
        # append row of headings to csv file..
        try:
            toAdd = ["Volume_ID", "Volume_Size", "Volume_Type", "IOPS", "Snapshot_ID", "Create_time",
                     "Availability Zone", "State"]
            with open(self.outputFile, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(toAdd)
        except Exception as e:
            self.logger.critical(str(e))
            print(e)

        # traverse through each running volume and append details to csv file..
        noOfVolume = 0
        try:
            for volume in ec2.volumes.all():
                noOfVolume += 1
                fields = [volume.volume_id, volume.size, volume.volume_type, volume.iops, volume.snapshot_id,
                          volume.create_time, volume.availability_zone, volume.size]
                with open(self.outputFile, 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(fields)
        except Exception as e:
            self.logger.critical(str(e))
            print(e)


        # append total no of volumes to the csv file..
        try:
            toAdd = ["Total no of Volumes", noOfVolume]
            with open(self.outputFile, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(toAdd)
        except Exception as e:
            self.logger.critical(str(e))
            print(e)

        # append blank rows to csv file..
        try:
            with open(self.outputFile, 'a') as f:
                writer = csv.writer(f)
                writer.writerow([])
                writer.writerow([])
        except Exception as e:
            self.logger.critical(str(e))
            print(e)

        # KEY PAIR
        # append row of headings to csv file..
        noOfKeyPair = 0
        try:
            toAdd = ["Key_Name", "Key_Fingerprint"]
            with open(self.outputFile, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(toAdd)
        except Exception as e:
            self.logger.critical(str(e))
            print(e)

        # traverse through each active key pair and append details to csv file..
        try:
            for key_pair in ec2.key_pairs.all():
                noOfKeyPair += 1
                fields = [key_pair.key_name, key_pair.key_fingerprint]
                with open(self.outputFile, 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(fields)
        except Exception as e:
            self.logger.critical(str(e))
            print(e)

        # append total no of key pairs to the csv file..
        try:
            toAdd = ["Total no of key pairs", noOfKeyPair]
            with open(self.outputFile, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(toAdd)
        except Exception as e:
            self.logger.critical(str(e))
            print(e)

        # append blank rows to csv file..
        try:
            with open(self.outputFile, 'a') as f:
                writer = csv.writer(f)
                writer.writerow([])
                writer.writerow([])
        except Exception as e:
            self.logger.critical(str(e))
            print(e)

        # SECURITY GROUPS
        # append row of headings to csv file..
        try:
            toAdd = ["Group_Id", "Group_Name", "VPC_ID", "Owner", "Description"]
            with open(self.outputFile, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(toAdd)
        except Exception as e:
            self.logger.critical(str(e))
            print(e)

        # traverse through each security group and append details to csv file..
        noOfSecurityGroup = 0
        try:
            for sg in ec2.security_groups.all():
                noOfSecurityGroup += 1
                fields = [sg.group_id, sg.group_name, sg.vpc_id, sg.owner_id, sg.description]
                with open(self.outputFile, 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow(fields)
        except Exception as e:
            self.logger.critical(str(e))
            print(e)

        # append total no of seurity groups to the csv file.
        try:
            toAdd = ["Total no of Security groups", noOfSecurityGroup]
            with open(self.outputFile, 'a') as f:
                writer = csv.writer(f)
                writer.writerow(toAdd)
        except Exception as e:
            self.logger.critical(str(e))
            print(e)

        # append summary of EC2 resources to the csv file..
        try:
            with open(self.outputFile, 'a') as f:
                writer = csv.writer(f)
                writer.writerow([])
                writer.writerow([])
                writer.writerow(["SUMMARY"])
                writer.writerow(['EC2 INSTANCES', 'VOLUMES', 'KEY PAIRS', 'SECURITY GROUPS'])
                writer.writerow([noOfEc2, noOfVolume, noOfKeyPair, noOfSecurityGroup])
        except Exception as e:
            self.logger.critical(str(e))
            print(e)

