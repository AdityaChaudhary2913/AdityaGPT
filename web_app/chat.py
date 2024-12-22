from web_app.api_client import GroqClient

class ChatManager:
    def __init__(self):
        self.client = GroqClient()
        self.conversation_history = []

    def add_message(self, role, content):
        self.conversation_history.append({"role": role, "content": content})

    def get_response(self, user_message):
        self.add_message("user", user_message)
        if any(keyword in user_message.lower() for keyword in ["what is", "define"]):
            prompt = f"Provide a concise definition of: {user_message}"
        elif "explain" in user_message.lower() or "code" in user_message.lower():
            prompt = f"Explain clearly with examples: {user_message}"
        else:
            prompt = f"Respond concisely to: {user_message}"
        messages = [{"role": "user", "content": prompt}]
        ai_response = self.client.get_response(messages)
        self.add_message("assistant", ai_response)
        return ai_response