from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path
from os import mkdir
from json import load
from time import time

out = Path("./docs")

env = Environment(
    loader=FileSystemLoader("./src/web/www"),
    autoescape=select_autoescape()
)

with open("context.json", "r") as context_file:
    context = load(context_file)

with open("export.txt", "r") as export:
    for line in export.readlines():
        t = time()
        url = line.strip().removeprefix("/")
        dest = out / Path(url)
        ddir = dest.parent
        if not ddir.exists():
            ddir.mkdir(parents=True)

        template = env.get_template(url)
        with open(dest, "w") as dest_file:
            dest_file.write(template.render(context))
        print("rendering",url,time()-t,"s")

