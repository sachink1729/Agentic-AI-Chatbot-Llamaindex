import gradio as gr
from src.agent_controller import AgentController
agent_controller = AgentController()
agent = agent_controller.get_agent()

def respond(message, history):
    # {"role": "user", "content": "message"}
    """
    Function to handle user input and return a response from the agent.

    Args:
        message (str): The user's message.
        history (list): The chat history.

    Returns:
        dict: A dictionary with the keys "role" and "content", where "role" is "assistant" and "content" is the response message.
    """
    response = agent.chat(message)
    response = {"role": "assistant", "content": response.response}
    return response    

def reset_agent():
    """
    Resets the agent's current chat history.

    This function prints the current chat history of the agent for logging purposes and
    resets it to clear any past interactions. This is useful for starting a new conversation
    session without any prior context.
    """
    print("resetting agent current chat history: ", agent.chat_history)
    agent.reset()

with gr.Blocks(theme=gr.themes.Default()) as demo:
    gr.Markdown("## Agentic Chatbot")
    gr.ChatInterface(
        respond,
        type="messages",
        chatbot=gr.Chatbot(height=450),
        textbox=gr.Textbox(placeholder="Ask me a maths question and hit enter", container=False, scale=7),
        description="Ask me anything about maths",
        theme="default"
    )
    button_reset =gr.Button("Reset Conversation", elem_id="reset")
    button_reset.click(reset_agent, inputs=[], outputs=[])

demo.launch(share=False)