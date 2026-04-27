# task-manager-python

A simple Python task manager example.

## Overview

This project demonstrates a basic task manager structure in Python. It defines a `Task` class for individual tasks and a `TaskManager` class for storing and listing tasks.

The current example creates tasks directly in `main.py` and prints them to the terminal.

## Project Structure

```text
app/
  main.py
  manager.py
  task.py

data/
  task.json
```

## Requirements

- Python 3

## Usage

From the `app` directory, run:

```bash
python main.py
```

The script creates sample tasks, adds them to a task manager, and prints them in the terminal.

## Files

- `main.py` - Runs the example task manager workflow.
- `task.py` - Defines the `Task` class.
- `manager.py` - Defines the `TaskManager` class.
- `data/task.json` - Empty placeholder file for task data.

## Notes

This project currently uses hardcoded sample tasks and does not yet read from or write to `data/task.json`.
