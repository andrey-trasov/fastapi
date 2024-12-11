from sqlalchemy.orm import Session

from models.users import Users
from schemas.authorization_schema import UserLoginSchema
from services.user_service import hash_password


async def checking_the_data(db: Session, creds: UserLoginSchema):
    bd_creds = db.query(Users).filter(Users.username == creds.username).first()
    if not bd_creds is None and bd_creds.password == await hash_password(creds.password):
        return True
    return False