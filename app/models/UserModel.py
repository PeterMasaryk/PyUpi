from sqlmodel import Field, SQLModel

class UserModel(SQLModel, table=True):

    __tablename__ = "users"

    def __init__(self, id, username, email, star_sign):
        self.id = id
        self.username = username
        self.email = email
        self.star_sign = star_sign

    id: str = Field(primary_key=True)
    username: str = Field(index=True)
    email: str | None = Field(default=None, index=True)
    star_sign: str
