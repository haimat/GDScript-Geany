GDScript-Geany
==============

This is the *GDScript* syntax definition for the Geany text editor / IDE.
GDScript is the scripting language for the [Godot Game Engine](http://www.godotengine.org/).
Geany is a text editor or lightweight IDE for Linux ([more information here](http://www.geany.org/)).

Installation
------------

First copy the file `filetypes.GDScript.conf` from this repo into the folder `~/.config/geany/filedefs`.
Then within Geany open the menu "Tools -> Configuration Files -> filetype_extensions.conf" and add the
following line into the `[Extensions]` section:

    [Extensions]
    ...
    GDScript=*.gd;
    ...

And still in the same configuration file modify the `[Groups]` section as follows:

    [Groups]
    ...
    Script=GDScript;
    ...

After restarting Geany should automatically set the filetype to GDScript when you open a `.gd` file.

Godot Setup
-----------

The last step is to tell Godot to use Geany as the external source code editor for GDScript files.
In the Godot environment open the *Settings* menu (in the top-right corner) and select *Editor Settings*.
Here scroll down until you find the options category called *External Editor*. Simply enter the path to your
editor executable, for example `/usr/bin/geany`, and activate the *User External Editor* checkbox.

**Have fun!**
