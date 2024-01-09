#tests/test_acessibility.py

# adding stuff to venv $PYTHONPATH
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import dependencies
import pytest
import json
from selenium import webdriver
from pages.sample_page import SamplePage
from utils.axe_utils import execute_acessibility_validation

# testing the google.com page
class TestAcessibility:
    @pytest.fixture
    def setup_teardown(self):
        self.driver = webdriver.Chrome()
        self.base_url = json.load(open("config.json"))["url"]
        self.page = SamplePage(self.driver, self.base_url)
        yield
        self.driver.quit()


    def test_acessibility_violations_existence(self, setup_teardown):
        self.page.open()
        result = execute_acessibility_validation(self.driver)
        # Check for violations
        assert result["violations"], "No accessibility violations found."

    def test_some_acessibility_violation(self, setup_teardown):
        self.page.open()
        result = execute_acessibility_validation(self.driver)
        accepted_violations = [
            'Ensures role attribute has an appropriate value for the element',
            'Ensures buttons have discernible text',
            'Ensures the contrast between foreground and background colors meets WCAG 2 AA contrast ratio thresholds',
            'Ensures the page has only one main landmark and each iframe in the page has at most one main landmark',
            'Ensures every id attribute value is unique',
            # Accept specific violations
        ]
        # Allow the accepted violation(s)
        violations = [violation['description'] for violation in result["violations"]]
        unexpected_violations = set(violations) - set(accepted_violations)
        assert not unexpected_violations, f"Unexpected violations found: {unexpected_violations}"

    def test_acessibility_violations(self, setup_teardown):
        self.page.open()
        result = execute_acessibility_validation(self.driver)
        # Checks for all accessibility violations
        assert result["violations"] == [], f"Violations found: {result['violations']}"
