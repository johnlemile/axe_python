#tests/test_accessibility.py

# adding stuff to venv $PYTHONPATH
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import dependencies
import pytest
import json
import logging
from selenium import webdriver
from pages.sample_page import SamplePage
from utils.axe_utils import execute_accessibility_validation

# Configure logging
logging.basicConfig(filename='report/accessibility_log.txt', level=logging.INFO)

class TestAccessibility:
    @pytest.fixture
    def setup_teardown(self):
        self.driver = webdriver.Chrome()
        self.base_url = json.load(open("config.json"))["url"]
        self.page = SamplePage(self.driver, self.base_url)
        yield
        self.driver.quit()


    def test_accessibility_violations_positive(self, setup_teardown):
        self.page.open()
        result = execute_accessibility_validation(self.driver)
        # Check for violations
        assert result["violations"], "No accessibility violations found."

    def test_accessibility_violations_negative(self, setup_teardown):
        self.page.open()
        result = execute_accessibility_validation(self.driver)
        # Check for violations
        violations = result["violations"]
        if violations:
            # Log violations
            for violation in violations:
                print(f"Violation: {violation['help']}")  # best for local run & debug
                #logging.info(f"Violation: {violation}")  # best for ci/cd runs
            # Fail the test if violations are present
            pytest.fail("Accessibility violations found.")

    def test_specific_accessibility_violation(self, setup_teardown):
        self.page.open()
        result = execute_accessibility_validation(self.driver)
        accepted_violations = [
            'Ensures role attribute has an appropriate value for the element',
            'Ensures buttons have discernible text',
            'Ensures the contrast between foreground and background colors meets WCAG 2 AA contrast ratio thresholds',
            'Ensures the page has only one main landmark and each iframe in the page has at most one main landmark',
            'Ensures every id attribute value is unique',
            # Add other accepted violations
        ]
        # Allow the accepted violation(s)
        violations = [violation['description'] for violation in result["violations"]]
        unexpected_violations = set(violations) - set(accepted_violations)
        if unexpected_violations:
            # Log unexpected violations
            for violation in unexpected_violations:
                print(f"Unexpected Violation: {violation}")  # best for local run & debug
                #logging.info(f"Unexpected Violation: {violation}")  # best for ci/cd runs
            # Fail the test if unexpected violations are present
            pytest.fail("Unexpected accessibility violations found.")
            
    def test_accessibility_violations(self, setup_teardown):
        self.page.open()
        result = execute_accessibility_validation(self.driver)
        
        # Check for all accessibility violations
        if result["violations"]:
            # Log all violations
            for violation in result["violations"]:
                print(f"Violation: {violation['help']}")  # best for local run & debug
                #logging.info(f"Violation: {violation}")  # best for ci/cd runs
            # Fail the test if any violations are present
            pytest.fail("Accessibility violations found.")