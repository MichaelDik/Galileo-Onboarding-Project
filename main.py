from galileo import galileo_context
from galileo.openai import openai
from galileo.config import GalileoPythonConfig
from dotenv import load_dotenv
import sys
import json
from tools import TOOLS, TOOL_FUNCTIONS

# Load environment variables from the .env file
load_dotenv()

# Set the project and Log stream, these are created if they don't exist.
# You can also set these using the GALILEO_PROJECT and GALILEO_LOG_STREAM
# environment variables.
galileo_context.init(project="Financial Advisor Agent",
                     log_stream="dev_main_ls")

# Initialize the Galileo OpenAI client wrapper
client = openai.OpenAI()

# Define a system prompt with guidance
system_prompt = f"""

You are a helpful financial advisor agent to help the user make investment decisions. 

You have access to tools for checking bank balances, getting stock advice, and retrieving customer information.
Use these tools when appropriate to help the user.

"""

# Define 3 hardcoded user inputs
user_prompts = [
    "Is AAPL a good Buy?",
    "What's my bank balance?",
    "What's the customer info for CUST-001?"
]

# Process each user prompt
for i, user_prompt in enumerate(user_prompts, 1):
    print(f"\n{'='*60}")
    print(f"Query {i}: {user_prompt}")
    print(f"{'='*60}\n")
    
    # Initialize messages for this query
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    # Send a request to the LLM with tools
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto"
    )
    
    # Handle tool calls if any
    message = response.choices[0].message
    if message.tool_calls:
        messages.append(message)
        
        # Execute tool calls
        for tool_call in message.tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            
            # Call the appropriate function from the tool registry
            if function_name in TOOL_FUNCTIONS:
                function_response = TOOL_FUNCTIONS[function_name](**function_args)
            else:
                function_response = {"error": "Unknown function"}
            
            # Add tool response to messages
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(function_response)
            })
        
        # Get final response from LLM with tool results
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            tools=TOOLS,
            tool_choice="auto"
        )
    
    # Print the response
    print(response.choices[0].message.content.strip())
    print()

# # Show Galileo information after the response
# config = GalileoPythonConfig.get()
# logger = galileo_context.get_logger_instance()
# project_url = f"{config.console_url}project/{logger.project_id}"
# log_stream_url = f"{project_url}/log-streams/{logger.log_stream_id}"

# print()
# print("🚀 GALILEO LOG INFORMATION:")
# print(f"🔗 Project   : {project_url}")
# print(f"📝 Log Stream: {log_stream_url}")