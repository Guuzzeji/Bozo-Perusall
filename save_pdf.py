import os
import sys
import base64
import shutil
from pypdf import PdfWriter

_CURRENT_DIR = os.path.join(os.getcwd(), 'tmp')


class SavePDF():
    def __init__(self, filename: str, export_path: str) -> None:
        self.filename = filename
        self.export_path = export_path
        self.pdf_files: list[str] = []
        self._make_work_folder()

    def __del__(self) -> None:
        self.pdf_files = []
        self._clean_work_folder()

    def _make_work_folder(self) -> None:
        if not os.path.exists(_CURRENT_DIR):
            os.makedirs(_CURRENT_DIR)
        self._clean_work_folder()

    def _clean_work_folder(self) -> None:
        if os.path.exists(_CURRENT_DIR):
            for filename in os.listdir(_CURRENT_DIR):
                file_path = os.path.join(_CURRENT_DIR, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))
                    sys.exit(1)

    def save_page(self, base64_content: str, filename: str) -> None:
        file_path = os.path.join(_CURRENT_DIR, filename+'.pdf')
        self.pdf_files.append(file_path)
        with open(file_path, 'wb') as f:
            f.write(base64.b64decode(base64_content))

    def merge_pages(self) -> None:
        merger = PdfWriter()
        if len(self.pdf_files) != 0:
            for page in self.pdf_files:
                merger.append(page)
            merger.write(os.path.join(
                self.export_path, self.filename + ".pdf"))
            merger.close()
