# User Data Management Application

A Python-based desktop application developed using Tkinter to collect, manage, store and export user information in multiple file formats.

## Overview

The User Data Management Application provides a simple graphical interface for collecting user details and storing them in an Excel spreadsheet. It also allows users to export submitted information into different formats, making data management and sharing easier.

The application follows a modular structure by separating the graphical user interface, backend data operations and application execution logic.

## Key Features

- **User Information Collection:** Collects Name, Email ID, Phone Number and Branch details.
- **Input Validation:** Checks that all required fields are completed.
- **Excel Integration:** Automatically creates an Excel workbook and stores submitted records.
- **Multiple Export Formats:** Export user information in:
  - JSON
  - TXT
  - XML
  - XLSX
- **Branch Selection:** Supports selecting branch options through checkboxes.
- **Clear Form:** Clears input fields and resets selections.
- **Graphical User Interface:** Provides an interactive desktop interface using Tkinter.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Tkinter | Desktop graphical user interface |
| OpenPyXL | Excel file creation and management |
| JSON | Structured data export |
| XML | XML data generation |
| File Handling | Reading and writing exported files |

## Application Architecture

The application is divided into three main modules:

1. **main.py** – Controls application execution, input validation, form submission, clearing fields and export actions.
2. **frontend.py** – Creates the Tkinter graphical interface, input fields, checkboxes and buttons.
3. **backend.py** – Handles Excel creation, data storage and exporting information into JSON, TXT, XML and XLSX formats.

## Project Structure

```text
User-Data-Management-Application/
│
├── main.py
├── frontend.py
├── backend.py
└── README.md
```

## Installation and Setup

### Prerequisites
- Python 3.10 or above
- pip package manager

### 1. Clone the Repository

```bash
git clone https://github.com/venky140/User-Data-Management-Application.git
```

### 2. Navigate to the Project Directory

```bash
cd User-Data-Management-Application
```

### 3. Install Dependencies

```bash
python -m pip install openpyxl
```

Tkinter is included with most standard Python installations.

### 4. Configure the Excel File Location

Open `backend.py` and configure the `excel_file` variable to point to a valid Excel file location on your computer.

### 5. Run the Application

```bash
python main.py
```

## How It Works

1. Launch the desktop application.
2. Enter the user's name, email address and phone number.
3. Select the relevant branch.
4. Click Submit to save the information.
5. Select an export format.
6. Download the submitted information in the selected format.
7. Use Clear to reset the form.

## Skills Demonstrated

- Python programming
- GUI development using Tkinter
- Modular programming
- File handling and data serialization
- Excel automation using OpenPyXL
- Input validation and exception handling
- Working with JSON and XML formats
