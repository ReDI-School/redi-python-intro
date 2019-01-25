# Markdown-based slides for Intro to Python course (work in progress)

## Description
Slides for the "Intro to Python" course made by
[ReDI School of Digital Integration](https://www.redi-school.org/berlin).

## Contents
* Topic 1
* Topic 2
* Topic 3
...

## Structure
* Topic*
* cmake
* remark.js
* Example
* CMakeLists.txt
* resources


## Prerequisites
* [Python3](https://www.python.org/downloads/) - to insert python code into slides before
compiling them into HTML
* [CMake](https://cmake.org/install/) - to manage compilation of Markdown files into HTML

## Usage
# Slides compilation
* Create an output folder
* From the output folder run once (to generate CMake files):
```bash
cmake /path-to-slides-2-0/
```
* After that from the output folder run:
```bash
cmake --build .
```
* When you change some slides, you have only to re-run the last command - CMake will
notice the changes and re-compile only needed files by itself
* Generated slides in HTML are stored in **out** folder inside the output folder.

# Slides editing
Slides are stored as [Markdown](https://daringfireball.net/projects/markdown/) files and
sets of resources. They are compiled to HTML files using
[remark.js](https://github.com/gnab/remark). The cmake-based build system is made using
[remark-cmake](https://github.com/train-it-eu/remark-cmake) project.\
The only additional feature is adding code from Python files into slides before slides
compilation. This is done by a custom cmake module
[replace-by-file-contents](cmake/replace-by-file-contents.cmake) which triggers the
[Python script](cmake/replace-by-file-contents.py).\
The script checks the given input file for the line starting from the words
"_PLEASE_REPLACE_BY_FILE_CONTENT:", considers everything that follows this keyword to be a
path to a Python file and inserts it's content instead of that line.\
Therefore the slides, containing Python code, may be described in file "slides.md.in",
then the file "slides.md" is generated after Python code substitution and the latter file
is used by remark.js to generate the resulting HTML page.

# Handouts generation
Handouts html is generated automatically near the slides html (called handouts.html).\
Handouts excludes animated slides (they are put in the same slide) and slides which are marked explicitly
to be excluded from the handouts (see [remark-cmake documentation]((https://train-it-eu.github.io/remark-cmake/Slides_about_CMake_with_CMake/Slides_about_CMake_with_CMake.html#1))
for more details).\
Handouts can be converted to pdf either with browser, or with [ecktape](https://github.com/astefanutti/decktape).

Useful resources:
* [Markdown syntax](https://daringfireball.net/projects/markdown/syntax)
* [Quick introduction to remark.js](https://remarkjs.com/#1)
* [Remark.js wiki](https://github.com/gnab/remark/wiki)
* [Quick introduction to remark-cmake](https://train-it-eu.github.io/remark-cmake/Slides_about_CMake_with_CMake/Slides_about_CMake_with_CMake.html#1)
* [remark-cmake API reference](https://train-it-eu.github.io/remark-cmake/api_reference/api_reference.html#1)

# Notes
* VSCode seems to be quite convenient tool for working with CMake-based projects containing Python and Markdown code (after installing CMake and Python extensions from the official extensions marketplace)

## The repository is under development at the moment
### TODO next
* Add all contents of the old PowerPoint slides here as markdown files and resources
* Complete this readme file
* Publish generated HTMLs
* Add html and pdf handouts generation as cmake targets
* Try to get rid of Python3 dependency for the build-system (implement code substitution in CMake)






