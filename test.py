from aerologger.aerologger import AeroLogger
import json
import random

name = "test"
log_file = "test_logs/test.log"

logger = AeroLogger(name, log_file)

data = {"CLIENT_ID": 10024, "PROJECT_ID": 101047, "STAND_ID": 100}
success_msgs = ["Starting project for \n{}", "Finished project for \n{}"]
err_msg = """Error for project\nTraceback (most recent call last):
  File "example_script.py", line 4, in <module>
    print(divide_numbers(10, 0))
  File "example_script.py", line 2, in divide_numbers
    return x / y
ZeroDivisionError: division by zero
"""

for i in range(1000):
    logger.info(success_msgs[0].format(json.dumps(data, indent=4)))
    if random.randint(0, 10) <= 3:
        logger.error(err_msg)
    else:
      logger.info(success_msgs[1].format(json.dumps(data, indent=4)))
