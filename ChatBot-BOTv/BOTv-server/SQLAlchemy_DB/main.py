from sqlalchemy.orm import sessionmaker
from . import Models
 
Models.Base.metadata.create_all(Models.engine)

Session = sessionmaker(bind=Models.engine)
def update_chatbot_session(session_id, data: dict):
    with Session() as session:
 
        chatbot_session = session.query(Models.ChatbotSession).filter_by(id=session_id).first()

        if chatbot_session:
            session_data = data.get("chatbot")
            all_messages = data.get("all_messages")

            if session_data is not None:
                chatbot_session.session_data = session_data
            if all_messages is not None:
                chatbot_session.all_messages = all_messages

            session_id = chatbot_session.id

            session.commit()

        else:
            raise Exception("Chatbot session not found")

    print(f"ChatbotSession updated with ID: {session_id}")
    return session_id


data = {
    'chatbot': {
        'settings': {
            'botName': 'Initial AI Assistant',
            'contextLength': '500',
            'contextData': '',
            'outputLength': '50',
            'conversationId': '',
            'apiKey': '',
            'limitSummary': 1000
        },
        'ui_messages': [

        ],
        'summary': '',
    },
    'all_messages': [

    ],
}
def create_chatbot_session():
    session = Session()

    try:
        chatbot_session = Models.ChatbotSession(
            session_data=data.get('chatbot'),
            all_messages=data.get('all_messages')
        )

        session.add(chatbot_session)
        session.commit()

        print("Chatbot session saved successfully!")
        return chatbot_session.id

    except Exception as e:
        print(f"Error occurred: {e}")
        session.rollback()
    finally:
        session.close()






def get_all_sessions():
    session = Session()
    try:
        sessions = session.query(Models.ChatbotSession).all()
        return sessions
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        session.close()


from sqlalchemy.orm import sessionmaker

from sqlalchemy.exc import NoResultFound

Session = sessionmaker(bind=Models.engine)


def get_chatbot_session_by_id(session_id):
    session = Session()

    try:
        chatbot_session = session.query(Models.ChatbotSession).filter_by(id=session_id).one_or_none()

        if chatbot_session:
            return chatbot_session
        else:
            print(f"No session found with id: {session_id}")
            return None
    except NoResultFound:
        print(f"No result found for session id: {session_id}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        session.close()

if __name__ == "__main__":

    print(create_chatbot_session())
