# utils/axe_utils.py

# import dependencies
from axe_selenium_python import Axe

# execute aXe violations validation
def execute_acessibility_validation(driver):
    # Create aXe instance with the driver
    axe = Axe(driver)
    
    # Injecting the aXe script into the browser
    axe.inject()
    
    # Running the accessibility check
    results = axe.run()

    # Checking for accessibility violations
    violations = results["violations"]
    
    # Printing the violations
    for violation in violations:
        print(f"Violation: {violation['help']}")
    
    return results
