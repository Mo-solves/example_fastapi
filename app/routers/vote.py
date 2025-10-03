from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models
from .auth2 import get_current_user
from ..schemas import Vote

router = APIRouter(prefix="/vote", tags=["votes"])


@router.post("/{id}", status_code=status.HTTP_201_CREATED)
def vote(
    vote_dir: Vote,
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    print(vote_dir.dir)
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} was not found",
        )

    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == post.id, models.Vote.user_id == current_user.id
    )
    found_vote = vote_query.first()
    if vote_dir.dir:
        if found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"user with id: {current_user.id} has  already liked the post with id: {id}",
            )
        new_vote = models.Vote(post_id=post.id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "Successfuly liked the post"}
    else:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Vote Does not exist"
            )
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "successfully unliked the post"}
