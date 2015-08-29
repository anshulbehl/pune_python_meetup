# pune_python_meetup

- Using robot framework to create your own test libraries

We are testing the our web application under webapp directory.

webapp__robot directory contains the library code needed to test the software

Tests script is listed under the webapp_tests directory.

- How to run the tests

    ✗ pybot webapp_tests
    ==============================================================================
    Webapp Tests                                                                  
    ==============================================================================
    Webapp Tests.Test                                                             
    ==============================================================================
    Create User                                                           | PASS |
    ------------------------------------------------------------------------------
    Create Token                                                          | PASS |
    ------------------------------------------------------------------------------
    Create User and access resource from token                            | PASS |
    ------------------------------------------------------------------------------
    Access Resource directly without creating token                       | FAIL |
    ValueError: No JSON object could be decoded

    Also teardown failed:
    ValueError: No JSON object could be decoded
    ------------------------------------------------------------------------------
    Access Resource directly from username                                | FAIL |
    ValueError: No JSON object could be decoded

    Also teardown failed:
    ValueError: No JSON object could be decoded
    ------------------------------------------------------------------------------
    Create User and Access resource from Username                         | PASS |
    ------------------------------------------------------------------------------
    Delete Users after creation                                           | PASS |
    ------------------------------------------------------------------------------
    Webapp Tests.Test                                                     | FAIL |
    7 critical tests, 5 passed, 2 failed
    7 tests total, 5 passed, 2 failed
    ==============================================================================
    Webapp Tests                                                          | FAIL |
    7 critical tests, 5 passed, 2 failed
    7 tests total, 5 passed, 2 failed
    ==============================================================================
    Output:  /home/abehl/pune_meetup/pune_python_meetup/output.xml
    Log:     /home/abehl/pune_meetup/pune_python_meetup/log.html
    Report:  /home/abehl/pune_meetup/pune_python_meetup/report.html

