
# Wikipedia URL Chat App 

A chatbot application that uses OpenAI's language model  for Wikipedia URL Question Answering.

## Technologies Used
  - Streamlit: The user interface is built with Streamlit, making it easy to create web apps with Python.

  - LangChain: LangChain is used for text processing, text splitting, and handling embeddings.

  - OpenAI LLM: The application integrates with OpenAI's powerful LLM model for natural language processing and understanding.


## Features
-Wikipedia Link Upload: Allow users to upload Wikipedia link to specific articles of interest.
 
-Information Retrieval: Retrieve and parse the content of the Wikipedia article corresponding to the uploaded link.
 
-Question-Answering: Enable users to ask questions related to the information in the Wikipedia article and receive accurate answers from the chatbot.
 
-User Interaction: Provide a user-friendly interface for seamless interaction with the chatbot.
 


## Getting Started
Follow these steps to set up and run the LLM Chat App on your own system:

1. Clone this repository using the following command:
   ```sh
   git clone https://github.com/Mayuresh2703/Wikipedia-URL-Char-App

2. Install the required Python packages using:
    ```sh
    pip install -r requirements.txt

3. Set up your OpenAI API key:

 - Visit the OpenAI Platform to create an account or log in if you already have one.
 - Follow the instructions on the OpenAI platform to obtain your API key. You can find detailed documentation on how to create an API key in the OpenAI API Documentation.
 - Once you have your API key, set it as an environment variable named OPENAI_API_KEY in your environment or in the application as specified in the project's setup instructions.

4. Run the app using:
    ```sh
    streamlit run wiki.py


## Usage
 - Upload a Wikipedia URL.

 - Ask questions related to the information in Wikipedia URL.

 - The chatbot will provide answers based on the URL's content.

## OpenAI API Key

This project relies on the OpenAI API for natural language processing and understanding. To use this application, you need to obtain an OpenAI API key.

1. Visit the [OpenAI Platform](https://platform.openai.com/) to create an account or log in if you already have one.

2. Follow the instructions on the OpenAI platform to obtain your API key. You can find detailed documentation on how to create an API key in the [OpenAI API Documentation](https://platform.openai.com/docs/guides/authentication).

3. Once you have your API key, set it as an environment variable named `OPENAI_API_KEY` in your environment or in the application as specified in the project's [setup instructions](#getting-started).

Please keep your API key confidential and do not share it publicly. If you plan to collaborate on this project with others, consider using environment variables or other secure methods for key management.

## Deployment 

1. This application is hosted on Streamlit Cloud.Link -> (https://wikipedia-url-chat-app-bbw3h2ktklx4jbmfkzvbco.streamlit.app/)
   

## Acknowledgements

 - (https://betterprogramming.pub/create-a-wikipedia-question-answering-app-with-python-2401e1789d6c)https://betterprogramming.pub/create-a-wikipedia-question-answering-app-with-python-2401e1789d6c

