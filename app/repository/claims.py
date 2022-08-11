from botocore.exceptions import ClientError
from boto3.resources.base import ServiceResource

class ClaimsRepository:
    def __init__(self, db: ServiceResource) -> None:
        self.__db = db

    def get_all(self):
        table = self.__db.Table('Claims')
        response = table.scan()
        return response.get('Items', [])

    def get_claim(self, uid: str):
        try:
            table = self.__db.Table('Claims')
            response = table.get_item(Key={'uid': uid})
            return response['Item']
        except ClientError as e:
            raise ValueError(e.response['Error']['Message'])

    def create_claim(self, claim: dict):
        table = self.__db.Table('Claims')
        response = table.put_item(Item=claim)
        return claim

    def update_claim(self, claim: dict):
        table = self.__db.Table('Claims')
        response = table.update_item(
            Key={'uid': claim.get('uid')},
            UpdateExpression="""
                set
                    claim_type=:claim_type
            """,
            ExpressionAttributeValues={
                ':claim_type': claim.get('claim_type')
            },
            ReturnValues="UPDATED_NEW"
        )
        return response

    def delete_claim(self, uid: str):
        table = self.__db.Table('Claims')
        response = table.delete_item(
            Key={'uid': uid}
        )
        return response