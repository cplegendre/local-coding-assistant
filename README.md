*\# Local Coding Assistant Chatbot*

*This project is a simple local chatbot application designed to assist
with coding-related questions. The chatbot uses the Ollama API to
provide responses and is built with the Streamlit framework to create an
interactive web-based interface.*

*\## Features*

*- \*\*Interactive Chat\*\*: Users can ask questions related to coding,
debugging, and software architecture.*

*- \*\*AI-Powered Responses\*\*: The chatbot uses the
\`coder-r1:latest\` model from Ollama to generate responses based on the
user\'s input.*

*- \*\*Real-Time Interaction\*\*: The chatbot streams responses as it
processes the request.*

*\## Prerequisites*

*Before running this project, ensure you have the following installed:*

*- Python 3.6 or higher*

*- \`streamlit\` library*

*- \`ollama\` library (or a similar API to interact with an AI model)*

*You can install the required libraries using \`pip\`:*

*\`\`\`bash*

*pip install streamlit ollama*

## How to Run the Chatbot

### Step 1: Clone the Repository

Clone this repository to your local machine:

*git clone https://github.com/cplegendre/local-coding-assistant.git*

*cd local-coding-assistant*

### Step 2: Install Dependencies

Install the required dependencies using pip:

*pip install -r requirements.txt*

### Step 3: Run the Application

Start the Streamlit app by running the following command:

*streamlit run chatbot.py*

This will start the chatbot locally and open it in your default browser.
You can interact with the chatbot by typing questions or commands
related to programming, debugging, or architecture.

### Step 4: Chat with the Assistant

Once the Streamlit interface is open, type your question in the input
box and the assistant will respond with helpful coding advice,
architecture suggestions, or debugging tips.

## How it Works

-   **Streamlit Framework**: The app uses the Streamlit library to
    provide a web-based interface for users to chat with the AI
    assistant.
-   **Session State**: The conversation history is maintained using
    Streamlit\'s *st.session_state* to ensure context is kept during the
    chat session.
-   **Ollama API**: The chatbot integrates with the Ollama API (or
    another AI service) to provide responses based on the conversation.
    The assistant is defined as an expert programmer and software
    architect who offers clean, efficient, and well-commented code.

## Customization

You can customize the chatbot\'s behavior by modifying the system prompt
in the script. The system prompt defines the assistant\'s role and how
it should respond to queries.

*system_prompt = {*

* \"role\": \"system\",*

* \"content\": \"You are an expert programmer and software architect.
Always provide clean, efficient, well-commented code. \"*

* \"Explain your reasoning step by step. Use modern best practices. When
suggesting architecture or strategy, \"*

* \"be opinionated and practical. Support Python, JavaScript, Rust, Go,
Bash, and any other language requested.\"*

*}*

Feel free to adjust the prompt to suit your specific use case.

## Contributing

Contributions to this project are welcome! If you find any bugs or want
to add features, please fork the repository, create a branch, and submit
a pull request.

## License

This project is licensed under the MIT License - see the LICENSE

file for details.

## Acknowledgements

-   **Streamlit**: A powerful framework for building interactive web
    applications.
-   **Ollama API**: A cutting-edge AI model for generating code and
    offering programming assistance.
