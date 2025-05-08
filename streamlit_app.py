import streamlit as st
import requests

# Set your N8n webhook URL here (ensure it's accessible, use ngrok for local testing if needed)
WEBHOOK_URL = "https://het-pragetx.app.n8n.cloud/webhook/f406671e-c954-4691-b39a-66c90aa2f103/chat"

def get_chatbot_response(user_message):
    try:
        # post the user message as JSON payload
        response = requests.post(WEBHOOK_URL, json={"message": user_message})
        if response.ok:
            return response.json().get("reply", "No reply received")
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Request failed: {e}"

def main():
    st.title("N8n Chatbot Demo")
    st.write("Type your message and get a response from the chatbot via an N8n workflow.")

    user_input = st.text_input("Your Message:")

    if st.button("Send"):
        if user_input:
            reply = get_chatbot_response(user_input)
            st.write("Chatbot Reply:", reply)
        else:
            st.write("Please enter a message.")

if __name__ == "__main__":
    main()