# LinguaLab 📜

Welcome to LinguaLab: a solo project to build a Latin-to-English translator — part programming, part language learning.

## Features
- Dictionary-based translation
- Latin noun declension (1st declension so far)
- Modular Python code structure

## Project Structure
<pre><code> ## Project Structure translator-project/ ├── data/ # Latin dictionary (JSON format) │ └── latin_dict.json ├── grammar/ # Grammar rules (declension, etc.) │ ├── __init__.py │ └── declension.py ├── translator/ # Main runner script │ ├── __init__.py │ └── main.py ├── .gitignore ├── README.md └── venv/ # Virtual environment (excluded from Git) </code></pre>


## How to Use

1. **Clone the repo**
2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    ```
3. **Run the translator** from the project root:
    ```bash
    python -m translator.main
    ```

## Goals
- [x] Build a declension engine for 1st declension nouns
- [ ] Add verb conjugation
- [ ] Handle more Latin cases (genitive, dative, etc.)
- [ ] Translate full sentences using grammatical structure
- [ ] Build a web interface (Streamlit or Flask)
- [ ] Turn it into a learning tool (quizzes, breakdowns, etc.)

## License
MIT — free to use, learn from, and build on.