# Introduction

This is going to be a full Python to Objective-C Interface Definition Language.

Using the python pyobjc adapter, users will be able to define python-Objective-C bridge classes and auto-generate the corresponding code.

This repo will contain a fully functional introductory example, as well.

## Status

* Very developmental. 
* Right now, rudimentary .py and .h files are being generated.
* A handful of types are supported, more to be added.
* It is unknown if the generated .py and .h files will link against each other. That's the next big step.


## Overview

* Based on ply for the lexing and parsing.
* 

A .poidl (py to objc interface definition language) file will look like this:

```
class POSimple
{
    int simple_int;
    string simple_string;
    dict simple_dict;
    mutable_dict simple_mutable_dict;
    array simple_array;
    mutable_array simple_mutable_array;
    boolean simple_boolean;
    function void simple_func(int test);
};
	
```

It's a C++-esque, curly-bracket and semi-colon language;

## Wish list
* optional arguments
* automatic init functions generated in python and objective-c
* test suite
