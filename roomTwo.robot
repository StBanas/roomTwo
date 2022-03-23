*** Settings ***
Documentation    Suite description
Library  roomTwo.py

*** Variables ***
${positive_response} =  UE-1 on cell=1 attached successful.
${negative_response} =  Cell-4 is not supported by the eNB.

*** Test Cases ***
Do attach
    Do_attach
Do detach
   Do_detach
Start traffic
    Start_traf
Stop traffic
    Stop_traf
Compare_positive_response
    ${stringToCompare}  POSITIVE_RESPONSE_COMPARATOR
    Should Be Equal As Strings  ${stringToCompare}  ${positive_response}
Compare_negative_response
    ${stringToCompare}  NEGATIVE_RESPONSE_COMPARATOR
    Should Not Be Equal As Strings  ${stringToCompare}  ${negative_response}

*** Keywords ***
Do_attach
    attach   1    1
Do_detach
    detach   1
Start_traf
    start_traffic  1  100  1
Stop_traf
    stop_traffic  1  1


