Recipes by Kara
===============

Recipes are contained in NestedText files, one per file, and the files are 
placed in the subdirectories of ~/home/recipes.  Recipes should take the form::

    name: glutinous rice
    ingredients:
        - 1 cup black glutinous rice
        - 2/3 cup water
    steps:
        - pressure cook on high for 18 minutes
        - allow pressure to release for 10 minutes
    comments:
        - add 1/4 can coconut milk and 1/8 cup sugar to make into a desert

The files can be placed in any number of subdirectories.
The filenames should end with the .nt suffix.

You can find recipes by searching for terms found in their file names.  For 
example, if the above recipe is found in glutinous-rice.nt, then you can display 
it using::

    > recipe rice

If there are other recipes with *rice* in the name they listed. You can narrow 
down to the one you want by giving more of the name::

    > recipe glutinous-rice

Or you can show all of them using::

    > recipe -a glutinous-rice

Finally, you can get a list of the ingredients using::

    > recipe -i rice
    name: glutinous rice
    ingredients:
        - 1 cup black glutinous rice
        - 2/3 cup water


Installation
------------

You can install using::

    git clone https://github.com/KenKundert/recipes.git
    cd recipes
    pip install .
