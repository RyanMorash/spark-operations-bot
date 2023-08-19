import os
from CollabConnector import CUCM

# ========================================================
# Load required parameters from environment variables
# ========================================================

cucm_username = os.getenv("CUCM_USERNAME")
cucm_password = os.getenv("CUCM_PASSWORD")
cucm_host = os.getenv("CUCM_HOST")

# ========================================================
# Initialize Program - Define Global Variables
# ========================================================

# Define CUCM connection object
cucm = CUCM.Connect(cucm_host, cucm_username, cucm_password)

# ========================================================
# Initialize Program - Function Definitions
# ========================================================

def cucm_getPhones():
    # Get a list of phones
    phone_list = cucm.get.Phone()
    return phone_list
