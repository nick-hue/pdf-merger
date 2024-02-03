# PDF Merger

## Description
This is an application that you can merge pdf files with.

## Installation

### Step 1: Clone the Repository
### Clone the repository to your local machine:  
    git clone https://your-repository-url
    cd your-repository-directory


### Step 2: Set up a Virtual Environment (Optional but recommended)
### It's a good practice to use a virtual environment to avoid conflicts with other packages:   
    python -m venv venv
    source venv/bin/activate # On Windows use venv\Scripts\activate


### Step 3: Install Required Packages
### Install all the required packages using the requirements.txt file:
    pip install -r requirements.txt

The `requirements.txt` file includes the following packages:
- `customtkinter`: A custom version of the Tkinter library for building GUIs.
- `Pillow`: A library for opening, manipulating, and saving many different image file formats.
- `pypdf`: A library for PDF file manipulation.

Ensure these packages are installed to run the application correctly.

## Running the Application

### To run the application, navigate to the directory containing `app.py` and run:
    python app.py


## Structure of the Application
Explain the structure of your application. For instance:
- `app.py`: The main entry point of the application.
- `controller.py`: Contains the logic for handling user interactions.