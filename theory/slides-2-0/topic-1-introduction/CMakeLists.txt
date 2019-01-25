# Add slides as target
add_remark_slides(topic-1-slides ALL HANDOUTS
    NAME "topic-1-introduction"
    TITLE "Intro to Python: Introduction"
    STYLE redi-style
    MARKDOWN_SLIDES slides.md
    RESOURCES
        img/python-logo.png
        img/coding-fire-big.gif
        img/studying-girl.jpg
        img/projects-examples.png
        img/program.png
        img/bicycle.png
        img/curious.png
        img/interpreter.png
        img/python-success.png
        img/download-python.png
        img/pycharm-welcome.png
        img/pycharm-create-project.png
        img/pycharm-create-file.png
        img/pycharm-file-name.png
        img/pycharm-select-project.png
)

# Set a list of python files used in slides
set(python_files
        ${CMAKE_CURRENT_SOURCE_DIR}/python/two-instructions.py
        ${CMAKE_CURRENT_SOURCE_DIR}/python/hello.py
        ${CMAKE_CURRENT_SOURCE_DIR}/python/hello-comments.py
        ${CMAKE_CURRENT_SOURCE_DIR}/python/hello-broken.py
        )

# Set a task to put python code in slides before building the slides
replace_by_file_contents(topic-1-slides ${CMAKE_CURRENT_SOURCE_DIR}/slides.md.in ${CMAKE_CURRENT_SOURCE_DIR}/slides.md "${python_files}")