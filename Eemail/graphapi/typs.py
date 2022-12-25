from Eemail.models import Message,User
from  graphene_django.types import DjangoObjectType



class MessageType(DjangoObjectType):
    class Meta:
        model=Message

class UserType(DjangoObjectType):
    class Meta:
        model=User        




