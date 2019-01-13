# Add slides as target
add_remark_slides(example_presentation ALL
    NAME "intro-to-python-input-variables"
    TITLE "Intro to Python: User Input and Variables"
    STYLE remark-style-default
    STYLE_TEMPLATE style.css.in
    MARKDOWN_SLIDES slides.md
    RESOURCES
        img/program.png
)

# Set a list of python files used in slides
set(python_files 
        python/two-instructions.py 
        python/hello.py)

# Set a task to put python code in slides before building the slides
replace_by_file_contents(example_presentation slides.md.in slides.md "${python_files}")