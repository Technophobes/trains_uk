from sqlalchemy import Integer, Column, String, Float, ForeignKey, UniqueConstraint, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker


Base = declarative_base()

class Region(Base):
    __tablename__ = 'Region'
    id = Column(Integer, primary_key=True)
    region_name = Column(String, unique=True)

    def __repr__(self):
        return "<Region(region_name='%s')>" % (self.region_name)


class Station(Base):
    __tablename__ = 'Station'
    id = Column(Integer, primary_key=True)
    station_name = Column(String, unique=True)
    total_1819 = Column(Integer)
    region = relation("Region", backref = "Station")
    region_id = Column(Integer, ForeignKey('Region.id'))


    def __repr__(self):
        return "<Station(station_name='%s')>" % (self.station_name)



# A bunch of stuff to make the connection to the database work.
def dbconnect():
    engine = create_engine('sqlite:///stations.db', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()