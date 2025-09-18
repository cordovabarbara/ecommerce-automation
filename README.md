# 🛒 QA Automation Project - Saucedemo

> End-to-end testing of an e-commerce workflow using **Python, Selenium & Pytest**.

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green) ![Pytest](https://img.shields.io/badge/Pytest-8.4.2-orange)

---

## 🚀 Project Overview

Automates the main workflow of the [Saucedemo](https://www.saucedemo.com) demo site:

1. **Login** with valid credentials  
2. **Add all products** to cart  
3. **Checkout** process  
4. **Assertions** for login and order confirmation  

Uses **Page Object Model (POM)** for clean and reusable code.

---
## 📁 Project Structure
```
saucedemo-automation/
├── pages/
│   ├── login.py
│   ├── shopping.py
│   └── checkout.py
├── tests/
│   └── test_checkout_flow.py
├── conftest.py
├── requirements.txt
└── README.md

# Clone repo
git clone https://github.com/your-username/your-repo.git
cd your-repo

# Optional: create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

# Install dependencies
pip install -r requirements.txt

# Run test
pytest tests/test_checkout_flow.py

<h2>Happy Testing! 🚀</h2> 
