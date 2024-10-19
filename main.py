"""
Main program for cli
"""

import sys
from selenium import webdriver

from page_content_gather import PageContentGather

print(r"""
______  _____  ___________  ______                         _ _ 
| ___ \|  _  ||___  /  _  |_| ___ \                       | | |
| |_/ /| | | |   / /| | | (_) |_/ /__ _ __ _   _ ___  __ _| | |
| ___ \| | | |  / / | | | | |  __/ _ \ '__| | | / __|/ _` | | |
| |_/ /\ \_/ /./ /__\ \_/ /_| | |  __/ |  | |_| \__ \ (_| | | |
\____/  \___/ \_____/\___/(_)_|  \___|_|   \__,_|___/\__,_|_|_|

    === Bypass print limit and save readings as PDFs === 
""")

username = input("Username: ")
password = input("Password: ")
assignment_url = input("Assignment URL: ").strip()
filename = input("Filename: ")
export_path = input("Save file to: ").strip()

print("\nRunning...\n")

# Note some issue running in headless mode, will not switch between tabs for some reason
grabber = PageContentGather(driver=webdriver, headless=False)

try:
    grabber.login_to_perusall(username=username, password=password)
    grabber.grab_assignment(assignment_url=assignment_url,
                            filename=filename,
                            export_path=export_path)

except Exception as e:
    print("[ERROR] --> ", e)

grabber.close_browser()
sys.exit(0)
