<p align="center">
  <img src="./src/assets/logo.png" width="300" alt="Amar Logo" />
</p>

  <p align="center">Python-based GUI application designed to streamline the generation and management of contracts for Amar Infâncias, a photography company.</p>
    <p align="center">

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

</div>

<br>
<br>

<div align="center">

<img src="src/assets/project_example.png" width="350">

</div>

## 🎯 Goal
At <strong>Amar Infâncias</strong>, the demand for photography coverages is high, which means contracts need to be generated frequently. I saw this as a great opportunity to practice automation while developing a tool that truly enhances our daily workflow.

<hr>

## ⚙️ Technologies
The app was built with:

- <strong>Python
- Python-docx
- Tkinter/Customtkinter</strong>

<hr>

## 💾 How to install
in the terminal, run the following command: 
```bash
pip install -r requirements.txt
```
all contract-sensitive information is protected using .env variables. Make sure to fill in all the necessary information in a .env file, following the .env.example file.

<hr>

## 🔧 How it works?
All contract templates are organized in separate modules inside the models folder. This modular approach makes debugging easier and ensures that each template contains all the necessary information for its respective package.

Once the form is filled out, clicking "Generate Contract" opens a dialog window where the user selects the destination folder. The contract is then automatically generated and saved in the chosen location.