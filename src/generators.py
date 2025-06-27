from llama_index.llms.ollama import Ollama
from llama_index.llms.groq import Groq

import os

class Generators:
    def __init__(self, model="llama-3.3-70b-versatile"):
        # self.llm = Ollama(model=model, temperature=0)
        """
        Initializes the Generators class with a specified language model.

        Args:
            model (str): The name of the model to use. Defaults to "llama-3.3-70b-versatile".
        """
        self.llm = Groq(model=model, api_key=os.environ['GROQ_API_KEY'], temperature=0)

    def get_llm(self):
        """
        Returns the currently initialized language model (LLM) instance.

        :return: The language model instance used by the Generators class.
        """
        return self.llm