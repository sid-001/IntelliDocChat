# IntelliDocChat - AI Powered Document Chat Application

IntelliDocChat is an innovative AI-powered document chat application that leverages the power of language processing and machine learning to provide users with an intuitive way to interact with their documents. By combining the capabilities of Langchain, ChromaDB, Sentence Transformers, and Streamlit, IntelliDocChat offers a seamless experience for engaging in natural language conversations with your documents and gaining valuable insights from them.

![Size](https://img.shields.io/badge/Size-5.07GB-blue) ![Star](https://img.shields.io/github/stars/sid-001/IntelliDocChat?style=social&label=Star%20on%20Github)

## Features

- **Knowledge Base Selection:** Choose a knowledge base from the left panel, allowing you to focus on specific document collections.

- **Document Upload:** Upload a PDF file containing your document data, enabling the system to process and analyze the content.

- **Conversational Interface:** Engage in natural language conversations with your documents using the chat interface. Ask questions, request information, and explore your documents dynamically.

- **Insights and Answers:** Gain insights and answers from your documents through the chat interface. IntelliDocChat employs advanced language understanding to provide relevant and accurate responses.

- **Embedding Options:** IntelliDocChat is built using BGE BASE-EN Embeddings by default, but it also supports other embeddings through Sentence Transformers, giving you the flexibility to experiment with different language representations.

## How to Use

1. **Choose a Knowledge Base:** On the left panel of the application interface, select a knowledge base that corresponds to the collection of documents you want to interact with.

2. **Upload a PDF Document:** Use the document upload feature to provide the system with the PDF document you want to explore. This document will be processed and made available for chat interactions.

3. **Start Chatting:** Engage in a natural language conversation with your uploaded document. Type your questions, prompts, or requests in the chat interface, and IntelliDocChat will provide responses based on the content of the document.

4. **Explore and Gain Insights:** Through the chat interface, you can dynamically explore the content of your document. Ask for specific information, summaries, or any other insights you're seeking.

5. **Switch Knowledge Bases (Optional):** If you have multiple document collections, you can switch between different knowledge bases to interact with various documents.

## Supported Embeddings

IntelliDocChat is initially configured to use BGE BASE-EN Embeddings, which are integrated with Sentence Transformers. However, you have the option to experiment with other embeddings by integrating them with Sentence Transformers.

## Getting Started

To get started with IntelliDocChat, simply clone or download the repository from the [GitHub repository link](https://github.com/sid-001/IntelliDocChat). Make sure to follow the installation steps outlined in the repository to set up the required dependencies and environment.

Please note that the installation steps are not included in this README file. Refer to the repository's documentation for detailed installation instructions.

## Feedback and Contributions

We welcome feedback and contributions from the community to improve IntelliDocChat. If you encounter any issues, have suggestions for enhancements, or would like to contribute to the project, please feel free to open issues and pull requests on the GitHub repository.

Let's revolutionize the way we interact with documents using the power of AI and natural language processing!

### Give it a Quick Try with RunCode.io

[![RunCode](https://runcode-app-public.s3.amazonaws.com/images/dark_btn.png)](https://runcode.io)

### How to install IntelliDocChat Locally?
Directly using IntelliDocChat on Windows is not recommended; however, it will run smoothly when using WSL2 on Windows. Here are the installation steps for IntelliDocChat, assuming you are using a Linux/Debian system. These steps will help you set up IntelliDocChat, making sure to use Python version 3.10 or lower, as Numpy does not support Python 3.11:

1. Clone the IntelliDocChat repository from GitHub:
    ```
    git clone https://github.com/sid-001/IntelliDocChat.git
    ```

2. Navigate into the cloned repository directory:
    ```
    cd IntelliDocChat
    ```

3. Create the required directories:
    ```
    make required dirs
    ```

4. Make two directories named `tmp` and `knowledge_base`.

5. Create a `.env` file with your OpenAI API key:
    ```
    echo 'OPENAI_API_KEY="YOUR_API_KEY"' > .env
    ```
   Replace `YOUR_API_KEY` with your actual OpenAI API key.

6. Set up a virtual environment named 'env':
    ```
    virtualenv env
    ```

7. Activate the virtual environment:
    ```
    source env/bin/activate
    ```

8. Install the required Python packages from the `requirements.txt` file:
    ```
    pip install -r requirements.txt
    ```

9. Run the IntelliDocChat using Streamlit:
    ```
    streamlit run main.py
    ```

Remember to replace `YOUR_API_KEY` with your actual OpenAI API key in step 5. This set of instructions should help you install IntelliDocChat on your Linux/Debian system using Python version 3.10 or lower.