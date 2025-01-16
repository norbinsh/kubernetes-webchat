# AI-Powered Web Interaction Demo

Showcases the integration of LLMs with the browser_use library to automate web interactions. The project includes two Python scripts that simulate a teacher and a student engaging in a web-based chat environment.

## Getting Started

### Prerequisites

- **Python 3.8 or higher**: Ensure Python is installed on your system. You can download it from the [official website](https://www.python.org/downloads/).
- **OpenAI API Key**: Obtain your API key from [OpenAI](https://platform.openai.com/account/api-keys).

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/norbinsh/kubernetes-webchat
   cd kubernetes-webchat
   ```

2. **Create and activate a virtual environment**:

   - For **macOS and Linux**:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   - Create a `.env` file in the root directory:

     ```bash
     touch .env
     ```

   - Add your OpenAI API key to the `.env` file:

     ```env
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Running the Scripts

### Teacher Script

To run the teacher simulation:

```bash
python teacher.py
```

### Student Script

To run the student simulation:

```bash
python student.py
```

## Notes

- Ensure your OpenAI API key is correctly set in the `.env` file.
- The scripts are designed for educational purposes to demonstrate AI-driven web interactions.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
