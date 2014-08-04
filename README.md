# Introduction

This is going to be a full Python to Objective-C Interface Definition Language.

Using the python pyobjc adapter, users will be able to define python-Objective-C bridge classes and auto-generate the corresponding code.

This repo will contain a fully functional introductory example, as well.

## Usage
* `python pyobjcidl.py --source-file=./test/simple.poidl --py-dest-dir='./test/' --objc-dest-dir='./test'`
* 

## Status

* Very developmental. 
* Right now, rudimentary .py and .h files are being generated.
* A handful of types are supported, more to be added.
* It is unknown if the generated .py and .h files will link against each other. That's the next big step.


## TODO 

- [x] add requirements.txt
- [x] implement whole directory scanning
- [ ] import statements
- [x] enforce no _ in func or variable names
- [ ] generate objc decorators in python
- [ ] don't generate the _concrete class if it already exists
- [ ] maybe parse the concrete class using a separate lexer to find out what functions it already contains
- [x] a python program that can call the main from all generated python classes
- [ ] instructions on using py2App
- [ ] working example
- [ ] setup.py
- [ ] unit tests


## Overview

* Based on ply for the lexing and parsing.
* Uses jinja as templates for generated .py and .h files
* Uses py2app to generate a plugin that can be referenced from a Cocoa project

A .poidl (py to objc interface definition language) file will look like this:

```
class POSimple
{
    int simple;
};
	
```

It's a C++-esque, curly-bracket and semi-colon language;

## Wish list
* optional arguments
* automatic init functions generated in python and objective-c
* test suite
