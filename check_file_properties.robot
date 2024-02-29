*** Settings ***
Library    OperatingSystem
Library    Collections
Library    CSVLibrary

*** Variables ***
${directory_path}       com.nexign/people
${b2b_prefix}           b2b_
${b2c_prefix}           b2c_
${b2b_count}            7
${b2c_count}            6
${expected_columns}    name b_day active po
${expected_rows_count}  101

*** Test Cases ***
Check File Names
    Check File Names
Check Tables Headers
    Check Headers
Check Rows Count
    Check Rows Count

*** Keywords ***
Check File Names
    [Documentation]    Check File Names
    ${b2b_files}=    List Files In Directory    ${directory_path}    ${b2b_prefix}*
    ${b2c_files}=    List Files In Directory    ${directory_path}    ${b2c_prefix}*

    ${b2b_count_in_directory}=    Get Match Count    ${b2b_files}    ${b2b_prefix}*
    ${b2c_count_in_directory}=    Get Match Count    ${b2c_files}    ${b2c_prefix}*

    Should Be Equal As Numbers    ${b2b_count_in_directory}    ${b2b_count}
    Should Be Equal As Numbers    ${b2c_count_in_directory}    ${b2c_count}

Check Headers
    [Documentation]    Check Headers
    @{csv_tables} =    Create List
    FOR    ${index}    IN RANGE    1    8
        Append To List    ${csv_tables}    ${b2b_prefix}${index}.csv
    END
    FOR    ${index}    IN RANGE    1    7
        Append To List    ${csv_tables}    ${b2c_prefix}${index}.csv
    END
    FOR    ${table}    IN    @{csv_tables}
        ${file_path} =    Join Path    ${directory_path}    ${table}
        ${table_data} =    Read CSV File to List    ${file_path}
        ${headers} =    Get From List    ${table_data}    0
        Check If Headers Match    ${headers}
    END

Check If Headers Match
    [Arguments]    ${actual_headers}
    @{expected_headers} =    Create List    name    b_day    active    po
    Lists Should Be Equal    ${actual_headers}    ${expected_headers}

Check Rows Count
    [Documentation]    Check Rows Count
    @{csv_tables} =    Create List
    FOR    ${index}    IN RANGE    1    8
        Append To List    ${csv_tables}    ${b2b_prefix}${index}.csv
    END
    FOR    ${index}    IN RANGE    1    7
        Append To List    ${csv_tables}    ${b2c_prefix}${index}.csv
    END
    FOR    ${table}    IN    @{csv_tables}
        ${file_path} =    Join Path    ${directory_path}    ${table}
        ${table_data} =    Read CSV File to List    ${file_path}
        ${number_of_rows} =    Get Length    ${table_data}
        Should Be Equal As Numbers    ${number_of_rows}    ${expected_rows_count}
    END