
import os
import sys
from datetime import datetime

FILE_INPUT_DIR = "file_inputs"
FILE_OUTPUT_DIR = "file_outputs"

def format_outfile_name(basename, extension="csv"):
    file = f"{basename}_{datetime.now().strftime('%Y-%m-%d_%H%M')}_res.{extension}"
    return os.path.join(FILE_OUTPUT_DIR,file)

