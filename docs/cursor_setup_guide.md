# Cursor IDE Setup Guide

This guide explains how to set up and use the Local AI Search project in Cursor IDE.

## Initial Setup

1. Open the project in Cursor IDE:
```bash
cursor local-ai-search
```

2. Install the Python extension if not already installed.

3. Select Python Interpreter:
   - Press `Cmd/Ctrl + Shift + P`
   - Type "Python: Select Interpreter"
   - Choose your Python environment

## Using Cursor Tasks

Access tasks in Cursor:
1. Press `Cmd/Ctrl + Shift + P`
2. Type "Tasks: Run Task"
3. Select from available tasks

### Available Tasks

1. **Install Dependencies**
   - Sets up all required packages
   - Run this first when setting up the project

2. **Run Application**
   - Starts the Streamlit application
   - Opens in your default browser

3. **Run Tests**
   - Executes test suite
   - Shows coverage report

4. **Format Code**
   - Runs Black and isort
   - Maintains consistent code style

5. **Lint Code**
   - Checks code quality with flake8
   - Runs type checking with mypy

6. **Clean Project**
   - Removes cache and build files
   - Useful for clean builds

7. **Start Ollama**
   - Starts the Ollama server
   - Runs in background

8. **Pull Mistral Model**
   - Downloads the Mistral model
   - Required for AI functionality

9. **Setup Environment**
   - Creates .env file from template
   - Configure before running app

## Keyboard Shortcuts

- Run Task: `Cmd/Ctrl + Shift + P` → "Tasks: Run Task"
- Quick Open File: `Cmd/Ctrl + P`
- Open Terminal: ``Cmd/Ctrl + ` ``
- Toggle Sidebar: `Cmd/Ctrl + B`

## Development Workflow

1. Start by running these tasks in order:
   - "Install Dependencies"
   - "Setup Environment"
   - "Pull Mistral Model"
   - "Start Ollama"

2. During development:
   - Use "Format Code" before commits
   - Run "Lint Code" to check quality
   - Use "Run Tests" to verify changes

3. Running the application:
   - Execute "Run Application"
   - Make changes and see live updates

## Debugging

1. Set breakpoints by clicking left of line numbers

2. Start debugging:
   - Press `F5` or
   - Use Run and Debug panel (`Cmd/Ctrl + Shift + D`)

3. Debug controls:
   - Continue: `F5`
   - Step Over: `F10`
   - Step Into: `F11`
   - Step Out: `Shift + F11`

## Recommended Extensions

- Python
- Python Test Explorer
- Python Docstring Generator
- TOML Language Support
- YAML Support

## Project Organization

The project follows this structure in Cursor:

```
local_ai_search/
├── .cursor/          # Cursor IDE configuration
├── src/              # Source code
├── tests/            # Test files
├── docs/             # Documentation
└── requirements/     # Dependencies
```

## Best Practices

1. Always run tests before committing
2. Format code regularly
3. Use the integrated terminal for commands
4. Commit often with clear messages
5. Keep dependencies updated


## Cursor Rules

The project includes predefined Cursor rules for consistent code quality:

### Python Rules

- **Line Length**: Maximum 88 characters (Black standard)
- **Docstring Style**: Google format
- **Import Order**: stdlib → third-party → first-party → local
- **Auto-formatting**: Enabled on save
- **Type Checking**: Strict mode enabled
- **Testing**: Auto-run tests on save
- **Code Style**: 
  - PascalCase for classes
  - snake_case for functions and variables
  - UPPER_CASE for constants

### Git Rules

- **Commit Messages**: Conventional commits
  - feat: New features
  - fix: Bug fixes
  - docs: Documentation
  - style: Code style changes
  - refactor: Code refactoring
  - test: Adding tests
  - chore: Maintenance tasks

- **Branch Naming**:
  - feature/description
  - bugfix/description
  - hotfix/description
  - release/version

### Editor Rules

- **Formatting**:
  - 4 spaces for indentation
  - Trim trailing whitespace
  - Add final newline
  - 88-character ruler
  - Auto-closing pairs

### To Apply Rules

1. Create `.cursor` directory:
```bash
mkdir -p .cursor
```

2. Copy rules file:
```bash
cp rules.json .cursor/
```

3. Restart Cursor IDE

### Overriding Rules

To override specific rules for your local setup:

1. Create `.cursor/rules.local.json`
2. Add your custom rules
3. Restart Cursor

Example override:
```json
{
    "version": "1.0",
    "rules": {
        "python": {
            "max_line_length": 100
        }
    }
}
```