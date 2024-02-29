class Customer:
    def __init__(self, data):
        self.party = self.Party(data["party"])
        self.type = self.Type(data["type"])

    def __dict__(self):
        return {
            "party": self.party.__dict__(),
            "type": self.type.__str__()
        }

    class Party:
        def __init__(self, party_data):
            self.biometric_data = party_data["biometricData"]
            self.birth_date = party_data["birthDate"]
            self.birth_place = party_data["birthPlace"]
            self.gender = self.Gender(party_data["gender"]["genderId"])
            self.identification_document = self.IdentificationDocument(party_data["identificationDocument"])
            self.INILA = party_data["INILA"]
            self.is_resident = party_data["isResident"]
            self.name_info = self.NameInfo(party_data["nameInfo"])
            self.nationality = self.Nationality(party_data["nationality"]["nationalityId"])
            self.public_official = party_data["publicOfficial"]
            self.speaking_language = self.SpeakingLanguage(party_data["speakingLanguage"]["languageId"])
            self.tax_registration_certificate = self.TaxRegistrationCertificate(
                party_data["taxRegistrationCertificate"]["taxIdentificationNumber"])

        def __dict__(self):
            return {
                "biometricData": self.biometric_data,
                "birthDate": self.birth_date,
                "birthPlace": self.birth_place,
                "gender": self.gender.__dict__(),
                "identificationDocument": self.identification_document.__dict__(),
                "INILA": self.INILA,
                "isResident": self.is_resident,
                "nameInfo": self.name_info.__dict__(),
                "nationality": self.nationality.__dict__(),
                "publicOfficial": self.public_official,
                "speakingLanguage": self.speaking_language.__dict__(),
                "taxRegistrationCertificate": self.tax_registration_certificate.__dict__()
            }

        class Gender:
            def __init__(self, gender_id):
                self.gender_id = gender_id

            def __dict__(self):
                return {"genderId": self.gender_id}

        class IdentificationDocument:
            def __init__(self, document_data):
                self.date_of_issue = document_data["dateOfIssue"]
                self.division_code = document_data["divisionCode"]
                self.number = document_data["number"]
                self.provided_by_organization = document_data["providedByOrganization"]
                self.series = document_data["series"]
                self.type = self.IdentificationType(document_data["type"]["identificationTypeId"])
                self.valid_for = document_data["validFor"]

            def __dict__(self):
                return {
                    "dateOfIssue": self.date_of_issue,
                    "divisionCode": self.division_code,
                    "number": self.number,
                    "providedByOrganization": self.provided_by_organization,
                    "series": self.series,
                    "type": self.type.__dict__(),
                    "validFor": self.valid_for
                }

            class IdentificationType:
                def __init__(self, identification_type_id):
                    self.identification_type_id = identification_type_id

                def __dict__(self):
                    return {"identificationTypeId": self.identification_type_id}

        class NameInfo:
            def __init__(self, name_info_data):
                self.first_name = name_info_data["firstName"]
                self.patronymic = name_info_data["patronymic"]
                self.surname = name_info_data["surname"]

            def __dict__(self):
                return {
                    "firstName": self.first_name,
                    "patronymic": self.patronymic,
                    "surname": self.surname
                }

        class Nationality:
            def __init__(self, nationality_id):
                self.nationality_id = nationality_id

            def __dict__(self):
                return {"nationalityId": self.nationality_id}

        class SpeakingLanguage:
            def __init__(self, language_id):
                self.language_id = language_id

            def __dict__(self):
                return {"languageId": self.language_id}

        class TaxRegistrationCertificate:
            def __init__(self, tax_identification_number):
                self.tax_identification_number = tax_identification_number

            def __dict__(self):
                return {"taxIdentificationNumber": self.tax_identification_number}

    class Type:
        def __init__(self, type_data):
            self.type_data = type_data

        def __str__(self):
            return self.type_data
