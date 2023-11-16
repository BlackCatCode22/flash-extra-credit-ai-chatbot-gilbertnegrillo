# Reference: GitHub Classroom: AI Chatbot with Flask and Plain Text Memo

# Notes:
# - Removed API key before publishing to GitHub classroom.
# - Received an OpenAIError saying that openai.Completion wasn't compatible with openai latest version.
# - I fixed it by installing openai version 0.28.0.

from flask import Flask, request, render_template
import openai
import constants

openai.api_key = constants.api_key

app = Flask(__name__)

conversation_history = {}


def count_tokens(text):
    num_words = len(text.split(" "))
    add_fifty_percent = len(text.split(" ")) / 2
    num_of_tokens = num_words + add_fifty_percent
    return num_of_tokens

# this is what happens when someone starts at the root of the website "/"


@app.route("/", methods=["GET", "POST"])
def start_here():
    if request.method == "POST":
        # There is a <textarea> on the index.html webpage named "question"
        #   what the user types in the <textarea> named "question" will be used as the prompt for text-davinci-003 .
        user_id = request.remote_addr
        text_question = request.form.get("question")

        chat_history = conversation_history.get(user_id, "")

        chat_history += f"\nHuman: {text_question}\nAI:"
        request_text = chat_history
        print(f"Chat history is: {request_text}")
        request_tokens = count_tokens(request_text)

        # Choose the model from OpenAI that you want to use.

        # Make a request to text-davinci-003.
        try:
            # Call the method named create from the Completion class of the OpenAI Python client library.
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=chat_history,
                max_tokens=1500,
                temperature=0.7,
                n=3,
                stop="\nHuman:"
            )

            response_text = response

            ai_response = response.choices[0].text.strip()
            chat_history += ai_response

            ai_response2 = response.choices[1].text.strip()
            ai_response3 = response.choices[2].text.strip()

            conversation_history[user_id] = chat_history

            response_tokens = count_tokens(response_text)
            total_tokens = request_tokens + response_tokens

            return render_template("index.html", textQuestion="", textAnswer=ai_response, textAnswer2=ai_response2,
                                   textAnswer3=ai_response3, tokenUsage=total_tokens, queryUsage=chat_history)

        except openai.OpenAIError as e:
            print(f"OpenAIError occurred: {e.__class__.__name__} - {e}")
            return render_template("index.html", textQuestion=text_question, textAnswer=f"OpenAIError occurred: "
                                                                                        f"{e.__class__.__name__} - {e}")

        except Exception as e:
            print(f"Unexpected error: {e.__class__.__name__} - {e}")
            return render_template("index.html", textQuestion=text_question, textAnswer=f"Unexpected error: "
                                                                                        f"{e.__class__.__name__} - {e}")

        print(f"Request Tokens: {request_tokens}, Response Tokens: {response_tokens}, Total Tokens: {total_tokens}")

    return render_template("index.html", textQuestion="", textAnswer="")


if __name__ == "__main__":
    app.run(debug=True)
