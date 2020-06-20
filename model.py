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
    Local_Authority = Column(String)
    Constituency = Column(String)
    NUTS2_Spatial_Unit = Column(String)
    NUTS2_Spatial_Unit_Code = Column(String)
    OS_Grid_Easting = Column(String)
    OS_Grid_Northing = Column(String)
    Station_Facility_Owner = Column(String)
    Station_Group = Column(String)
    PTE_Urban_Area_Station = Column(String)
    London_Travelcard_Area = Column(String)
    Network_Rail_Region_of_station = Column(String)
    CRP_Line_Designation = Column(String)
    Entries_Exits_Full = Column(Integer)
    Entries_Exits_Reduced = Column(Integer)
    Entries_Exits_Season = Column(Integer)
    Entries_Exits_1819 = Column(Integer)
    Entries_Exits_1718 = Column(Integer)
    Interchanges_1819 = Column(Integer)
    Entries_Exits_1819_GBrank = Column(Integer)
    Entries_Exits_1718_GBrank = Column(Integer)
    Large_station_change_flag = Column(Float)
    Small_station_change_flag = Column(Float)
    Percent_Change = Column(Float)
    Explanation_of_large_change_1819 = Column(Integer)
    Source_for_explanation_of_large_change_1819 = Column(Integer)


    def __repr__(self):
        return "<Station(station_name='%s')>" % (self.station_name)



# A bunch of stuff to make the connection to the database work.
def dbconnect():
    engine = create_engine('sqlite:///stations.db', echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()