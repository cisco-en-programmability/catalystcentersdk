"""Cisco Catalyst Center GetSites data model.

Copyright (c) 2026 Cisco Systems.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import json

import fastjsonschema

from catalystcentersdk.exceptions import MalformedRequest


class JSONSchemaValidatorA36B1E624416553EB72D8F1C9461C938:
    """GetSites request schema definition."""

    def __init__(self):
        super().__init__()
        self._validator = fastjsonschema.compile(json.loads("""{
                    "$schema": "http://json-schema.org/draft-04/schema#",
                    "properties": {
                        "response": {
                            "items": {
                                "properties": {
                                    "country": {
                                        "enum": [
                                            "Afghanistan",
                                            "Albania",
                                            "Algeria",
                                            "American Samoa",
                                            "Andorra",
                                            "Angola",
                                            "Anguilla",
                                            "Antarctica",
                                            "Antigua and Barbuda",
                                            "Argentina",
                                            "Armenia",
                                            "Aruba",
                                            "Australia",
                                            "Austria",
                                            "Azerbaijan",
                                            "Bahamas",
                                            "Bahrain",
                                            "Bangladesh",
                                            "Barbados",
                                            "Belarus",
                                            "Belgium",
                                            "Belize",
                                            "Benin",
                                            "Bermuda",
                                            "Bhutan",
                                            "Bolivia",
                                            "Bosnia and Herzegovina",
                                            "Botswana",
                                            "Bouvet Island",
                                            "Brazil",
                                            "British Indian Ocean Territory",
                                            "Brunei",
                                            "Bulgaria",
                                            "Burkina Faso",
                                            "Burundi",
                                            "Cabo Verde",
                                            "Cambodia",
                                            "Cameroon",
                                            "Canada",
                                            "Cape Verde",
                                            "Cayman Islands",
                                            "Central African Republic",
                                            "Chad",
                                            "Chile",
                                            "China",
                                            "Christmas Island",
                                            "Cocos (Keeling) Islands",
                                            "Colombia",
                                            "Comoros",
                                            "Congo",
                                            "Congo Democratic Republic of the",
                                            "Cook Islands",
                                            "Costa Rica",
                                            "Ivory Coast",
                                            "Croatia",
                                            "Cuba",
                                            "Cyprus",
                                            "Czech Republic",
                                            "Czechia",
                                            "Denmark",
                                            "Djibouti",
                                            "Dominica",
                                            "Dominican Republic",
                                            "Ecuador",
                                            "Egypt",
                                            "El Salvador",
                                            "Equatorial Guinea",
                                            "Eritrea",
                                            "Estonia",
                                            "Ethiopia",
                                            "Falkland Islands (Malvinas)",
                                            "Faroe Islands",
                                            "Fiji",
                                            "Finland",
                                            "France",
                                            "French Guiana",
                                            "French Polynesia",
                                            "French Southern Territories",
                                            "Gabon",
                                            "Gambia",
                                            "Georgia",
                                            "Germany",
                                            "Ghana",
                                            "Gibraltar",
                                            "Greece",
                                            "Greenland",
                                            "Grenada",
                                            "Guadeloupe",
                                            "Guam",
                                            "Guatemala",
                                            "Guernsey",
                                            "Guinea",
                                            "Guinea-Bissau",
                                            "Guyana",
                                            "Haiti",
                                            "Heard Island and McDonald Islands",
                                            "Holy See (Vatican City State)",
                                            "Holy See",
                                            "Honduras",
                                            "Hong Kong",
                                            "Hungary",
                                            "Iceland",
                                            "India",
                                            "Indonesia",
                                            "Iran Islamic Republic of",
                                            "Iran (Islamic Republic of)",
                                            "Iraq",
                                            "Ireland",
                                            "Isle of Man",
                                            "Israel",
                                            "Italy",
                                            "Jamaica",
                                            "Japan",
                                            "Jersey",
                                            "Jordan",
                                            "Kazakhstan",
                                            "Kenya",
                                            "Kiribati",
                                            "Korea Democratic People's Republic of",
                                            "Korea (Democratic People's Republic of)",
                                            "Kosovo",
                                            "South Korea",
                                            "Kuwait",
                                            "Kyrgyzstan",
                                            "Lao People's Democratic Republic",
                                            "Latvia",
                                            "Lebanon",
                                            "Lesotho",
                                            "Liberia",
                                            "Libya",
                                            "Liechtenstein",
                                            "Lithuania",
                                            "Luxembourg",
                                            "Macao",
                                            "Macedonia",
                                            "Madagascar",
                                            "Malawi",
                                            "Malaysia",
                                            "Maldives",
                                            "Mali",
                                            "Malta",
                                            "Marshall Islands",
                                            "Martinique",
                                            "Mauritania",
                                            "Mauritius",
                                            "Mayotte",
                                            "Mexico",
                                            "Micronesia Federated States of",
                                            "Micronesia (Federated States of)",
                                            "Moldova",
                                            "Monaco",
                                            "Mongolia",
                                            "Montenegro",
                                            "Montserrat",
                                            "Morocco",
                                            "Mozambique",
                                            "Burma",
                                            "Myanmar",
                                            "Namibia",
                                            "Nauru",
                                            "Nepal",
                                            "Netherlands",
                                            "Netherlands Antilles",
                                            "New Caledonia",
                                            "New Zealand",
                                            "Nicaragua",
                                            "Niger",
                                            "Nigeria",
                                            "Niue",
                                            "Norfolk Island",
                                            "Northern Mariana Islands",
                                            "Norway",
                                            "Oman",
                                            "Pakistan",
                                            "Palau",
                                            "Palestinian Territory Occupied",
                                            "Palestine State of",
                                            "Panama",
                                            "Papua New Guinea",
                                            "Paraguay",
                                            "Peru",
                                            "Philippines",
                                            "Pitcairn",
                                            "Poland",
                                            "Portugal",
                                            "Puerto Rico",
                                            "Qatar",
                                            "R\u00e9union",
                                            "Romania",
                                            "Russia",
                                            "Rwanda",
                                            "Saint Helena Ascension and Tristan da Cunha",
                                            "Saint Kitts and Nevis",
                                            "Saint Lucia",
                                            "Saint Pierre and Miquelon",
                                            "St. Vincent and the Grenadines",
                                            "Samoa",
                                            "San Marino",
                                            "Sao Tome and Principe",
                                            "Saudi Arabia",
                                            "Senegal",
                                            "Serbia",
                                            "Seychelles",
                                            "Sierra Leone",
                                            "Singapore",
                                            "Slovakia",
                                            "Slovenia",
                                            "Solomon Islands",
                                            "Somalia",
                                            "South Africa",
                                            "South Georgia and the South Sandwich Islands",
                                            "Spain",
                                            "Sri Lanka",
                                            "South Sudan",
                                            "Sudan",
                                            "Suriname",
                                            "Svalbard and Jan Mayen",
                                            "Swaziland",
                                            "Sweden",
                                            "Switzerland",
                                            "Syrian Arab Republic",
                                            "Taiwan",
                                            "Tajikistan",
                                            "Tanzania United Republic of",
                                            "Thailand",
                                            "Timor-Leste",
                                            "Togo",
                                            "Tokelau",
                                            "Tonga",
                                            "Trinidad and Tobago",
                                            "Tunisia",
                                            "Turkey",
                                            "Turkmenistan",
                                            "Turks and Caicos Islands",
                                            "Tuvalu",
                                            "Uganda",
                                            "Ukraine",
                                            "United Arab Emirates",
                                            "United Kingdom",
                                            "United States",
                                            "United States Minor Outlying Islands",
                                            "Uruguay",
                                            "Uzbekistan",
                                            "Vanuatu",
                                            "Venezuela",
                                            "Venezuela (Bolivarian Republic of)",
                                            "Vietnam",
                                            "Virgin Islands British",
                                            "Virgin Islands U.S.",
                                            "Wallis and Futuna",
                                            "Western Sahara",
                                            "Yemen",
                                            "Zambia",
                                            "Zimbabwe"
                                        ],
                                        "type": "string"
                                    },
                                    "floorNumber": {
                                        "type": "integer"
                                    },
                                    "height": {
                                        "type": "number"
                                    },
                                    "id": {
                                        "type": "string"
                                    },
                                    "length": {
                                        "type": "number"
                                    },
                                    "name": {
                                        "minLength": 1,
                                        "type": "string"
                                    },
                                    "nameHierarchy": {
                                        "minLength": 8,
                                        "type": "string"
                                    },
                                    "parentId": {
                                        "type": "string"
                                    },
                                    "rfModel": {
                                        "enum": [
                                            "Free Space",
                                            "Outdoor Open Space",
                                            "Cubes And Walled Offices",
                                            "Indoor High Ceiling",
                                            "Drywall Office Only"
                                        ],
                                        "type": "string"
                                    },
                                    "siteHierarchyId": {
                                        "type": "string"
                                    },
                                    "type": {
                                        "enum": [
                                            "floor"
                                        ],
                                        "type": "string"
                                    },
                                    "unitsOfMeasure": {
                                        "allOf": [
                                            {
                                                "enum": [
                                                    "feet",
                                                    "meters"
                                                ],
                                                "type": "string"
                                            },
                                            {
                                                "default": "feet"
                                            }
                                        ]
                                    },
                                    "width": {
                                        "type": "number"
                                    }
                                },
                                "type": "object"
                            },
                            "type": "array"
                        },
                        "version": {
                            "type": "string"
                        }
                    },
                    "type": "object"
                }""".replace("\n" + " " * 16, "")))

    def validate(self, request):
        try:
            self._validator(request)
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest(
                "{} is invalid. Reason: {}".format(request, e.message)
            )
