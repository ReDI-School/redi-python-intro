# Add slides as target
add_remark_slides(topic-2-slides ALL HANDOUTS
    NAME "topic-2-interactive-programs"
    TITLE "Intro to Python: Interactive Programs"
    STYLE redi-style
    MARKDOWN_SLIDES slides.md
    RESOURCES
        img/program.png
        img/variable.png
)

# Set a list of python files used in slides
set(python_files
        ${CMAKE_CURRENT_SOURCE_DIR}/python/two-instructions.py
        ${CMAKE_CURRENT_SOURCE_DIR}/python/input.py
        ${CMAKE_CURRENT_SOURCE_DIR}/python/integers.py
        ${CMAKE_CURRENT_SOURCE_DIR}/python/floats.py)

# Set a task to put python code in slides before building the slides
replace_by_file_contents(topic-2-slides ${CMAKE_CURRENT_SOURCE_DIR}/slides.md.in ${CMAKE_CURRENT_SOURCE_DIR}/slides.md "${python_files}")