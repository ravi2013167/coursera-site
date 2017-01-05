import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Team(Base):
    __tablename__ = 'team'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)


class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key = True)
    team_id = Column(Integer, primary_key = False)
    name = Column(String(80), nullable = False)
    country = Column(String(250), nullable = False)
    info = Column(String(250), nullable = False)
    career = Column(String(250), nullable = False)
    batting_style = Column(String(250), nullable = False)
    bowling_style = Column(String(250), nullable = False)
    picture = Column(String(250))


class Batsman(Base):
    __tablename__ = 'batsman'

    id = Column(Integer, primary_key = True)
    stance_type = Column(String(80), nullable = False)
    foot_position = Column(String(80), nullable = False)
    shot = Column(String(280), nullable = False)
    #user = relationship(User)
    #menuItems = relationship("MenuItem", cascade="all, delete-orphan")
    '''@property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }
'''
class Bowler(Base):
    __tablename__ = 'bowler'

    id = Column(Integer, primary_key = True)
    ball_type = Column(String(80), nullable = False)
    

class Fielder(Base):
    __tablename__ = 'fielder'

    id = Column(Integer, primary_key = True)
    field_type = Column(String(80), nullable = False)
    

class PlayerStrength(Base):
    __tablename__ = 'player_strength'

    id = Column(Integer, primary_key = True)
    strength_detail = Column(String(80), nullable = False)
    

class PlayerWeakness(Base):
    __tablename__ = 'player_weakness'

    id = Column(Integer, primary_key = True)
    weakness_detail = Column(String(80), nullable = False)

class PlayerMoment(Base):
    __tablename__ = 'player_moment'

    id = Column(Integer, primary_key = True)
    moment_type = Column(String(80), nullable = False)
    moment_name = Column(String(80), nullable = False)

class Video(Base):
    __tablename__ = 'video'

    id = Column(Integer, primary_key = True)
    video_type = Column(String(80), nullable = False)
    video_name = Column(String(80), nullable = False)
    video_url = Column(String(980), nullable = False)

    

#class MenuItem(Base):
    '''__tablename__ = 'menu_item'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)



    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }


'''

engine = create_engine('sqlite:///cricdb.db')
'''
from sqlalchemy import MetaData
meta = MetaData()
import contextlib
with contextlib.closing(engine.connect()) as con:
    trans = con.begin()
    for table in reversed(meta.sorted_tables):
        con.execute(table.delete())
    trans.commit()
'''

Base.metadata.create_all(engine)
