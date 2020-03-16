from sqlalchemy import Column, Integer, String, Date, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


def get_engine(conn_str, echo = True):
    return create_engine(conn_str, echo = echo)


Base = declarative_base()


class ChideoEmployee(Base):
    '''Anybody who works at ChIDEO'''
    __tablename__ = "chideoers"
    id = Column(Integer, primary_key = True)
    name = Column(String(50))
    email = Column(String(50))
    host_slots = relationship("HostEngagements", back_populates = "host")


    def serialize(self):
        return {
            "id": self.id, 
            "name": self.name, 
            "email": self.email
        }


class HostEngagements(Base):
    '''Folks who have already been selected to host MLM, along with the week 
    they hosted'''
    __tablename__ = "mlm_hosts"
    id = Column(Integer, primary_key = True)
    chideoer_id = Column(Integer, ForeignKey("chideoers.id"))
    week_of_hosting = Column(Date)
    host = relationship("ChideoEmployee", back_populates = "host_slots")

    def serialize(self):
        return {
            "id": self.id, 
            "chideoer_id": self.chideoer_id, 
            "week_of_hosting": self.week_of_hosting
        }

