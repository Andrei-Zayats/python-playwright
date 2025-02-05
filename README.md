# python-playwright

## UI tests
Repository on [github](https://github.com/Andrei-Zayats/python-playwright)

### Technologies
- Python
- Playwright
- Allure Report

### Commands
Install Playwright for Python:
```
pip install pytest-playwright
```

Install Allure Report for Python:
```
pip install allure-pytest
```

Run tests in headed mode:
```
pytest --headed
```

Run tests in headed mode with two browsers and allure:
```
pytest -v -s --headed --alluredir allure_results --browser webkit --browser firefox
```


Make report:
```
allure serve allure_results
```