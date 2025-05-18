import strawberry
from strawberry.fastapi import GraphQLRouter
from typing import List, Optional
from models import Feedback
from dataclasses import replace
from datetime import datetime
FEEDBACKS = []

@strawberry.type
class FeedbackType:
    id: int
    userId: str
    productId: str
    rating: int
    comment: str
    date: str

@strawberry.input
class FeedbackInput:
    userId: str
    productId: str
    rating: int
    comment: str

@strawberry.type
class Query:
    @strawberry.field
    def feedbacks(self) -> List[FeedbackType]:
        return FEEDBACKS

    @strawberry.field
    def feedbackById(self, id: int) -> Optional[FeedbackType]:
        return FEEDBACKS[id] if id < len(FEEDBACKS) else None

    @strawberry.field
    def feedbackByUser(self, userId: str) -> List[FeedbackType]:
        return [f for f in FEEDBACKS if f.userId == userId]

    @strawberry.field
    def feedbackByProduct(self, productId: str) -> List[FeedbackType]:
        return [f for f in FEEDBACKS if f.productId == productId]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def createFeedback(self, input: FeedbackInput) -> FeedbackType:
        global FEEDBACKS
        new_id = len(FEEDBACKS)
        new_feedback = FeedbackType(
            id=new_id,
            userId=input.userId,
            productId=input.productId,
            rating=input.rating,
            comment=input.comment,
            date=datetime.now().isoformat()
        )
        FEEDBACKS.append(new_feedback)
        return new_feedback

    @strawberry.mutation
    def deleteFeedback(self, id: int) -> bool:
        global FEEDBACKS
        if id >= len(FEEDBACKS):
            return False
        FEEDBACKS = [f for i, f in enumerate(FEEDBACKS) if i != id]
        return True

schema = strawberry.Schema(Query, Mutation)

graphql_app = GraphQLRouter(schema)