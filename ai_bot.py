from dotenv import dotenv_values
import openai

# Load environment variables from .env file
env_vars = dotenv_values('.env')

# Initialize the OpenAI client
openai.api_key = env_vars['OPEN_AI_KEY']

# Initial system message defining the assistant's persona
system_message = {
    "role": "system",
    "content": "You are Tommy, a manager at the technology firm with many years of experience. You are a "
               "demanding but fair leader, with a blunt communication style and a dry sense of humor. Please "
               "respond as though you are the user's manager."
}

# Get initial user prompt
initial_prompt = input('Ask Tommy a question!: ')
initial_prompt += ' Please limit the response to a single paragraph.'

# Initial user message
user_message = {
    "role": "user",
    "content": initial_prompt
}

# List to keep track of the conversation
messages = [system_message, user_message]

while True:
    # Generate response from the assistant
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    content = response.choices[0].message.content

    # Print assistant's response
    print(f'{content}\n')

    # Append assistant's response to messages
    messages.append({"role": "assistant", "content": content})

    # Get user's reply
    reply_prompt = input('Respond to Tommy (or type "thanks" to exit):\n')

    if reply_prompt.lower() == 'thanks':
        print("See you")
        break

    # Append user's reply to messages
    messages.append({"role": "user", "content": reply_prompt})
