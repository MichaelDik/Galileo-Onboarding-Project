import sys
import os
sys.stdout.reconfigure(encoding="utf-8")
from openai import OpenAI

# Initialize client - API key should be in OPENAI_API_KEY environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("Error: OPENAI_API_KEY environment variable is not set.")
    print("Please set it with: export OPENAI_API_KEY='your-api-key'")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def run():
    response = client.responses.create(
        model="gpt-4o-mini",
        input="How are you today"
    )
    
    print(response.output_text)

if __name__ == "__main__":
    run()



