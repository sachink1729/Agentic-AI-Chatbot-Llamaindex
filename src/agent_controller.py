from llama_index.core.agent import FunctionCallingAgent
from llama_index.core.tools import FunctionTool
from src.generators import Generators
from src.tools import *
from src.utils.app_logger import GenericLogger

logger = GenericLogger().get_logger()


add_tool = FunctionTool.from_defaults(fn=add)
multiply_tool = FunctionTool.from_defaults(fn=multiply)
miscellaneous_tool = FunctionTool.from_defaults(fn=miscellaneous)
sin_tool = FunctionTool.from_defaults(fn=calculate_sin)
cos_tool = FunctionTool.from_defaults(fn=calculate_cos)
log_tool = FunctionTool.from_defaults(fn=calculate_log)
exp_tool = FunctionTool.from_defaults(fn=calculate_power)
real_number_tool = FunctionTool.from_defaults(fn=only_real_numbers)
convert_to_real_number_tool = FunctionTool.from_defaults(fn=convert_to_real_number)
divide_tool = FunctionTool.from_defaults(fn=divide)
subtract_tool = FunctionTool.from_defaults(fn=subtract)
greet_user_tool = FunctionTool.from_defaults(fn=greet_user_and_ask_name)
ask_name_tool = FunctionTool.from_defaults(fn=ask_name)
update_name_tool = FunctionTool.from_defaults(fn=update_name)

class AgentController:
    def __init__(self):        
        """
        Initializes the AgentController class.

        This method creates an instance of the AgentController class with the LLaMA model and the system prompt.

        The system prompt is a string that is provided to the LLaMA model to generate responses.
        """

        logger.info("creating AgentController")
        self.llm = Generators().get_llm()
        self.system_prompt = """
                                INSTRUCTIONS: You are a maths tools expert. You are capable to have chain of thoughts and You will only use the tools available to you and without getting the function output you wouldn't proceed.

                                avoid getting into this mess like this:

                                Calling function: subtract with args: {"a": {"function": "subtract", "args": [{"function": "calculate_power", "args": [9, 16]}, {"function": "calculate_power", "args": [7, 18]}]}, "b": 3281711}
                                
                                always pass the desired inputs to the functions you call.

                                NOTE: You will ALWAYS evaluate the user's query and perfom query classification and provide three things:
                                answer, tool_used, reasoning.
                                
                                like this:

                                Answer: answer
                                - Tool Used: tool_name
                                - Reasoning: reasoning for using the tool
                                

                                An example:

                                Answer: 21.0
                                - Tool Used: multiply
                                - Reasoning: The tool was used to calculate the product of two numbers.
                                
                                
                                Solve the queries STEP by STEP and feel free to use the tools available to you and do not hallucinate or make assumptions.
                                """
        self.agent = self.get_agent()
        logger.info("AgentController created")
    def get_agent(self):
        
        """
        Creates and returns a FunctionCallingAgent initialized with a set of tools and the specified language model.

        The agent is configured to use a variety of mathematical and utility tools, 
        and is provided with a system prompt for operation. It logs the creation process.

        :return: An initialized FunctionCallingAgent instance.
        """
        logger.info("creating Agent")
        agent = FunctionCallingAgent.from_tools([multiply_tool, add_tool, sin_tool, cos_tool, log_tool, exp_tool, 
                                                 real_number_tool ,convert_to_real_number_tool, miscellaneous_tool,
                                                 divide_tool, subtract_tool, greet_user_tool, ask_name_tool, update_name_tool], 
                                        llm=self.llm,verbose=True,
                                        system_prompt=self.system_prompt)
        logger.info("Agent created")
        return agent
    
    def chat(self, query: str):
        """
        Processes a chat query using the initialized agent and returns the response.

        This method sends a user query to the agent, which processes it using the available tools 
        and language model, and returns the generated response. 

        Args:
            query (str): The query string to be processed by the agent.
        
        Returns:
            The agent's response to the provided query.
        """
        response = self.agent.chat(query)
        return response
