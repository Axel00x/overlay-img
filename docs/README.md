# Project README

## Overlay

PyQt5 Overlay GUI App (Settings dialog + Main window)

## Overview

This repository contains a PyQt5-based desktop application with an overlay and a modular settings dialog implemented as a `QDialog`.

The README explains how to install dependencies and run the app.

## Features

* Overlay
* PyQt5-based UI
* Modal settings dialog (`QDialog`) with example fields

## Requirements

* Python 3.8+ (or latest stable 3.x)
* PyQt5

Install with pip:

```bash
pip install PyQt5
```

(If you use a virtual environment, activate it before installing.)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Axel00x/overlay-img
    cd overlay-img
    ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    # on Windows
    venv\Scripts\activate
    # on Unix / macOS
    source venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    # or if you don't have a requirements.txt:
    pip install PyQt5
    ```

## Running the app

Run your main application script (example):

```bash
python main.py
```

## License

MIT license.
