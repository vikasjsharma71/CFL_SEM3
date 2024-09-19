import logging

# Configure the logger
logger = logging.getLogger('cfprac2')
logger.setLevel(logging.DEBUG)

# Create a file handler that logs debug and higher level messages
file_handler = logging.FileHandler('D:/mylogfile.log', mode='a')  # 'a' for append mode
file_handler.setLevel(logging.DEBUG)

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)

# Log messages
logger.info("My first log")
logger.info("This is CFL Prac 2")

print("Logging complete. Check 'D:/mylogfile.log' for details.")
