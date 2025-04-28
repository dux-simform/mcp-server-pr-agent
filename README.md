# MCP Server PR Agent

This project provides a server for managing and analyzing pull requests using the MCP framework.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd mcp-server-pr-agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file:
   Copy the `.env.sample` file and fill in the required values:
   ```bash
   cp .env.sample .env
   ```

4. Run the server:
   ```bash
   python server.py
   ```

## Environment Variables

The `.env` file should contain the following variables:

- `GIT_PROVIDER`: The Git provider (e.g., `github`).
- `OPENAI_API_KEY`: Your OpenAI API key.
- `OPENAI_API_TYPE`: The type of OpenAI API (e.g., `azure`).
- `OPENAI_API_VERSION`: The version of the OpenAI API.
- `OPENAI_API_BASE`: The base URL for the OpenAI API.
- `OPENAI_API_DEPLOYMENT`: The deployment ID for the OpenAI API.
- `GITHUB_USER_TOKEN`: Your GitHub user token.

Refer to `.env.sample` for an example configuration.

