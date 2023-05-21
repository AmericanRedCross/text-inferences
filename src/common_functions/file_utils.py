
import os
import sys
from datetime import datetime

FILE_INPUT_DIR = "file_inputs"
FILE_OUTPUT_DIR = "file_outputs"

def format_outfile_name(executing_script, format="csv"):
    file = f"{executing_script}_{datetime.now().strftime('%Y-%m-%d_%H%M')}_res.{format}"
    return os.path.join(FILE_OUTPUT_DIR,file)

