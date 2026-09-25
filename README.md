# AI Study Assistant

A Python-based study assistant that uses Google's Gemini API to help students learn from their own study notes.

## Features

* Ask questions about your study notes
* Generate summaries
* Uses your own notes as context for AI responses
* Organised into separate Python modules
* Simple command-line interface
* Supports multiple subjects through separate note files

## Project Structure

```text
AI-Study-Assistant/
│
├── main.py          # Main application
├── ai.py            # Gemini API functionality
├── menu.py          # Command-line menu
├── notes.txt        # Study notes
├── .gitignore       # Files ignored by Git
└── README.md        # Project documentation
```

## Requirements

* Python 3.10+
* Google Gemini API key
* `google-genai`

## Installation

Clone the repository:

```bash
git clone https://github.com/dorartmripa/AI-Study-Assistant.git
cd AI-Study-Assistant
```

Install the required package:

```bash
python -m pip install google-genai
```

## API Key

Create a Gemini API key through Google AI Studio.

Set your API key as an environment variable.

### Windows PowerShell

```powershell
$env:GEMINI_API_KEY="your-api-key"
```

## Running the Application

Run:

```bash
python main.py
```

The application will allow you to select your study material and interact with the AI assistant.

## Future Improvements

Planned features include:

* [ ] Quiz generation
* [ ] Flashcard generation
* [ ] Study history
* [ ] PDF note support
* [ ] Multiple subjects
* [ ] Improved error handling
* [ ] Note searching and retrieval
* [ ] RAG-based question answering
* [ ] Improved terminal interface

## Technologies

* **Python**
* **Google Gemini API**
* **Git & GitHub**

## License

This project is licensed under the MIT License.
