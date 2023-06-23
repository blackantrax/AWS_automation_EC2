import boto3

# Configuration des informations d'identification AWS
aws_access_key_id = 'VOTRE_ACCESS_KEY'
aws_secret_access_key = 'VOTRE_SECRET_KEY'
region_name = 'votre-region-aws'  # Par exemple, 'us-west-2' pour la région de l'Oregon

# Création du client EC2
ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          region_name=region_name)

# Définition des paramètres pour la création de l'instance EC2
instance_params = {
    'ImageId': 'ami-xxxxxxxx',  # ID de l'image Amazon Machine (AMI) à utiliser
    'InstanceType': 't2.micro',  # Type d'instance
    'MinCount': 1,  # Nombre minimum d'instances à lancer
    'MaxCount': 1,  # Nombre maximum d'instances à lancer
    'KeyName': 'votre-key-pair',  # Nom de votre paire de clés EC2
    'SecurityGroupIds': ['votre-security-group'],  # Liste des IDs des groupes de sécurité
    'SubnetId': 'votre-subnet'  # ID du sous-réseau VPC
}

# Création de l'instance EC2
response = ec2_client.run_instances(**instance_params)

# Récupération de l'ID de l'instance créée
instance_id = response['Instances'][0]['InstanceId']

print(f"L'instance EC2 avec l'ID {instance_id} a été créée.")
