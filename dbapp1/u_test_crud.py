from app import db, Message

# READ
all_messages = Message.query.all()
print(all_messages)

message_1 = Message.query.get(1)
print(message_1)

message_dainius = Message.query.filter_by(name='Dainius').all()
print(message_dainius)

# UPDATE
dainius = Message.query.get(4)
dainius.email = 'dainius@yahoo.com'
db.session.commit()

# DELETE
jonas = Message.query.get(1)
db.session.delete(jonas)
db.session.commit()

print(Message.query.all())
