*** Settings ***
Documentation    Suite description
Library  roomTwo.py

*** Variables ***
${response} =  UE-1 already attached.

*** Test Cases ***
Do attach
    Do_attach
Do detach
   Do_detach
Start traffic
    Start_traf
Stop traffic
    Stop_traf
Compare_response

    ${stringToCompare}  RESPONSE_COMPARATOR  ${}
    Should Be Equal  ${stringToCompare}  ${response}

*** Keywords ***
Do_attach
    attach   1    1
Do_detach
    detach   1
Start_traf
    start_traffic  1  100  1
Stop_traf
    stop_traffic  1  1


