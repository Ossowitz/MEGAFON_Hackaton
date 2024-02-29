*** Settings ***
Library    RequestsLibrary

*** Variables ***
${base_url}    http://dbss-sso.external.rm-dhekoli.cloud.billing.ru:47226/openapi/v1/customerManagement/customers
${auth}    ('Admin', '1111')
${headers}    Content-Type=application/json
${request_body}    ${EMPTY}
...    {
...        "party": {
...            "biometricData": true,
...            "birthDate": "1977-01-08",
...            "birthPlace": "г. Санкт-Петербург",
...            "gender": {
...                "genderId": 1
...            },
...            "identificationDocument": {
...                "dateOfIssue": "2001-12-12",
...                "divisionCode": "946-777",
...                "number": "122262247300339",
...                "providedByOrganization": "15 Отделение по оформлению внутренних паспортов и регистрации граждан РФ - Красносельский район",
...                "series": "1812",
...                "type": {
...                    "identificationTypeId": 5
...                },
...                "validFor": "2047-02-01"
...            },
...            "INILA": "85513361297",
...            "isResident": true,
...            "nameInfo": {
...                "firstName": "Пётр",
...                "patronymic": "Леонидович",
...                "surname": "Колобанов"
...            },
...            "nationality": {
...                "nationalityId": 1
...            },
...            "publicOfficial": false,
...            "speakingLanguage": {
...                "languageId": 3
...            },
...            "taxRegistrationCertificate": {
...                "taxIdentificationNumber": "705332995790"
...            }
...        },
...        "type": "INDIVIDUAL"
...    }

*** Test Cases ***
Check Post Request Status Code
    Create Session    my_session    ${base_url}
    ${response}=    Post Request    my_session    ${base_url}    data=${request_body}    headers=${headers}    auth=${auth}
    Should Be True    200 <= ${response.status_code} < 300