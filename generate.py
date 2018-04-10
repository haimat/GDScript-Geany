#!/usr/bin/python3
"""
This file generates the geany filetype definition from the godot
documentation. This should make it easuer to keep it up to date. To run
it, you need to pass in the path to the documentation directory. For 
example:
	/generate.py ~/src/godot-docs
"""
import argparse
import configparser
import os
import sys

OUTFILE = 'filetypes.GDScript.conf'

HEADER = """\
Original Author: Matthias F. Brandstetter <pub@mabra.me>
Copyright (C) 2014 Matthias F. Brandstetter <pub@mabra.me>

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Library General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Library General Public License for more details.

You should have received a copy of the GNU Library General Public
License along with this library; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.\
"""


def get_keywords(input_dir):
	# TODO: Can we parse the gdscript_basics docs page for this?
	return "and break class const continue elif else enum export extends false for func if in null or pass preload return self tool true var while static".split(" ")


def get_global_functions(input_dir):
	functions = []
	with open(input_dir+'/classes/class_@gdscript.rst') as base_types:
		for line in base_types.readlines():
			pos = line.find('_class_@GDScript_')
			if pos != -1:
				end = line.find(':', pos)
				functions.append(line[pos+len('_class_@GDScript_'):end])
	return functions
	
def get_classes(input_dir):
	classes = []
	for file_name in os.listdir(input_dir+'/classes/'):
		# capitilization means we will need to parse these files
		if file_name.startswith('class_'):
			with open(input_dir+'/classes/'+file_name) as class_data:
				class_name = class_data.readlines()[6]
				classes.append(class_name.strip())
	return classes


def generate(input_dir):
	config = configparser.ConfigParser()
	config['styling'] = {
		"default": "default",
		"commentline": "comment_line",
		"number": "number_1",
		"string": "string_1",
		"character": "character",
		"word": "keyword_1",
		"triple": "string_2",
		"tripledouble": "string_2",
		"classname": "type",
		"defname": "function",
		"operator": "operator",
		"identifier": "identifier_1",
		"commentblock": "comment",
		"stringeol": "string_eol",
		"word2": "keyword_2",
		"decorator": "decorator",
	}
	IDENTIFIERS = get_global_functions(input_dir) + get_classes(input_dir)
	PRIMARY = get_keywords(input_dir)

	config['keywords'] = {
		"primary": " ".join(p for p in PRIMARY),
		"identifiers": " ".join(i for i in IDENTIFIERS)
	}

	config['lexer_properties'] = {
		"fold.comment.python": 1,
		"fold.quotes.python": 1
	}

	config['settings'] = {
		"extension": "gd",
		"lexer_filetype": "Python",
		"comment_single": "#",
		"comment_use_indent": False,
		
	}

	config['indentation'] = {
		"width": 4,
		"type": 1  # 1 is tabs
	}

	config['build_settigs'] = {

	}
	return config
	
def main(args):
	parser = argparse.ArgumentParser(description='Generate geany file definition')
	parser.add_argument('docs_dir', type=str, nargs=1,
						help='Path to a clone of the godot-docs repo')
	
	config = parser.parse_args(args)
	with open(OUTFILE, 'w') as configfile:
		for line in HEADER.split('\n'):
			configfile.write('\n## ' + line)
		configfile.write('\n\n')
	with open(OUTFILE, 'a') as configfile:
		config = generate(config.docs_dir[0])
		config.write(configfile)


if __name__ == "__main__":
	main(sys.argv[1:])
