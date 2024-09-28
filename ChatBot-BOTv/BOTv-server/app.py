from fastapi import FastAPI
from requests import session

from SQLAlchemy_DB.main import get_chatbot_session_by_id,update_chatbot_session,create_chatbot_session
from BOTv import chatbot
from email_sender import send_email

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://deploy-chatbot-botv.onrender.com"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/chat_id/{chat_id}/")
def get_chat_data(chat_id: str):

    session = get_chatbot_session_by_id(chat_id)

    if session:
        return session
    else:
        return {"error": "Chat session not found"}


@app.put("/update_chat_data/{chat_id}/")
def update_chat_data(chat_id:str,data:dict):
    session = update_chatbot_session(chat_id,data)
    if session:
        return session
    else:
        return {"error": "Chat session not found"}


@app.post("/settings/")
def create_chat_data(data: dict):
    settings = data["chatbot"]["settings"]
    context = settings["contextData"]
    ui_messages = data["ui_messages"]
    max_words = int(settings["outputLength"])
    limit_summary = settings["limitSummary"]
    summary =  data["summary"]
    print("+++++++++++++++++++++++++++++++++++++++++++++++==")
    response,is_summarized,summary = chatbot(context,ui_messages,max_words,limit_summary,summary)
 
    return {"response": response,"isSummarized":is_summarized,"summary":summary}

@app.post("/conversationIdRequest/")
def send_chat_id_on_email(data: dict):
    email = data["email"]
    print(email)
    chat_id = create_chatbot_session()
    url = f"http://localhost:5173/chat/{chat_id}"
    message=f'Here is your chat conversation ID: {url}'
    response = send_email(recipient_email=email,subject='Explore Your Chat Conversation ID', message=message)
 
    return response