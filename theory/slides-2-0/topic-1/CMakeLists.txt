# Add slides as target
add_remark_slides(topic-1-slides ALL
    NAME "intro-to-python-introduction"
    TITLE "Intro to Python: Introduction"
    STYLE remark-style-default
    STYLE_TEMPLATE style.css.in
    MARKDOWN_SLIDES slides.md
    RESOURCES
        img/redi-logo.png
        img/python-logo.png
)

# Set a list of python files used in slides
set(python_files
        python/two-instructions.py
        python/hello.py)

# Set a task to put python code in slides before building the slides
replace_by_file_contents(topic-1-slides slides.md.in slides.md "${python_files}")