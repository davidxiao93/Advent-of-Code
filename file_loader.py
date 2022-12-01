import inspect
from pathlib import Path
import os

def get_input():
    caller_frame = inspect.stack()[1]
    p = Path(caller_frame.filename)
    problem = p.stem[:2]
    input_file_path_parts = list(p.parts)[:-1] + [problem + ".txt"]
    input_file_path = os.path.join(*input_file_path_parts)
    with open(input_file_path) as f:
        input_contents = ''.join(f.readlines())
    if input_contents[-1] == "\n":
        input_contents = input_contents[:-1]
    return input_contents
