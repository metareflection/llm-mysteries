from anthropic import Anthropic
from typing import Callable
import os

MODEL = 'claude-3-5-sonnet-20241022'

def generate(prompt: str) -> str:
    """
    Generate text using Claude API with similar interface to Ollama.
    
    Args:
        prompt (str): The input prompt to send to Claude
        
    Returns:
        str: Generated text response from Claude
        
    Example:
        >>> generate_func = default_generate_func
        >>> response = generate_func("Tell me a story about...")
    """
    # Initialize client with API key from environment
    client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
    
    # Create message and get response
    response = client.messages.create(
        model=MODEL,
        max_tokens=1000,  # Adjust as needed
        temperature=0.6,  # Matching Ollama temperature
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    return response.content[0].text

if __name__ == '__main__':
    # Example usage
    prompt = "What is the capital of France?"
    response = generate(prompt)
    print(response)
