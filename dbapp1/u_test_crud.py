from app import db, Message

all_messages = Message.query.all()
print(all_messages)
