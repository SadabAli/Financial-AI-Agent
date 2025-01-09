# Finance Agentic AI

## Project Description
This project implements a **Finance Agentic AI** that helps users with financial analysis, stock predictions, and market insights. The AI is built using **Gemini** and various financial tools like **YFinance** for real-time stock information. The system is capable of providing stock prices, company fundamentals, news, and recommendations to users based on current market data.

## Features
- Real-time stock data
- Stock price predictions
- Financial analysis and recommendations
- Interactive web interface
- Use of **DuckDuckGo** for web-based search queries related to finance
- Ability to handle multiple tasks and provide responses through an agent-based model

## Installation and Setup

### Prerequisites
Ensure you have Python 3.7+ installed on your system.

### Steps to Set Up

1. **Clone the repository**:
    ```bash
    git clone https://github.com/SadabAli/Financial-AI-Agent.git
    cd finance-agentic-ai
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv ~/.venvs/aienv
    source ~/.venvs/aienv/bin/activate  # On Linux/MacOS
    ```

3. **Install required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Export your API keys**:
    Before running the project, set up your API keys for services like Groq, Gemini and any other necessary APIs.
    ```bash
    export OPENAI_API_KEY=your_openai_api_key
    export EXA_API_KEY=your_exa_api_key
    ```

5. **Run the application**:
    ```bash
    python playground.py
    ```

## Usage
Once the application is running, you can interact with the finance AI agent through the web interface. Enter your queries regarding stock prices, financial news, and analysis, and the AI will provide the necessary information.

### Example Queries
- "What is the stock price of Tesla?"
- "Show me the financial report for Apple."
- "Give me the latest stock market news."
- 
![Screenshot 2025-01-09 124818](https://github.com/user-attachments/assets/4e78243d-db18-4277-8aa3-23c6466ca8c5)


## Contributing
If you wish to contribute to this project, feel free to fork the repository, make your changes, and create a pull request. Please ensure that your code adheres to the project’s coding standards.


