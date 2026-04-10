# Healthcare Chatbot

A healthcare chatbot powered by Google's Gemini AI and the Agent Development Kit (ADK).

## Features

- AI-powered healthcare assistance using Gemini 2.5 Flash
- Local development ready
- Easy deployment to cloud platforms
- Session-based conversation management

## Prerequisites

- Python 3.8+
- Google API Key (get one at [Google AI Studio](https://aistudio.google.com/app/apikeys))
- Git (for deployment)

## Installation

### 1. Activate Virtual Environment

```powershell
.venv\Scripts\activate
```

### 2. Install Dependencies

```powershell
uv pip install google-adk flask python-dotenv
```

Or install from requirements.txt:

```powershell
uv pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root:

```
GOOGLE_GENAI_USE_VERTEXAI=0
GOOGLE_API_KEY=your_api_key_here
```

2. Replace `your_api_key_here` with your actual Google API key

## Running Locally

### Option 1: Direct Python

```powershell
python -c "from my_health_carechatbot.agent import root_agent; print(root_agent.generate('Hello, I need health advice'))"
```

### Option 2: Web Interface (Recommended)

Create a `main.py` file:

```python
from flask import Flask, request, jsonify
from my_health_carechatbot.agent import root_agent
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    try:
        response = root_agent.generate(user_message)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Then run:

```powershell
python main.py
```

Access at: `http://localhost:5000`

## Deployment

### Option 1: Railway.app (Easiest)

1. Push code to GitHub (ensure `.env` is in `.gitignore`)
2. Go to [railway.app](https://railway.app)
3. Connect your GitHub repository
4. Add environment variables in Railway dashboard:
   - `GOOGLE_GENAI_USE_VERTEXAI=0`
   - `GOOGLE_API_KEY=your_key`
5. Deploy

### Option 2: Google Cloud Run

```bash
gcloud run deploy healthcare-chatbot --source .
```

### Option 3: Render.com

1. Push to GitHub
2. Create new Web Service on [render.com](https://render.com)
3. Connect repository
4. Add environment variables
5. Deploy

## Project Structure

```
my_health_carechatbot/
├── agent.py          # Main agent configuration
├── __init__.py       # Package initialization
├── .env              # Environment variables (don't commit)
├── .adk/             # ADK session data
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Security

⚠️ **IMPORTANT**: Never commit `.env` to version control!

Use `.gitignore`:

```
.env
.venv/
__pycache__/
*.pyc
.adk/
```

## Troubleshooting

**Error: `uv: The term is not recognized`**
- Add to PATH: `$env:Path = "C:\Users\valla\.local\bin;$env:Path"`

**Error: `GOOGLE_API_KEY not found`**
- Check `.env` file exists with correct API key
- Ensure `.env` is in the project root

**Error: `google-adk not installed`**
- Run: `uv pip install google-adk`

## API Usage Example

```python
from my_health_carechatbot.agent import root_agent

# Get health advice
response = root_agent.generate("What should I do for a fever?")
print(response)
```

## License

MIT

## Support

For issues with Google ADK: [Visit ADK Documentation](https://ai.google.dev/docs/agents)

For Gemini API issues: [Visit Gemini Docs](https://ai.google.dev)
