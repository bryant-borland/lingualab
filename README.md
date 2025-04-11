# LinguaLab 📜

Welcome to LinguaLab: a solo project to build a Latin-to-English translator — part programming, part language learning.

This project is inspired by the vocabulary and structure introduced in *Familia Romana* by Hans Ørberg. 
This tool is not affiliated with or a reproduction of the book, but uses its content as a learning reference.

## Features
- Dictionary-based translation
- Latin noun declension (1st declension so far)
- Modular Python code structure

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
- [x] Basic Quiz
- [ ] Build a declension 
- [ ] Add verb conjugation
- [ ] Handle more Latin cases (genitive, dative, etc.)
- [ ] Translate full sentences using grammatical structure
- [ ] Build a web interface (Streamlit or Flask)
- [ ] Turn it into a learning tool (quizzes, breakdowns, etc.)

## License
MIT — free to use, learn from, and build on.