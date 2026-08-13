# project-zbot

A small command-line chatbot. It sends a single prompt to a model on
[OpenRouter](https://openrouter.ai) through the OpenAI SDK and prints the reply.

## Requirements

- Python 3.13+
- [uv](https://docs.astral.sh/uv/)
- An OpenRouter API key

## Setup

```bash
uv sync
cp .env.example .env
```

Then open `.env` and set your key:

```
OPENROUTER_API_KEY=sk-or-...
```

## Usage

```bash
uv run main.py "What is the capital of France?"
```

Add `--verbose` to also print the prompt and token counts:

```bash
uv run main.py "What is the capital of France?" --verbose
```

```
User prompt:
What is the capital of France?

Prompt tokens: 15
Response tokens: 8

Response:
The capital of France is Paris.
```

## Configuration

The model is set in `main.py` and defaults to `openai/gpt-oss-20b:free`. Any
model ID from OpenRouter's catalog works — swap the `model` argument in
`generate_content` to change it.
