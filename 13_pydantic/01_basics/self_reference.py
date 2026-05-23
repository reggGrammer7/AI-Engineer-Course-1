from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None


comment = Comment(
    id=1,
    content="First Comment",
    replies=[
        Comment(
            id=2,
            content="reply 1",
            replies=[
                Comment(
                    id=4,
                    content="nested reply",
                    replies=[]
                )
            ]
        ),
        Comment(
            id=3,
            content="reply 2",
            replies=[]
        )
    ]
)

print(comment)
