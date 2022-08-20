"""This adds dummy voters only once"""
from voter import Voter
import random

voter = Voter("Droid-fi")

def add_voter():
    poling_stations = [
        'SK1A', 'SK2A', 'SK3A', 'SN1A', 'SN2A','SN3A',#Kituo-North
        'SS1A','SS2A', 'SS3A', 'SS1B', 'SS2B','SS3B',#Kituo-South
        'N1A', 'N2A','N3A', 'NN1A', 'NN2A', 'NN3A',#Naiobi-North
        'N1B', 'N2B','N3B', 'NS1B', 'NS2B', 'NS3B',#Naiobi-South
        'MU1A', 'MU2A', 'MU3A','MUN1A', 'MUN2A', 'MUN3A',#Kiamu-North
        'MU1B', 'MU2B', 'MU3B', 'MUS1B', 'MUS2B', 'MUS3B'#Kiamu-South
    ]

    first_name = ""
    middle_name = ""
    last_name = ""
    id_number = ""
    county = ""
    constituency = ""
    ward = ""
    country = "Keinya"

    _gender = ['Male', 'Female']

    gender = random.choice(_gender)

    count = 1

    for station in poling_stations:
        if station == 'SK1A' or station == 'SK2A' or station == 'SK3A':
            county = "Kituo"
            constituency = "Kituo-North"
            ward = "KNA"
            for i in range(1,1500,1):
                first_name = f"F{station}{i}"
                middle_name = f"M{station}{i}"
                last_name = f"L{station}{i}"
                id_number = f"id{count}"
                voter.insert_voter(first_name, middle_name, last_name,
                 id_number, gender,county, country,constituency, ward,station)
                count += 1

        elif station == 'SN1A' or station == 'SN2A' or station == 'SN3A':
            county = "Kituo"
            constituency = "Kituo-North"
            ward = "KNB"
            for i in range(1,1500,1):
                first_name = f"F{station}{i}"
                middle_name = f"M{station}{i}"
                last_name = f"L{station}{i}"
                id_number = f"id{count}"
                voter.insert_voter(first_name, middle_name, last_name,
                 id_number, gender,county, country,constituency, ward,station)
                count += 1
            
        elif station == 'SS1A' or station == 'SS2A' or station == 'SS3A':
            county = "Kituo"
            constituency = "Kituo-South"
            ward = "KSA"
            for i in range(1,1500,1):
                first_name = f"F{station}{i}"
                middle_name = f"M{station}{i}"
                last_name = f"L{station}{i}"
                id_number = f"id{count}"
                voter.insert_voter(first_name, middle_name, last_name,
                 id_number, gender,county, country,constituency, ward,station)
                count += 1
        
        elif station == 'SS1B' or station == 'SS2B' or station == 'SS3B':
            county = "Kituo"
            constituency = "Kituo-South"
            ward = "KSB"
            for i in range(1,1500,1):
                first_name = f"F{station}{i}"
                middle_name = f"M{station}{i}"
                last_name = f"L{station}{i}"
                id_number = f"id{count}"
                voter.insert_voter(first_name, middle_name, last_name,
                 id_number, gender,county, country,constituency, ward,station)
                count += 1

        elif station == 'N1A' or station == 'N2A' or station == 'N3A':
            county = "Naiobi"
            constituency = "Naiobi-North"
            ward = "NNA"
            for i in range(1,1500,1):
                first_name = f"F{station}{i}"
                middle_name = f"M{station}{i}"
                last_name = f"L{station}{i}"
                id_number = f"id{count}"
                voter.insert_voter(first_name, middle_name, last_name,
                 id_number, gender,county, country,constituency, ward,station)
                count += 1

        elif station == 'NN1A' or station == 'NN2A' or station == 'NN3A':
            county = "Naiobi"
            constituency = "Naiobi-North"
            ward = "NNB"
            for i in range(1,1500,1):
                first_name = f"F{station}{i}"
                middle_name = f"M{station}{i}"
                last_name = f"L{station}{i}"
                id_number = f"id{count}"
                voter.insert_voter(first_name, middle_name, last_name,
                 id_number, gender,county, country,constituency, ward,station)
                count += 1

        elif station == 'N1B' or station == 'N2B' or station == 'N3B':
            county = "Naiobi"
            constituency = "Naiobi-South"
            ward = "NSA"
            for i in range(1,1500,1):
                first_name = f"F{station}{i}"
                middle_name = f"M{station}{i}"
                last_name = f"L{station}{i}"
                id_number = f"id{count}"
                voter.insert_voter(first_name, middle_name, last_name,
                 id_number, gender,county, country,constituency, ward,station)
                count += 1

        elif station == 'NS1B' or station == 'NS2B' or station == 'NS3B':
            county = "Naiobi"
            constituency = "Naiobi-South"
            ward = "NSB"
            for i in range(1,1500,1):
                first_name = f"F{station}{i}"
                middle_name = f"M{station}{i}"
                last_name = f"L{station}{i}"
                id_number = f"id{count}"
                voter.insert_voter(first_name, middle_name, last_name,
                 id_number, gender,county, country,constituency, ward,station)
                count += 1

        elif station == 'MU1A' or station == 'MU2A' or station == 'MU3A':
            county = "Kiamu"
            constituency = "Kaimu-North"
            ward = "KNAK"
            for i in range(1,1500,1):
                first_name = f"F{station}{i}"
                middle_name = f"M{station}{i}"
                last_name = f"L{station}{i}"
                id_number = f"id{count}"
                voter.insert_voter(first_name, middle_name, last_name,
                 id_number, gender,county, country,constituency, ward,station)
                count += 1
        
        elif station == 'MUN1A' or station == 'MUN2A' or station == 'MUN3A':
            county = "Kiamu"
            constituency = "Kaimu-North"
            ward = "KNBK"
            for i in range(1,1500,1):
                first_name = f"F{station}{i}"
                middle_name = f"M{station}{i}"
                last_name = f"L{station}{i}"
                id_number = f"id{count}"
                voter.insert_voter(first_name, middle_name, last_name,
                 id_number, gender,county, country,constituency, ward,station)
                count += 1
        
        elif station == 'MU1B' or station == 'MU2B' or station == 'MU3B':
            county = "Kiamu"
            constituency = "Kaimu-South"
            ward = "KSAK"
            for i in range(1,1500,1):
                first_name = f"F{station}{i}"
                middle_name = f"M{station}{i}"
                last_name = f"L{station}{i}"
                id_number = f"id{count}"
                voter.insert_voter(first_name, middle_name, last_name,
                 id_number, gender,county, country,constituency, ward,station)
                count += 1

        elif station == 'MUS1B' or station == 'MUS2B' or station == 'MUS3B':
            county = "Kiamu"
            constituency = "Kaimu-South"
            ward = "KSBK"
            for i in range(1,1500,1):
                first_name = f"F{station}{i}"
                middle_name = f"M{station}{i}"
                last_name = f"L{station}{i}"
                id_number = f"id{count}"
                voter.insert_voter(first_name, middle_name, last_name,
                 id_number, gender,county, country,constituency, ward,station)
                count += 1

add_voter()