[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/dq-QnIdS)
# tPythonAIchatBot01
tPythonAIchatBot01

## AI Chatbot Server
This repository contains the implementation of a simple web-based AI chatbot using the Flask framework and OpenAI's GPT-3 (Davinci) model.

### How it Works
The Python program uses Flask, a micro web framework, to create a local server. It is designed to interact with a webpage, rendering an index.html file that serves as the chatbot's interface.

### Server Behavior
When the server starts, it routes requests to the root ("/") through the start_here function. The function handles two types of HTTP methods:

GET: Simply renders index.html with empty fields for the question and answer.
POST: Activated when a user submits a question through the form on index.html. The user's input is captured from a textarea named "question" and sent to OpenAI's GPT-3 model, specified as "text-davinci-003", to generate a response. The generated response is then rendered back on index.html in the answer textarea.
Error Handling
If there is an issue with the OpenAI API request, the server prints an error message with a debugging clue to the console.

### Webpage Interaction
The index.html file contains:

A form for users to submit their questions to the chatbot.
Two textarea elements for the question input and the AI-generated answer.
Styling to make the chatbot visually appealing, including a background image and styled submit button.
Local Server Setup
To run the server, you need to have Flask installed in your Python environment. You can install Flask by running the command pip install Flask from the Python console window within the PyCharm IDE.

The server script is found at the bottom of the Python file, defined by the block:

### python code

if __name__ == "__main__":
    app.run(debug=True)
This block is the entry point of the Flask application. When you run the Python script, this block invokes the app.run function, which starts a local development server for the chatbot application. The debug=True parameter allows for automatic reloading of the server on code changes and provides debug information in case of exceptions.

### Environment Setup
Folder Structure:

/templates: Contains HTML files that the Flask app will render. In this application, it holds the index.html which is the main interface for the chatbot.
/static: This is where all the static content such as images, JavaScript, and CSS files are stored. The Flask app serves these files unmodified.
Background Image:

The /static folder includes a beautiful background image for the webpage named twoRobotsReading.png, which was generated by DALL-E, an AI system created by OpenAI that can create realistic images and art from a description in natural language.

### Security Note
The provided API key is hardcoded, which is not a secure practice for production environments. It's recommended to use environment variables or a configuration file to handle API keys.

### Launching the Chatbot
Execute the Python script to launch the server, and navigate to localhost with the specified port in your web browser to interact with the AI chatbot.

Remember to remove or secure the hardcoded API key before making your code public on GitHub.

# Some ways to overcome the stateless nature of the API interactions:

When you're directly using the OpenAI API to communicate with a language model, the stateless nature of the API means that each query is independent and the model does not inherently recall previous interactions. However, there are a few strategies you can use to create a more conversational and context-aware interaction:

Session-Based Approach: OpenAI provides a way to maintain context through sessions. You can initiate a session and the API will keep track of the conversation history for the duration of that session.

Injecting Context: You can manually maintain the context by including previous questions and answers in the prompt for each new query. This is similar to what's done with chatbots where the context is prepended to the prompt to maintain continuity.

Using the Chat Interface: OpenAI also offers a specialized chat interface for conversational AI which is designed to maintain context across a series of messages.

For the standard Completion.create endpoint, if you want the model to recall previous queries during a single interaction, you would need to manage the conversation history yourself and include it with each request to the API.

For example, if you want to continue a conversation, you could do something like this:

## Python Code:
Copy code
conversation_history = "User: How's the weather today?\nAI: It's quite sunny with a mild breeze."

### Later on, you want to continue the conversation
new_user_input = "What about tomorrow?"

### Append the new input to the conversation history
conversation_history += f"\nUser: {new_user_input}\nAI:"

### Now use this updated history as the prompt
response = openai.Completion.create(
    engine=model_name,
    prompt=conversation_history,
    max_tokens=150,
    temperature=0.7
)

### Extract the model's response and update the conversation history
ai_response = response.choices[0].text.strip()
conversation_history += ai_response

### conversation_history now has the full conversation that you can use for subsequent API calls
Keep in mind that there is a limit to the number of tokens that the model can process in a single prompt, so for very long conversations, you might need to truncate older parts of the conversation or summarize them.








