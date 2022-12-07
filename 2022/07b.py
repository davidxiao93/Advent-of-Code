from __future__ import annotations
from typing import List, Dict, Tuple

import file_loader

input_string = file_loader.get_input()


Output = List[str]
Command = List[str]
commands: List[Tuple[Command, Output]] = []
current_command: Tuple[Command, Output] = ([], [])
for line in input_string.splitlines():
    if line.startswith("$"):
        if current_command != ([], []):
            commands.append(current_command)
        current_command = (line.split()[1:], [])
    else:
        current_command = (current_command[0], current_command[1] + [line])
commands.append(current_command)


class Directory:
    def __init__(self):
        self.parent: Directory = None
        self.files: Dict[str, int] = {}
        self.directories: Dict[str, Directory] = {}
        self.total_size = -1

    def size(self) -> int:
        if self.total_size != -1:
            return self.total_size
        return sum(self.files.values()) + sum([d.size() for d in self.directories.values()])


root = Directory()

pwd = root
output: List[str] = []
for command in commands:
    c = command[0]
    if c[0] == "ls":
        for o in command[1]:
            if o.startswith("dir"):
                dirname = o.split()[-1]
                if dirname not in pwd.directories:
                    pwd.directories[dirname] = Directory()
                    pwd.directories[dirname].parent = pwd
            else:
                size = int(o.split()[0])
                filename = o.split()[-1]
                if filename not in pwd.files:
                    pwd.files[filename] = size
    elif c[0] == "cd":
        if c[1] == "..":
            pwd = pwd.parent
        elif c[1] == "/":
            pwd = root
        else:
            dirname = c[1]
            pwd = pwd.directories[dirname]

required_space = 30_000_000 - (70_000_000 - root.size())
smallest = 70_000_000

dirs_to_check = [root]
while len(dirs_to_check) > 0:
    d = dirs_to_check.pop(0)
    if d.size() >= required_space and d.size() < smallest:
        smallest = d.size()
    dirs_to_check += d.directories.values()

print(smallest)

