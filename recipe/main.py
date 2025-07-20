# DESCRIPTION {{{1
"""
Recipes by Kara

Recipes are kept in {db}

Usage:
    recipe [options] <term>

Options:
    --ingredients, -i  just show the list of ingredients
"""

# IMPORTS {{{1
from docopt import docopt
from inform import error, fatal, os_error, did_you_mean, InformantFactory
from pathlib import Path
import nestedtext as nt

# PARAMETERS {{{1
RECIPES_DATABASE = "~/home/recipes"
highlight = InformantFactory(message_color="cyan")

# UTILITY FUNCTIONS {{{1
# display_path() {{{2
def display_path(path):
    highlight(f"{path!s}:")

# display_ingredients() {{{2
def display_ingredients(paths):
    more_than_one = len(paths) > 1
    for path in paths:
        if more_than_one:
            display_path(path)

        # load the nestedtext file
        try:
            recipe = nt.load(path, top=dict)
        except OSError as e:
            error(os_error(e))
            return
        except nt.NestedTextError as e:
            e.report()

        # just display the name and ingredients, NT is convenient format
        to_display = dict(
            Name = recipe.get('name', path.stem),
            Ingredients = recipe.get('ingredients', '')
        )
        print(nt.dumps(to_display))
        if more_than_one:
            print()

# display_recipe() {{{2
# Currently NestedText reader completely ignores comments.
# Avoid NT reader and just dump the whole file.
def display_recipes(paths):
    more_than_one = len(paths) > 1

    for path in paths:
        if more_than_one:
            display_path(path)
        print(path.read_text().strip())
        if more_than_one:
            print()

# MAIN {{{1
def main():
    cmdline = docopt(__doc__.format(db=RECIPES_DATABASE))
    term = cmdline["<term>"].lower()
    seen = set()
    found = []

    for root, dirs, files in Path(RECIPES_DATABASE).expanduser().walk():
        for filename in files:
            path = root/filename
            if path.suffix != '.nt':
                continue
            basename = path.name.lower()
            seen.add(basename)
            if term in basename:
                found.append(path)

    if not found:
        if seen:
            fatal(
                "not found.", culprit=term,
                codicil=f"did you mean {did_you_mean(term, seen)}?"
            )
        else:
            fatal(f"no recipes found in {RECIPES_DATABASE}")

    if len(found) > 1:
        highlight("choose from ...")
        for path in found:
            print(path.stem)
    elif cmdline['--ingredients']:
        display_ingredients(found)
    else:
        display_recipes(found)
