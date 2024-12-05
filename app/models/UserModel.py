from sqlmodel import Field, SQLModel

class UserModel(SQLModel, table=True):

    __tablename__ = "users"

    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    id: str = Field(primary_key=True)
    username: str = Field(index=True)
    email: str | None = Field(default=None, index=True)
