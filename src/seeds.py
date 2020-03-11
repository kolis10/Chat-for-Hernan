from models import db, Chats, Messages, Invites
from datetime import datetime, timedelta

def run():

    #Arrange the deletes in the opposite order of the models
    Invites.query.delete()
    Messages.query.delete()
    Chats.query.delete()
    
    # MYSQL database for gitpod
    db.session.execute("ALTER TABLE invites AUTO_INCREMENT = 1")
    db.session.execute("ALTER TABLE messages AUTO_INCREMENT = 1")
    db.session.execute("ALTER TABLE chats AUTO_INCREMENT = 1")

    # POSTGRES database for heroku
    # db.session.execute("ALTER SEQUENCE messages_id_seq RESTART")
    # db.session.execute("ALTER SEQUENCE chats_id_seq RESTART")

    db.session.add(Chats())
    db.session.add(Chats())
    db.session.add(Chats())
    db.session.add(Chats())
    db.session.add(Chats())
    db.session.add(Chats())

    now = datetime.utcnow()


    ##################
    #     INVITES
    ##################
    db.session.add(Invites(
        chat_id = 1,
        username = "Naz"
    ))
    db.session.add(Invites(
        chat_id = 1,
        username = "koLiS10"
    ))


    ##################
    #     MESSAGES
    ##################
    db.session.add(Messages(
        chat_id = 1,
        writer_username = "kolis10",
        message = "'Sup",
        created_at = now
    ))
    db.session.add(Messages(
        chat_id = 2,
        writer_username = "Naz",
        message = "Konichiwa",
        created_at = now
    ))
    db.session.add(Messages(
        chat_id = 3,
        writer_username = "Curly-Fry",
        message = "Hey",
        created_at = now
    ))
    db.session.add(Messages(
        chat_id = 4,
        writer_username = "Coder",
        message = "Dude",
        created_at = now
    ))
    db.session.add(Messages(
        chat_id = 5,
        writer_username = "Rager",
        message = "Yo",
        created_at = now
    ))
    db.session.add(Messages(
        chat_id = 6,
        writer_username = "Tony",
        message = "Hi",
        created_at = now
    ))
    ############################################
    db.session.add(Messages(
        chat_id = 1,
        writer_username = "Naz",
        message = "Konichiwa, kolis10",
        created_at = now + timedelta(minutes=2)
    ))
    db.session.add(Messages(
        chat_id = 2,
        writer_username = "kolis10",
        message = "'Sup, Naz",
        created_at = now + timedelta(minutes=2)
    ))
    db.session.add(Messages(
        chat_id = 3,
        writer_username = "Tony",
        message = "Hi, Curly-Fry",
        created_at = now + timedelta(minutes=2)
    ))
    db.session.add(Messages(
        chat_id = 4,
        writer_username = "Rager",
        message = "Yo, Coder",
        created_at = now + timedelta(minutes=2)
    ))
    db.session.add(Messages(
        chat_id = 5,
        writer_username = "Coder",
        message = "Dude, Rager",
        created_at = now + timedelta(minutes=2)
    ))
    db.session.add(Messages(
        chat_id = 6,
        writer_username = "Curly-Fry",
        message = "Hey, Tony",
        created_at = now + timedelta(minutes=2)
    ))
    
    db.session.commit()
    return 'seeds ran successfully'