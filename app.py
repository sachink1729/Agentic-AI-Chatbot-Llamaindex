# flask app
from flask import Flask
from src.agent_controller import AgentController
from flask import request

app = Flask(__name__)   
agent_controller = AgentController()
agent = agent_controller.get_agent()


@app.route('/chat', methods=['POST'])
def chat():
    """
    Handles POST requests to /chat.
    
    This function expects a JSON payload with a single key 'query' with a string value.
    The query is processed by the agent and the response is returned as a JSON string.
    """
    
    data = request.get_json()
    query = data['query']
    response = agent.chat(query)
    return response.response, 200

@app.route('/ping',methods=['GET'])
def ping():
    """
    Handles GET requests to /ping.
    
    This function simply returns a string 'Alive' as a confirmation of the
    application being alive.
    """
    
    return "Alive", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3389, debug=True)