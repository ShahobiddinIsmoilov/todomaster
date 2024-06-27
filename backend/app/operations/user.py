from sqlalchemy.orm import Session

from ..models import models
from ..schemas import schemas


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    fake_hashed_password = user.password + "halflife2"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# def check_credentials(db: Session, )