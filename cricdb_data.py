from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cricdb_setup import Team, Player, Base, Batsman, Bowler, Fielder, PlayerStrength, PlayerWeakness, PlayerMoment, Video

engine = create_engine('sqlite:///cricdb.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

Team1 = Team(id = 1, name='India')

session.add(Team1)
session.commit()

# Create dummy player
Player1 = Player(id = 1, team_id = 1, name="Virat Kohli", country="India", info='Born Nov 05, 1988 (28 years) Birth Place Delhi Nickname Kohli Height 5 ft 9 in (175 cm) Role Batsman Batting Style Right Handed Bat Bowling Style Right-arm medium', career='blank', batting_style='blank', bowling_style='blank',
             picture='vk.jpg')
session.add(Player1)
session.commit()

# Menu for UrbanBurger
Batsman1 = Batsman(id=1, stance_type="front on", foot_position="front foot", shot="straight drive")

session.add(Batsman1)
session.commit()

Video1 = Video(id=1, video_type='batsman', video_name='front on front foot straight drive', video_url='google.com')
session.add(Video1)
session.commit()

print ("added menu items!")
