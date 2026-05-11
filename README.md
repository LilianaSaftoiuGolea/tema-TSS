# Laborator 10.05 (L5) – CI/CD pentru `linear_search`

[![CI](https://github.com/LilianaSaftoiuGolea/tema-TSS/actions/workflows/ci.yml/badge.svg)](https://github.com/LilianaSaftoiuGolea/tema-TSS/actions/workflows/ci.yml)

## Descriere scurtă

Repository-ul conține rezolvarea laboratoarelor L3 și L4 pentru funcția `linear_search(v, key)`, plus un pipeline GitHub Actions pentru laboratorul 10.05 (L5).

Funcția:
- primește o listă de exact 5 numere întregi și o cheie întreagă;
- returnează indicele primei apariții a lui `key`;
- returnează `-1` dacă elementul nu există;
- ridică `ValueError` dacă lungimea listei este diferită de 5.

## Structura proiectului

```text
repo/
├── README.md
├── RAPORT_L5.md
├── requirements.txt
├── cosmic-ray-ci.toml
├── src/
│   ├── linear_search.py
│   └── oracle.py
├── tests/
│   ├── test_black_box.py
│   ├── test_white_box.py
│   ├── test_mutation_helpers.py
│   └── test_random.py
└── .github/
    └── workflows/
        └── ci.yml
```

## Ce face pipeline-ul

La fiecare `push` sau `pull_request`, workflow-ul:

1. instalează dependențele proiectului;
2. rulează toate suitele de teste (`black box`, `white box`, `random`, `mutation helpers`);
3. rulează coverage;
4. eșuează dacă acoperirea pentru fișierul testat `src/linear_search.py` scade sub 100%;
5. generează raportul HTML de coverage și îl publică drept artefact;
6. rulează mutation testing într-un job separat;
7. salvează raportul de mutații ca artefact;
8. lasă job-ul de mutation testing ca opțional (`continue-on-error: true`).

## Instrucțiuni de rulare locală

### 1. Instalare dependențe

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Rulare toate testele

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Pe Windows PowerShell:

```powershell
$env:PYTHONPATH="src"
python -m unittest discover -s tests -v
```

### 3. Coverage

```bash
PYTHONPATH=src python3 -m coverage erase
PYTHONPATH=src python3 -m coverage run --branch -m unittest discover -s tests -v
PYTHONPATH=src python3 -m coverage report --include="src/linear_search.py" -m
PYTHONPATH=src python3 -m coverage html -d htmlcov
```

### 4. Mutation testing

```bash
export PYTHONPATH=src
export RANDOM_JOURNAL_FILE=random_mutation_journal.txt
cosmic-ray init cosmic-ray-ci.toml ci_session.sqlite
cosmic-ray --verbosity=INFO baseline cosmic-ray-ci.toml
cosmic-ray exec cosmic-ray-ci.toml ci_session.sqlite
cr-report ci_session.sqlite > mutation_report.txt
```

Pe Windows PowerShell:

```powershell
$env:PYTHONPATH="src"
$env:RANDOM_JOURNAL_FILE="random_mutation_journal.txt"
cosmic-ray init cosmic-ray-ci.toml ci_session.sqlite
cosmic-ray --verbosity=INFO baseline cosmic-ray-ci.toml
cosmic-ray exec cosmic-ray-ci.toml ci_session.sqlite
cr-report ci_session.sqlite > mutation_report.txt
```

## Semnificația badge-ului

Badge-ul din partea de sus arată starea curentă a workflow-ului GitHub Actions:
- verde = pipeline-ul a trecut;
- roșu = cel puțin un job a eșuat.

## Notificare la eșec

GitHub Actions poate trimite notificări web sau email pentru workflow-urile pe care le declanșezi. Pentru demonstrația cerută în laborator:

1. activezi notificările GitHub Actions în cont;
2. introduci intenționat un bug în `src/linear_search.py`;
3. faci `push`;
4. faci screenshot atât la run-ul eșuat din tab-ul **Actions**, cât și la notificarea primită.


