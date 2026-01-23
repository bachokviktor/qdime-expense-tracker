## Introduction

QDime is an expense tracker system implemented using Django

## Setup

Clone the repository:

```bash
git clone https://github.com/bachokviktor/qdime-expense-tracker.git
cd qdime-expense-tracker
```

Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Create the `.env` file and set the environment variables used in `settings.py`

Apply the migrations:

```bash
python3 manage.py migrate
```

Run the development server:

```bash
python3 manage.py runserver
```
