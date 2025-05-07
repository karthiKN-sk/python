# Python Project Environment Setup Guide

This guide walks you through setting up a virtual environment and managing project dependencies using `venv` (built-in) or `virtualenv` (third-party) or [Conda](https://docs.conda.io) or Google Colab.

---

## 🧱 1. Create a Virtual Environment

### ✅ Using `venv` (built-in with Python 3.3+)

1. Navigate to your project directory:

            ```bash
            cd /path/to/your/project
            ```
2. Create a virtual environment:

            ```
            python -m venv venv
            ```
3. Activate the environment:
       Linux/macOS:  
       
            ```
            source venv/bin/activate
            ``` 
       Windows:

            ```
            venv\Scripts\activate
            ``` 

## 2.⚙️ Using virtualenv (third-party)

1. Install virtualenv (if not installed):

            ```
            pip install virtualenv 
            ```
2. Create a virtual environment:

            ```
            virtualenv venv
            ```

3. Activate the environment:
      Linux/macOS:

            ```
            source venv/bin/activate
            ```
      Windows:
      
            ```
            venv\Scripts\activate
            ```
        
## 3. Create a Conda Environment

1. You can create a new environment with a specific Python version:

            ```bash
            conda create -n myenv python=3.10
            ```
2. Activate the Environment:

            ```
            conda activate myenv
            ```
3. To deactivate it:

            ```
            conda deactivate
            ```
## Update python Version

            ```
            conda install python= #version
            ```


 
## Update python Version in Google Colab
## install python 3.9
            ```
            !sudo apt-get update -y
            !sudo apt-get install python3.9
            ```

## change alternatives
            ```
            !sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 
            !sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9
            ```

## check python version
            ```
            !python --version
            ```

## choices for the alternative python3

            ```
            !sudo update-alternatives --config python3
            ```
## Example
          There are 3 choices for the alternative python3 (providing /usr/bin/python3).
            Selection    Path                 Priority   Status
            ------------------------------------------------------------
            * 0            /usr/bin/python3.11   2         auto mode
            1            /usr/bin/python3.10   1         manual mode
            2            /usr/bin/python3.11   2         manual mode
            3            /usr/bin/python3.12   1         manual mode

            Press <enter> to keep the current choice[*], or type selection number: