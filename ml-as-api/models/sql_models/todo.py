from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, relationship
from user import Base

class TODO(Base):
   __tablename__ = "todos"
   id = Column(Integer, primary_key=True, index=True)
   text = Column(String, index=True)
   completed = Column(Boolean, default=False)
   owner_id = Column(Integer, ForeignKey("users.id"))
   owner = relationship("User", back_populates="todos")
