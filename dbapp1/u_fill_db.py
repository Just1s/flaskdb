from app import db, Message

db.create_all()

jonas = Message('Jonas', 'jonas@gmail.com', 'Labas rytas!')
rokas = Message('Rokas', 'rokas@gmail.com', 'Labas vakaras!')
justas = Message('Justas', 'justas@gmail.com', 'Viso gero!')
dainius = Message('Dainius', 'dainius@gmail.com', 'Laba diena!')

db.session.add_all([jonas, rokas, justas, dainius])
db.session.commit()

print(jonas.id)
print(rokas.id)
print(justas.id)
print(dainius.id)
