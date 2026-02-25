# Calculator Service

A production-style Python calculator module with CI/CD support.

## Features

- Modular architecture
- Logging
- Unit testing with pytest
- Linting with flake8
- Jenkins CI pipeline

## Run Locally

```bash
python -m venv venv
# Windows (PowerShell)
venv\Scripts\Activate.ps1

# macOS/Linux
# source venv/bin/activate

pip install -r requirements.txt
python -m pytest -v
```

## Run Calculator

```bash
python -c "from app.calculator import Calculator; calc = Calculator(); print(calc.add(10, 20)); print(calc.divide(10, 2))"
```

## CLI Usage

```bash
python -m app add 10 20
python -m app subtract 20 10
python -m app multiply 5 4
python -m app divide 10 2
```
