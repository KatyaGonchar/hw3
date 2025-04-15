*** Settings ***
Library    BuiltIn
Library    ../source/hw22_bank.py

*** Variables ***
${CLIENT_ID}         1
${CLIENT_NAME}       Ivan
${START_BALANCE}     10000
${YEARS}             2

*** Test Cases ***

Register Client Successfully
    ${result}=    Register Client    ${CLIENT_ID}    ${CLIENT_NAME}
    Should Be True    ${result} == True

Open Deposit Account Successfully
    Register Client    ${CLIENT_ID}    ${CLIENT_NAME}
    ${result}=    Open Deposit Account    ${CLIENT_ID}    ${START_BALANCE}    ${YEARS}
    Should Be True    ${result} == True

Open Deposit Fails For Unregistered Client
    ${result}=    Open Deposit Account    999    ${START_BALANCE}    ${YEARS}
    Should Be True    ${result} == False

Calculate Correct Interest
    Register Client    ${CLIENT_ID}    ${CLIENT_NAME}
    Open Deposit Account    ${CLIENT_ID}    ${START_BALANCE}    ${YEARS}
    ${result}=    Calc Deposit Interest Rate    ${CLIENT_ID}
    ${expected}=    Evaluate    round(${START_BALANCE} * (1 + 0.1 / 12) ** (12 * ${YEARS}), 2)
    Should Be Equal As Numbers    ${result}    ${expected}

Calc Interest Fails For Unregistered Client
    ${result}=    Calc Deposit Interest Rate    999
    Should Be True    ${result} == False

Calc Interest Fails If No Deposit
    Register Client    ${CLIENT_ID}    ${CLIENT_NAME}
    ${_}=    Close Deposit    ${CLIENT_ID}
    ${result}=    Calc Deposit Interest Rate    ${CLIENT_ID}
    Should Be True    ${result} == False

Close Deposit Successfully
    Register Client    ${CLIENT_ID}    ${CLIENT_NAME}
    Open Deposit Account    ${CLIENT_ID}    ${START_BALANCE}    ${YEARS}
    ${result}=    Close Deposit    ${CLIENT_ID}
    Should Be True    ${result} == True

Close Deposit Fails For Unregistered Client
    ${result}=    Close Deposit    999
    Should Be True    ${result} == False

Close Deposit Fails If No Deposit
    Register Client    ${CLIENT_ID}    ${CLIENT_NAME}
    ${result}=    Close Deposit    ${CLIENT_ID}
    Should Be True    ${result} == False
