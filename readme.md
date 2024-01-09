# Accessibility Testing Framework

Quick framework with aXe and Python for local accessibility tests. Uses Pytest to run and generate .html reports

## The Weapon

[aXe](https://deque.com/axe), or Accessibility Engine, is an open-source testing tool designed to identify and help resolve web accessibility issues. It is commonly used for auditing and ensuring that web applications comply with accessibility standards, such as the Web Content Accessibility Guidelines (WCAG). aXe is maintained by Deque Systems, a company that focuses on digital accessibility solutions.

## Trowing Axes

From the 'tests/test_acessibility.py' file, we have the below scenarios
- test_accessibility_violations_positive (aXe checks if there are NOTICED violations, fail test if there are NO NOTICED violations)
- test_accessibility_violations_negative (aXe checks if there are NO NOTICED violations, fail test if there are NOTICED violations)
- test_some_accessibility_violation (handle specific violation validation, fail test if accepted violations are NOTICED)
- test_accessibility_violations (aXe checks all acessibility violations, fail test if there ARE violations)

## Go Berserk

Install [Python](https://www.python.org/), [Pip](https://pypi.org/) and [pytest](https://docs.pytest.org/) then run


- Create Python environment and activate venv:
```
python3 -m venv venv
source venv/bin/activate
```

- Install dependencies:
```
pip3 install -r requirements.txt
```

- Run (report folder should be generated on root):
```
pytest -v --html=report/test_acessibility_report.html
```

## Longhouse for Improvement

- Add CI/CD
- Add BDD