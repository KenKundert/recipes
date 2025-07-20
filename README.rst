Recipes by Kara
===============

Recipes are contained in NestedText files, one per file, and the files are 
placed in the subdirectories of ~/home/recipes.  Recipes should take the form:

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
example, if the above recipe is found in glutinous-rice.nt, then you can find it 
using::

    > recipe -n rice
    deserts/glutinous-rice

You can display the entire recipe with::

    > recipe rice

If there are other recipes with *rice* in the name they will also be displayed, 
so you can narrow down to the one you want using::

    > recipe glutinous-rice

Finally, you can get a list of the ingredients using:

    > recipe -i rice
    name: glutinous rice
    ingredients:
        - 1 cup black glutinous rice
        - 2/3 cup water
