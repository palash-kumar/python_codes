# Basic Calculator using Python

Folder structure:

```shell
calculator_py/
├── calc.py # backup of old main.py
├── functions
│   ├── arethmatic.py
│   └── __pycache__
│       └── arethmatic.cpython-313.pyc
├── main.py
├── __pycache__
│   └── main.cpython-313.pyc
├── readme.md
├── routers
│   ├── calculator.py
│   └── __pycache__
│       └── calculator.cpython-313.pyc
└── views
    └── calculator.html
```

Requirement:

```shell
pip install sympy fastapi uvicorn

```

Run:

```shell
uvicorn app.main:app --reload

# url: http://localhost:8001/
```
