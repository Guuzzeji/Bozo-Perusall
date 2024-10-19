import sys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.print_page_options import PrintOptions

from login import Login
from save_pdf import SavePDF


class PageContentGather(Login):
    def grab_assignment(self, assignment_url: str, filename: str, export_path: str) -> None:
        if not self.is_login:
            print("[ERROR] --> Not logged in")
            sys.exit(1)

        pdf_writer = SavePDF(filename=filename, export_path=export_path)
        self.driver.get(assignment_url)
        original_tab = self.driver.current_window_handle
        sleep(5)

        if not self._epub_exist():
            print("[ERROR] --> Failed to find epub container")
            sys.exit(1)

        pages = self.driver.find_element(By.ID, "epub-container").find_elements(By.TAG_NAME, "iframe")

        page_count = 0
        for page in pages:
            # Get src link to epub page
            epub_url = page.get_attribute("src")
            self.driver.switch_to.new_window("tab")
            self.driver.get(epub_url)
            sleep(5)

            print("[GARBING PDF FROM] --> " + epub_url)

            # Print options
            print_options = PrintOptions()
            print_options.page_width = self.driver.get_window_rect()['y']
            print_options.page_height = self.driver.get_window_rect()['x']

            # Save page
            pdf_page = self.driver.print_page(print_options=print_options)
            pdf_writer.save_page(pdf_page.encode(), 'page-' + str(page_count))

            # Close tab
            self.driver.close()
            self.driver.switch_to.window(original_tab)
            page_count += 1

        print("[MERGING PAGES INTO PDF]")
        pdf_writer.merge_pages()

    def _epub_exist(self) -> bool:
        return len(self.driver.find_elements(By.ID, "epub-container")) > 0
