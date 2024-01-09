# utils/axe_utils.py

import logging
from axe_selenium_python import Axe

# Configure logging
logging.basicConfig(filename='repor/accessibility_log.txt', level=logging.INFO)

# execute aXe violations validation
def execute_accessibility_validation(driver):
    # Create aXe instance with the driver
    axe = Axe(driver)
    
    # Injecting the aXe script into the browser
    axe.inject()
    
    # Running the accessibility check
    results = axe.run()

    # Checking for accessibility violations
    violations = results["violations"]
    
    # Printing and/or Logging violations
    for violation in violations:
        #print(f"Violation: {violation['help']}") # best for local runs & debug
        logging.info(f"Violation: {violation['help']}") # best for ci/cd runs

    return results
