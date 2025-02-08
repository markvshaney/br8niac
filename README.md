# Local AI Search

A Streamlit-based web application that leverages local AI models for web searching. Built with Python best practices and modern development tools.

## 🌟 Features

- **Local AI Integration**: Uses Ollama for local AI model processing
- **Interactive UI**: Built with Streamlit for a responsive user experience
- **Search History**: Keeps track of recent searches
- **Real-time Status**: Monitors AI model availability
- **Modern Architecture**: Follows Python best practices and clean architecture

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed locally
- Make (optional, but recommended)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/local-ai-search.git
cd local-ai-search
```

2. Install the package and dependencies:
```bash
make install
```
Or without Make:
```bash
pip install -e ".[dev]"
pip install -r requirements/dev.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
```

4. Pull the required AI model:
```bash
ollama pull mistral
```

### Running the Application

```bash
make run
```
Or:
```bash
streamlit run src/local_ai_search/pages/home.py
```

## 🛠️ Development

### Project Structure

```
local_ai_search/
├── src/                  # Source code
│   └── local_ai_search/
│       ├── pages/       # Streamlit pages
│       ├── components/  # UI components
│       ├── services/    # Business logic
│       └── utils/       # Utilities
├── tests/               # Test suite
├── docs/               # Documentation
└── requirements/       # Dependencies
```

### Available Commands

- `make install`: Install package and dependencies
- `make format`: Format code using black and isort
- `make lint`: Run linting checks
- `make test`: Run test suite with coverage
- `make clean`: Clean temporary files
- `make run`: Start the application

### Running Tests

```bash
make test
```

This will run the test suite and generate a coverage report.

### Code Quality

Before committing, ensure:

1. All tests pass:
```bash
make test
```

2. Code is properly formatted:
```bash
make format
```

3. Linting checks pass:
```bash
make lint
```

## 📚 Documentation

- `/docs/index.md`: General documentation
- `/docs/api.md`: API documentation
- `/docs/development.md`: Development guide

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests and linting
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🧰 Built With

- [Streamlit](https://streamlit.io/) - Web interface
- [Ollama](https://ollama.ai/) - Local AI model
- [Pytest](https://pytest.org/) - Testing framework
- [Black](https://black.readthedocs.io/) - Code formatter
- [MyPy](http://mypy-lang.org/) - Static type checker

## ✨ Acknowledgments

- Streamlit team for the amazing framework
- Ollama team for making local AI models accessible
- Python community for the tools and libraries

## 📝 Note

This project is designed to work with local AI models for privacy and performance. Make sure you have enough system resources to run the AI model effectively.