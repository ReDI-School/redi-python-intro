function(replace_by_file_contents target infile outfile sourcefiles)
    add_custom_command(
        OUTPUT ${outfile}
        COMMAND "${CMAKE_SOURCE_DIR}/cmake/replace-by-file-contents.py" ${infile} ${outfile}
        DEPENDS ${infile} ${sourcefiles}
        COMMENT "Generating " ${outfile}
        WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
    )

    set(replace_target_name ${target}_preprocess_code)

    add_custom_target(
        ${replace_target_name}
        DEPENDS ${outfile}
    )

    add_dependencies(${target} ${replace_target_name})
endfunction(replace_by_file_contents)