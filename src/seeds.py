from models import db, Users, Chats
def run():

    #Arrange the deletes in the opposite order of the models
    Chats.query.delete()
    Users.query.delete()
    
    # MYSQL database for gitpod
    db.session.execute("ALTER TABLE chats AUTO_INCREMENT = 1")
    db.session.execute("ALTER TABLE users AUTO_INCREMENT = 1")

    db.session.execute("ALTER TABLE Chats ADD CONSTRAINT user1_username_username FOREIGN KEY (user1_username) REFERENCES USERS(username)")
    db.session.execute("ALTER TABLE Chats ADD CONSTRAINT user1_username_username FOREIGN KEY (user2_username) REFERENCES USERS(username)")
 
    # POSTGRES database for heroku
    # db.session.execute("ALTER SEQUENCE chats_id_seq RESTART")
    # db.session.execute("ALTER SEQUENCE users_id_seq RESTART")


    ##################
    #     USERS
    ##################
    Issac = Users(
        username = 'kolis10'
    )
    db.session.add(Issac)
    Naz = Users(
        username = 'Naz'
    )
    db.session.add(Naz)
    Chouerlee = Users(
        username = 'Curly-Fry'
    )
    db.session.add(Chouerlee)
    Zion = Users(
        username = 'Coder'
    )
    db.session.add(Zion)
    Rajae = Users(
        username = 'Rager'
    )
    db.session.add(Rajae)
    Anthony = Users(
        username = 'Tony'
    )
    db.session.add(Anthony)

    ##################
    #     CHATS
    ##################
    db.session.add(Chats(
        user1_username = Chouerlee,
        user2_username = Anthony,
        writer_username = Chouerlee,
        message = "'Sup"
    ))
    db.session.add(Chats(
        user1_username = Issac,
        user2_username = Naz,
        writer_username = Issac,
        message = "Hey"
    ))
    db.session.add(Chats(
        user1_username = Naz,
        user2_username = Zion,
        writer_username = Naz,
        message = "Konichiwa"
    ))
    db.session.add(Chats(
        user1_username = Zion,
        user2_username = Rajae,
        writer_username = Zion,
        message = "Dude"
    ))
    db.session.add(Chats(
        user1_username = Rajae,
        user2_username = Chouerlee,
        writer_username = Rajae,
        message = "Yo"
    ))
    db.session.add(Chats(
        user1_username = Anthony,
        user2_username = Issac,
        writer_username = Anthony,
        message = "Hi"
    ))
    db.session.commit()
    return 'seeds ran successfully'