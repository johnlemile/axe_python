# Acessibility Testing Framework

Quick framework with aXe and Python for local acessibility tests. Uses Pytest to generate .html reports

## aXe

[aXe](https?//deque.com/axe), or Accessibility Engine, is an open-source testing tool designed to identify and help resolve web accessibility issues. It is commonly used for auditing and ensuring that web applications comply with accessibility standards, such as the Web Content Accessibility Guidelines (WCAG). aXe is maintained by Deque Systems, a company that focuses on digital accessibility solutions.

## Testing Scenarios

From the 'tests/test_acessibility.py' file
- test_acessibility_violations_existence (check if there is violations)
- test_some_acessibility_violation (handle specific violation validation)
- test_acessibility_violations (check all acessibility violations)

## Dependencies

Install [Python](https://www.python.org/), [Pip](https://pypi.org/) and [pytest](https://docs.pytest.org/) then run


- Create Python environment and activate venv
```
python3 -m venv venv
source venv/bin/activate
```

- Install dependencies
```
pip3 install -r requirements.txt
```

- Run (reports folder should be generated on root)
```
python3 -v --html=reports/report.html
```

## Room for Improvement

- Add CI/CD
- Add BDD