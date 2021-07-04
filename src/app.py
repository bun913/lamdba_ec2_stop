import boto3
from botocore.exceptions import ClientError
from response import ResponseHandler

response = ResponseHandler()


def lambda_handler(event, context):
    instances = get_ec2_instances()
    try:
        instances.stop()
    except ClientError as e:
        response.append_eroor(type="ClientError", message=str(e))
        return response.get_errors()
    except Exception as e:
        response.append_eroor(type="UnExpectedError", message=str(e))
        return response.get_errors()
    id_list = [instance.id for instance in instances]
    return response.get_respose(",".join(id_list))


def get_ec2_instances():
    """EC2インスタンスを取得
    """
    ec2 = boto3.resource('ec2')
    filter = [
        {
            'Name': 'Reboot',
            'Values': ['True']
        }
    ]
    result = ec2.instances.filter()
    return result
