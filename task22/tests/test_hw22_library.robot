*** Settings ***
Library    BuiltIn
Library    ../source/hw22_library.py

*** Variables ***
${BOOK_NAME}     1984
${AUTHOR}        George Orwell
${PAGES}         328
${ISBN}          978-0451524935
${READER_1}      Alice
${READER_2}      Bob

*** Test Cases ***

Successful Reservation By Reader
    ${book}=    Create Book    ${BOOK_NAME}    ${AUTHOR}    ${PAGES}    ${ISBN}
    ${reader}=    Create Reader    ${READER1}
    ${result}=    Reserve Book    ${reader}    ${book}
    Should Be True    ${result} == True

Reservation By Incorrect Reader Fails
    ${book}=    Create Book    ${BOOK_NAME}    ${AUTHOR}    ${PAGES}    ${ISBN}
    ${reader1}=    Create Reader    ${READER1}
    ${reader2}=    Create Reader    ${READER2}
    Reserve Book    ${reader1}    ${book}
    ${result}=    Reserve Book    ${reader2}    ${book}
    Should Be True    ${result} == False

Successful Get Of Reserved Book
    ${book}=    Create Book    ${BOOK_NAME}    ${AUTHOR}    ${PAGES}    ${ISBN}
    ${reader}=    Create Reader    ${READER1}
    Reserve Book    ${reader}    ${book}
    ${result}=    Get Book    ${reader}    ${book}
    Should Be True    ${result} == True

Return Book Fails From Incorrect Reader
    ${book}=    Create Book    ${BOOK_NAME}    ${AUTHOR}    ${PAGES}    ${ISBN}
    ${reader1}=    Create Reader    ${READER1}
    ${reader2}=    Create Reader    ${READER2}
    Get Book    ${reader1}    ${book}
    ${result}=    Return Book    ${reader2}    ${book}
    Should Be True    ${result} == False

Successful Return By Correct Reader
    ${book}=    Create Book    ${BOOK_NAME}    ${AUTHOR}    ${PAGES}    ${ISBN}
    ${reader}=    Create Reader    ${READER1}
    Get Book    ${reader}    ${book}
    ${result}=    Return Book    ${reader}    ${book}
    Should Be True    ${result} == True
