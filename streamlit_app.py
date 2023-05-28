import streamlit as st
from my_project.langchain_agent import LangChainAgent  # Import your LangChain agent

class ChatApp:
    def __init__(self):
        self.agent = LangChainAgent()
        self.chat_history = []

    def add_message(self, user, message):
        self.chat_history.append({
            'user': user,
            'message': message
        })

    def chat(self):
        st.title('Chat with LangChain Agent')
        
        st.markdown("## Chat History")
        for chat in self.chat_history:
            st.markdown(f"**{chat['user']}**: {chat['message']}")

        user_input = st.text_input("Enter your message:")
        if st.button('Send'):
            self.add_message('You', user_input)
            response = self.agent.respond(user_input)  # Get the response from your agent
            self.add_message('LangChain Agent', response)
            

if __name__ == "__main__":
    chat_app = ChatApp()
    chat_app.chat()
