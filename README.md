[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![spaCy](https://img.shields.io/badge/NLP-spaCy-09A3D5)](https://spacy.io/)
[![Pandas](https://img.shields.io/badge/Data-Pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Remotive API](https://img.shields.io/badge/API-Remotive-2F80ED)](https://remotive.com/api-documentation)
[![Tests](https://img.shields.io/badge/Tests-unittest%20%7C%20coverage-25A162)](https://coverage.readthedocs.io/)

# Job Matcher

Job Matcher is open source software licensed under the [MIT License](https://opensource.org/licenses/MIT).

A Python-based **Job Matcher** application that helps users discover suitable remote jobs based on their skills and preferences.
The system fetches live job listings, applies an NLP-based matching pipeline, and presents results through an interactive **Streamlit** UI.

---

## Features

- Fetches live remote job listings via the **Remotive API**
- NLP-based skill matching using **spaCy**
- Interactive web UI built with **Streamlit**
- Stores matched jobs locally to avoid duplicates
- Built using **Test-Driven Development (TDD)** with high test coverage

---

## Tech Stack

- **Language:** Python
- **UI:** Streamlit
- **NLP:** spaCy (`en_core_web_md`)
- **Data Handling:** Pandas
- **API:** Remotive Jobs API
- **Testing:** unittest, coverage

---

## Project Structure

```
Job-Matcher/
├── app.py                 # Streamlit application entry point
├── requirements.txt       # Python dependencies
├── config/                # Configuration files and paths
├── data/                  # Stored user data and job listings (CSV)
├── pages/                 # Streamlit multi-page UI
├── src/                   # Core application logic
│   ├── api/               # API caller logic
│   ├── nlp/               # NLP processing and matching
│   ├── data_manager/      # Data storage and retrieval
├── tests/                 # Unit and integration tests
└── README.md
```

---

## Build & Run Instructions

### 1️. Clone the repository

```bash
git clone https://github.com/SGTK06/Job-Matcher.git
cd Job-Matcher
```

### 2️. Create and activate a virtual environment (Python 3.12 recommended)

**Windows (PowerShell):**

```powershell
py -3.12 -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️. Install dependencies

```bash
pip install -r requirements.txt
```

> ⏳ Note: Installation may take some time due to NLP and ML-related dependencies.

### 4️. Install spaCy language model

```bash
python -m spacy download en_core_web_md
```

### 5️. Run the application

```bash
streamlit run app.py
```

---

## Running Tests

(Optional but recommended)

```bash
python -m unittest discover tests
```

For coverage:

```bash
coverage run -m unittest discover tests
coverage report
```

---

## Testing & Quality

- **Statement Coverage:** ~89%
- **Branch Coverage:** ~87%
- Testing techniques used:
  - Boundary Value Analysis
  - Equivalence Partitioning
  - Pairwise Testing
  - Mocking external APIs and NLP components

---

## Demo

A demo video is available here:
🔗 https://drive.google.com/file/d/1LmWFddK6ieHM53z3sD_ZlK_UaiNp99L5/view

---
