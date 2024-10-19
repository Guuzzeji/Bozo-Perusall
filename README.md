# Bozo-Perusall

## About

Download PDF copy of Perusall assignments via the assignment url.

>[!IMPORTANT] Use at your own risk! (I am not responsible for any damage to your account or computer)

## How to Run

Follow project setup first then you can run this command and follow the instructions in terminal:

```bash
python main.py
```

## Project Setup

This guide will help you set up your environment to run the project.

## Prerequisites

Ensure that you have Python **3.12.6** installed on your system.

You can check your Python version by running:

```bash
python3 --version
```

## Setting Up the Virtual Environment

It's a good practice to use a virtual environment to manage dependencies and avoid conflicts with global packages.

**1. Create a virtual environment**:

```bash
python3 -m venv venv
```

**2. Activate the virtual environment**:

- On **Linux/MacOS**:
  
  ```bash
  source venv/bin/activate
  ```

- On **Windows**:
  
  ```bash
  .\venv\Scripts\activate
  ```

**3. Install the project dependencies**:

```bash
pip install -r requirements.txt
```

###  Deactivating the Virtual Environment

When you're done, deactivate the virtual environment:

```bash
deactivate
```

That's it! You're ready to start working on the project.

## TODO / Notes

- [ ] Fix sleep for specific elements and make them base on whether element shows up or not
- [ ] Hide password with input password python lib
- [ ] Fix error handling
