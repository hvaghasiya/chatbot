# import streamlit as st
# from openai import OpenAI

# # Show title and description.
# st.title("💬 Chatbot")
# st.write(
#     "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
#     "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
#     "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
# )

# # Ask user for their OpenAI API key via `st.text_input`.
# # Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# # via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
# openai_api_key = st.text_input("OpenAI API Key", type="password")
# if not openai_api_key:
#     st.info("Please add your OpenAI API key to continue.", icon="🗝️")
# else:

#     # Create an OpenAI client.
#     client = OpenAI(api_key=openai_api_key)

#     # Create a session state variable to store the chat messages. This ensures that the
#     # messages persist across reruns.
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # Display the existing chat messages via `st.chat_message`.
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # Create a chat input field to allow the user to enter a message. This will display
#     # automatically at the bottom of the page.
#     if prompt := st.chat_input("What is up?"):

#         # Store and display the current prompt.
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         # Generate a response using the OpenAI API.
#         stream = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#             ],
#             stream=True,
#         )

#         # Stream the response to the chat using `st.write_stream`, then store it in 
#         # session state.
#         with st.chat_message("assistant"):
#             response = st.write_stream(stream)
#         st.session_state.messages.append({"role": "assistant", "content": response})



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