import graphene
import Eemail.schema
from Eemail.schema import Mutation
class Query(Eemail.schema.Query,graphene.ObjectType):
    pass


class Mutation(Mutation,graphene.ObjectType):
     pass






schema=graphene.Schema(query=Query,mutation=Mutation)