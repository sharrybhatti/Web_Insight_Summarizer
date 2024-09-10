# Web_Insight_Summarizer

**Web_Insight_Summarizer** is a Streamlit app that allows users to enter a topic, searches the web for relevant information, summarizes the content, and provides links to the sources. This app leverages a Large Language Model (LLM) to generate concise summaries from the gathered information.

## Features

- **Search**: Enter a topic to perform a web search.
- **Content Extraction**: Extracts text content from the top search results.
- **Summarization**: Uses an LLM to summarize the gathered information.
- **Source Links**: Displays links to the sources of the information.

## Installation

To run the app locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sharybhatti/Web_Insight_Summarizer.git

    Navigate to the Project Directory

    bash

cd InformationSummarizer

Create a Virtual Environment (optional but recommended)

bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies

bash

pip install -r requirements.txt

Run the Streamlit App

bash

    streamlit run app.py

Dependencies

The app requires the following Python packages:

    streamlit
    requests
    beautifulsoup4
    langchain_ollama

These dependencies are listed in the requirements.txt file.
Usage

    Open the Streamlit app in your web browser.
    Enter a topic in the text input field.
    Click the "Search and Summarize" button.
    The app will display the top search result links and generate a summary of the gathered information.

Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please follow these steps:

    Fork the Repository: Click the "Fork" button on GitHub to create a copy of the repository.
    Create a Branch: Create a new branch for your changes.

    bash

git checkout -b feature-branch

Make Your Changes: Implement your changes or improvements.
Commit Your Changes: Commit your changes with a descriptive message.

bash

git add .
git commit -m "Add feature or fix bug"

Push to Your Fork: Push your changes to your forked repository.

bash

    git push origin feature-branch

    Open a Pull Request: Go to the original repository and open a pull request with a description of your changes.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Contact

For any questions or feedback, please reach out to Shaharyarshabbir348@gmail.com.


Let me know if there are any other details you'd like to include or if you need further modifications!
