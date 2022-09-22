#!/usr/local/bin/python3
import csv
import logging
import os
import re
from typing import List, Optional, Tuple, Dict

import requests
from bs4 import BeautifulSoup


def parse_prime_mover_type(prime_mover: str) -> Optional[str]:
    map_dict = {
        "Diesel Elétrica": "DIESEL_ELECTRIC",
        "Diesel-Elétrica": "DIESEL_ELECTRIC",
        "Elétrica": "ELECTRIC",
        "Diesel-Eletrica": "DIESEL_ELECTRIC",
        "Diesel-elétrica": "DIESEL_ELECTRIC",
        "Diesel-elétrico": "DIESEL_ELECTRIC"
    }

    if prime_mover not in map_dict:
        logging.warning("Unknown prime mover type: {}".format(prime_mover))
        return None

    return map_dict[prime_mover]


def parse_manufacturer(manufacturer: str) -> Optional[str]:
    manufacturer = manufacturer.upper()
    map_dict = {
        " GENERAL ELECTRIC - ERIE": 'GE',
        "[GEVISA]] ( BRASIL)": 'GE',
        "ALCO": 'ALCO',
        "ALCO-GE ( ESTADOS UNIDOS)": 'ALCO',
        "AMERICAN LOCOMOTIVE COMPANY ( ESTADOS UNIDOS)": 'ALCO',
        "AMERICAN LOCOMOTIVE COMPANY( ESTADOS UNIDOS)MONTREAL LOCOMOTIVE WORKS ( CANADÁ), SUBSIDIÁRIA DA (ALCO)": 'ALCO',
        "BALDWIN LOCOMOTIVE WORKS": 'Baldwin-Whitcomb',
        "BALDWIN-WESTINGHOUSE( ESTADOS UNIDOS)": 'Baldwin-Westinghouse',
        "BALDWIN-WHITCOMB ": 'Baldwin-Whitcomb',
        "BOMBARDIER": 'Bombardier',
        "CATERPILLAR": 'Caterpillar',
        "COOPER BESSEMER": 'Cooper-Bessemer',
        "COOPER-BRESSEMER": 'Cooper-Bessemer',
        "COPPER-BRESSEMER": 'Cooper-Bessemer',
        "CUMMINS – U.S.A. (ORIGINAL)  FNM": 'Cummins',
        "CUMMINS": 'Cummins',
        "ELECTRO-MOTIVE DIESEL (EMD)": 'EMD',
        "EMAQ ( BRASIL)CAF( ESPANHA)": 'EMAC',
        "EMD ( ÁFRICA DO SUL)": 'EMD',
        "EMD (USA )": 'EMD',
        "EMD ( ESTADOS UNIDOS)": 'EMD',
        "EMD - LA GRANGE ( ESTADOS UNIDOS)": 'EMD',
        "EMD - LA GRANGE ILLINOIS ( ESTADOS UNIDOS)": 'EMD',
        "EMD - LA GRANGE, ILLINOIS ( ESTADOS UNIDOS)GMDD - LONDON, ONTÁRIO ( CANADÁ)": 'EMD',
        "EMD": 'EMD',
        "EMD(USA)  MACOSA (ESPANHA)  VILLARES (BRASIL)": 'Villares',
        "ENGLISH ELECTRIC CO. E VULCAN FOUNDRY LTD.  REINO UNIDO": 'English-Electric',
        "ENGLISH ELECTRIC E ROBERT STEPHENSON AND HAWTHORNS LTD( REINO UNIDO)": 'English-Electric',
        "ENGLISH ELECTRIC": 'English-Electric',
        "ENGLISH ELETRIC CO. E VULCAN FOUNDRY LTD.  REINO UNIDO": 'English-Electric',
        "ENGLISH ELETRIC": 'English-Electric',
        "GE ": 'GE',
        "GE ( BRASIL)": 'GE',
        "GE ( ESTADOS UNIDOS) GE DO BRASIL ( BRASIL)": 'GE',
        "GE ( ESTADOS UNIDOS)": 'GE',
        "GE ( ESTADOS UNIDOS)GE DO BRASIL ( BRASIL)": 'GE',
        "GE ( ESTADOS UNIDOS)GE DO BRASIL ( BRASIL)DORBYL TRANSPORT PRODUCTS ( ÁFRICA DO SUL)BABCOCK & WILCOX ( ESPANHA)": 'GE',
        "GE ( ESTADOS UNIDOS)GE DO BRASIL ( BRASIL)DORMAN LONG ( ÁFRICA DO SUL)": 'GE',
        "GE ( ESTADOS UNIDOS)GE DO BRASIL": 'GE',
        "GE BRASIL - CAMPINAS ( BRASIL)  GE - ERIE ( ESTADOS UNIDOS)": 'GE',
        "GE BRASIL - CAMPINAS ( BRASIL)": 'GE',
        "GE BRASIL": 'GE',
        "GE DO BRASIL ( BRASIL) GONINAN ( AUSTRÁLIA)": 'GE',
        "GE DO BRASIL ( BRASIL)": 'GE',
        "GE ERIE ( ESTADOS UNIDOS)": 'GE',
        "GE TRANSPORTATION": 'GE',
        "GE TRANSPORTATION- ERIE ( ESTADOS UNIDOS)": 'GE',
        "GE TRANSPORTATION ESTADOS UNIDOS BRASIL": 'GE',
        "GE": 'GE',
        "GE-ALCO ( ESTADOS UNIDOS)": 'GE',
        "GE-COOPER BESSEMER": 'Cooper-Bessemer',
        "GE-SCHENECTADY-NY( ESTADOS UNIDOS)[1]GE DO BRASIL( BRASIL)[2]": 'GE',
        "GENERAL ELECTRIC - ERIE ( ESTADOS UNIDOS) WESTINGHOUSE": 'GE',
        "GENERAL ELECTRIC DO BRASIL S/A": 'GE',
        "GENERAL ELECTRIC E WESTINGHOUSE": 'GE',
        "GENERAL ELECTRIC — SCHENECTADY, NY ( ESTADOS UNIDOS)": 'GE',
        "GENERAL ELECTRIC": 'GE',
        "GET ERIE, PA.(USA) GEVISA CAMPINAS-SP": 'GE',
        "GET ERIE, PA.(USA)": 'GE',
        "GEVISA ( BRASIL)": 'GE',
        "GM (USA)": 'EMD',
        "GM-EMD": 'EMD',
        "GM-EMD/GM-GMDD": 'EMD',
        "GMDL (CANADÁ )": 'EMD',
        "GMDL ONTÁRIO, CANADÁ": 'EMD',
        "LEW ( ALEMANHA ORIENTAL)": 'LEW',
        "MACOSA- LICENSA GENERAL MOTORS": 'MACOSA',
        "MACOSA- LICENÇA GENERAL MOTORS": 'MACOSA',
        "SACM": 'SACM',
        "SLM-WINTERTHUR-BROWN, BOVERI & CIE (SUÍÇA)": 'Winterthur',
        "VILLARES ( BRASIL), SOB LICENÇAEMD ( ESTADOS UNIDOS)": 'Villares',
    }

    if manufacturer not in map_dict:
        logging.warning("Unknown manufacturer: {}".format(manufacturer))
        return None

    return map_dict[manufacturer]


def parse_first_year_occurrence(info: str) -> Optional[int]:
    years = re.findall(r"\d{4}", info)
    return None if len(years) == 0 else int(years[0])


def parse_percentage(info: str) -> Optional[float]:
    if '%' not in info:
        return None

    percentage = float(re.sub(r"[^\d.]", '', info.replace(",", ".")))
    return percentage/100


def parse_multiple_units(info: str) -> Optional[bool]:
    map_dict = {
        "Sim": True,
        "Sim, Até 3 Unidades": True,
        "Sim (dupla)": True,
        "Apenas na Traseira": True,
        "Sim.": True,
        "sim": True,
        "Até três unidades": True,
        "Sim, até três unidades": True,
        "Sim, mas removida pela Fepasa": True,
        "Não": False,
        "ate 5 unidades": True,
        "até 4 unidades": True,
    }

    if info not in map_dict:
        logging.warning("Unknown multiple units boolean: {}".format(info))
        return None

    return map_dict[info]


def parse_brake_system(info: str) -> Optional[str]:
    map_dict = {
        "24 RL": "24RL",
        "6SL WABCO": "6SL",
        "6SL": "6SL",
        "6SL, 26L": "6SL/26L",
        "26L": "26L",
        "26L  MP: 28-LAV-1": "26L/28-LAV-1",
        "6SL,": "6SL",
        "26LA": "26LA",
        "Ar comprimido 14EL": "14EL",
        "AS-2": "AS-2",
        "F-4 (ferro fundido)": "F-4",
        "6-SL-AV-1": "6-SL-AV-1",
        "28L-AV-1": "28L-AV-1",
        "26L Wabco": "26L",
    }

    if info not in map_dict:
        logging.warning("Unknown brake system: {}".format(info))
        return None

    return map_dict[info]


def parse_cylinders_size(info: str) -> Optional[str]:
    map_dict = {
        "9\"": "230,2 mm (9 1/16 in) x 266,7 mm (10 1/2 in)",
        "9\" x 10 1/2\"": "230,2 mm (9 1/16 in) x 266,7 mm (10 1/2 in)",
        "323,85 mm (12.75\") x 393,70 mm (15.5\")": "323,85 mm (12 3/4 in) x 393,70 mm (15 1/2 in)",
        "10”(254mm) x 12”(305mm)": "254,0 mm (10 in) x 304,8 mm (12 in)",
        "8½”(216mm)x10”(254mm)": "215,9 mm (8 1/2 in) x 254,0mm (10 in)",
        "9 1/16” (230mm)x10”(254mm)": "230,2 mm (9 1/16 in) x 254,0 mm (10 in)",
        "8 1/2\" (216mm)x10\"(254mm)": "215,9 mm (8 1/2 in) x 254,0 mm (10 in)",
        "9 1/16\" (230mm)x10\"(254mm)": "230,2 mm (9 1/16 in) x 254,0 mm (10 in)",
        "9 1/16”(230mm)x10”(254mm)": "230,2 mm (9 1/16 in) x 254,0 mm (10 in)",
        "9 1/16Pol": "230,2 mm (9 1/16 in) x 254,0 mm (10 in)",
        "125mmx150mm": "125,0 mm x 150,0 mm",
        "228,6 mm x 266,7 mm": "228,6 mm x 266,7 mm",
        "9” x 10½”": "230,2 mm (9 1/16 in) x 266,7 mm (10 1/2 in)",
        "6¼”x8”": "158,8 mm (6 1/4 in) x 203,2 mm (8 in)",
        "6\"1/4 x 8\"": "158,8 mm (6 1/4 in) x 203,2 mm (8 in)",
        "175 mm": "175 mm x 180 mm",
    }

    if info not in map_dict:
        logging.warning("Unknown cylinders size: {}".format(info))
        return None

    return map_dict[info]


def parse_fuel_capacity(info: str) -> Optional[str]:
    info = info.replace(",", ".").lower()

    if re.match(r"^[\d.]{2,10}\s*l?$", info):
        return "{} L".format(int(re.sub(r"[^\d]", "", info)))

    map_dict = {
        "500 litros/ 2000 litros (905-Abpf Campinas)": "500 L / 2000 L",
        "AS616: 4.914 l AS616E: 7.201l": "4914 L / 7201 L",
        "12.000 – 15.000 litros": "12000 L - 15000 L",
        "Bitola 1000mm B-B:2.840lA1A: l Bitola 1.600mm: 3.200 l": "2840 L / 3200 L",
        "6.070l  MP: 6.600l": "6070 L / 6600 L",
        "Bitola 1000mm B-B:2.840lA1A: l": "2840 L",
        "901 a 904 7360l  905 a 934 9462l  935 a 940 10.870l": "7360 L / 9462 L / 10870 L",
        "3.200 Galões": "14547 L",
        "13,900 litros": "13900 L",
        "13.900 a 15.000 litros": "13900 L - 15000 L",
        "14.400 litros": "14400 L",
    }

    if info not in map_dict:
        logging.warning("Unknown fuel capacity: {}".format(info))
        return None

    return map_dict[info]


def parse_generator(info: str) -> Optional[str]:
    map_dict = {
        "GE 564 C1": "GE 564 C1",
        "GT 5 B 1 A 1": "GE GT-581",
        "Westinghouse 471 BZ": "Westinghouse 471 BZ",
        "D15-E": "D15-E",
        "AR-10B3": "AR-10B3",
        "Bitola 1.000mm: D12F  Bitola 1.600mm: D12F e D32F": "D12F / D32F",
        "D32T": "D32T",
        "D12F": "D12F",
        "D25-E": "D25-E",
        "AR-10-F": "AR-10-F",
        "D22": "D22",
        "D32": "D32",
        "G.E.:5 GMG 136B1 Westinghouse: YX32A": "GE 5GMG-136B1 / YX32A",
        "GE 5GT 558": "GE 5GT-558",
        "GT – 1.503 - X 1": "GT-1503-X1",
        "2x GMG136": "2x GMG136",
        "5GMG - 197": "5GMG-197",
        "5GT-581-C3": "5GT-581-C3",
        "GT596 C.C.": "GT596 CC",
        "5GMG – 146E1": "GE 5GMG-146E1",
        "GT601": "GT601",
        "5GT-601-A1": "5GT-601-A1",
        "5GT 601": "5GT-601",
        "GBG 0609-150A": "GBG 0609-150A",
        "GBG 0909-150A": "GBG 0909-150A",
    }

    if info not in map_dict:
        logging.warning("Unknown generator: {}".format(info))
        return None

    return map_dict[info]


def parse_truck_type(info: str) -> Optional[str]:
    map_dict = {
        "A1A-A1A": "A1A-A1A",
        "B-B": "B-B",
        "C-C": "C-C",
    }

    if info not in map_dict:
        logging.warning("Unknown truck type: {}".format(info))
        return None

    return map_dict[info]


def parse_wheel_arrangement_aar(info: str) -> Optional[str]:
    map_dict = {
        "B-B": "B-B",
        "A1A-A1A": "A1A-A1A",
        "C-C": "C-C",
        "1-B+B-1": "1-B+B-1",
        "C+C": "C+C",
        "1-B-B-1": "1-B-B-1",
        "B+B-B+B": "B+B-B+B",
        "D-D": "D-D",
        "Brasil: B-B; A1A-A1A Austrália: C-C": "B-B / A1A-A1A",
        "B-B; A1A-A1A": "B-B / A1A-A1A",
        "1-C+C-1": "1-C+C-1",
        "2-B+B-2": "2-B+B-2",
        "2-C+C-2": "2-C+C-2",
        "2-D+D-2": "2-D+D-2",
        "B": "B",
        "B-B (1,6m) ou C-C (1,0m)": "B-B / C-C",
        "B+B": "B+B",
        "C-C/B-B+B-B": "C-C/B-B+B-B",
        "B-B+B-B": "B-B+B-B",
        "C-CA1A-A1A1-C-C-1": "C-C",
        "B-B (Brasil) ou C-C (Chile)": "B-B",
        "1-D-1": "1-D-1",
    }

    if info not in map_dict:
        logging.warning("Unknown AAR arrangement: {}".format(info))
        return None

    return map_dict[info]


def parse_wheel_arrangement_whyte(info: str) -> Optional[str]:
    map_dict = {
    }

    if info not in map_dict:
        logging.warning("Unknown Whyte arrangement: {}".format(info))
        return None

    return map_dict[info]


def parse_meters(info: str) -> Optional[int]:
    info = info.lower()
    if re.match(r"^[\d]*[,]?[\d]*\s?m(etros)?$", info):
        return round(float(re.sub(r"[^\d,]", "", info).replace(",", ".")) * 1000)

    map_dict = {}

    if info not in map_dict:
        logging.warning("Unknown meters dimension: {}".format(info))
        return None

    return map_dict[info]


def parse_horsepower(info: str) -> Optional[int]:
    info = info.lower()
    if re.match(r"^[\d]*[.,]?[\d]*\s?hp$", info):
        return int(re.sub(r"[^\d]", "", info))

    map_dict = {
        "1.450 hp (1,09mw)": 1450,
        "2.250 hp (1,69mw)": 2250,
        "1.800hp (1,5mw)": 1800,
        "2.000hp (1.545kw)": 2000,
    }

    if info not in map_dict:
        logging.warning("Unknown horsepower value: {}".format(info))
        return None

    return map_dict[info]


def parse_motor_capacity(info: str) -> Optional[str]:
    info = info.lower()
    if re.match(r"^[\d]*[.]?[\d]*\s?cc³\s?x\s?[\d]+$", info):
        return info

    map_dict = {
        "9.287cc³ x 12 = 111.444Cm^3": '9.287cc³ x 12',
    }

    if info not in map_dict:
        logging.warning("Unknown motor capacity value: {}".format(info))
        return None

    return map_dict[info]


def parse_rpm(info: str) -> Optional[int]:
    info = info.lower()
    if re.match(r"^[\d]+\s*RPM$", info):
        return int(re.sub(r"[^\d]", "", info))

    map_dict = {}

    if info not in map_dict:
        logging.warning("Unknown RPM value: {}".format(info))
        return None

    return map_dict[info]


def parse_cubic_meters(info: str) -> Optional[float]:
    info = info.lower()
    if re.match(r"^[\d]*[,]?[\d]*\s?m³$", info):
        return float(re.sub(r"[^\d.]", "", info.replace(",", ".")))

    map_dict = {
        "950 litros": 0.95,
        "334 l": 0.334,
    }

    if info not in map_dict:
        logging.warning("Unknown cubic meters value: {}".format(info))
        return None

    return map_dict[info]


def parse_float_with_unit(info: str, unit: str, skip_warning=False) -> Optional[float]:
    unit = unit.lower()
    sanitized_info = info.lower().replace(unit, "")
    if re.match(r"^[\d]*[,]?\d+\s*$", sanitized_info):
        return float(re.sub(r"[^\d.]", "", sanitized_info.replace(",", ".")))

    if re.match(r"^[\d]*[.]?[\d]*\s*$", sanitized_info):
        return float(re.sub(r"[^\d.]", "", sanitized_info))

    map_dict = {

    }

    if info not in map_dict and not skip_warning:
        logging.warning("Unable to parse float value '{}' with unit '{}'".format(info, unit))

    return map_dict[info] if info in map_dict else None


def parse_int_with_unit(info: str, unit: str, skip_warning=False) -> Optional[int]:
    number = parse_float_with_unit(info, unit, True)

    if number is None and not skip_warning:
        logging.warning("Unable to parse integer value '{}' with unit '{}'".format(info, unit))

    return int(number) if number is not None else None


def parse_weight(info: str) -> Optional[float]:
    kg_value = parse_float_with_unit(info, "kg", True)
    tons_value = parse_float_with_unit(info, "t", True)
    if kg_value is None and tons_value is None:
        logging.warning("Unable to parse weight value '{}'".format(info))

    return tons_value*1000 if tons_value is not None else kg_value


def parse_liters(info: str) -> Optional[int]:
    l_value = parse_int_with_unit(info, "l", True)
    litros_value = parse_int_with_unit(info, "litros", True)
    if litros_value is None and l_value is None:
        logging.warning("Unable to liters value '{}'".format(info))

    return litros_value if litros_value is not None else l_value


def parse_millimeters(info: str, skip_warning=False) -> Optional[float]:
    mm_value = parse_int_with_unit(info, "mm", True)
    if mm_value is not None:
        return float(mm_value)

    m_value = parse_float_with_unit(info, "m", True)
    if m_value is not None:
        return m_value * 1000.0

    metros_value = parse_float_with_unit(info, "metros", True)
    if metros_value is not None:
        return metros_value * 1000.0

    if not skip_warning:
        logging.warning("Unable to parse millimeters value '{}'".format(info))

    return None


def parse_wheel_diameter(info: str) -> Optional[float]:
    mm_value = parse_millimeters(info, True)
    if mm_value is not None:
        return mm_value

    map_dict = {
        "40\"": 1016.0,
        "AS616: 1.067 mm (40\") AS616E: 9.144 mm (36\")": 1067.0,
        "940 mm (37”)": 940.0,
        "40”": 1016.0,
        "B-B: 40\"  A1A: Externos:40\" Centrais:36\"": 1016.0,
        "1.118mm (44\")": 1118.0,
        "91,44 cm (36’’)": 914.4,
        "838,2 mm (33”)[3]": 838.2,
        "46”": 1168.4,
        "36”": 914.4,
        "36\"": 914.4,
    }

    if info not in map_dict:
        logging.warning("Unknown wheel diameter: {}".format(info))
        return None

    return map_dict[info]


def parse_gauge(info: str) -> Optional[float]:
    map_dict = {
        "1600 (mm)": "Larga",
        "1,600 m (Brasil)": "Larga",
        "1,600 m": "Larga",
        "1,000 m (Brasil)": "Métrica",
        "1,000 m": "Métrica",
        "1000 mm": "Métrica",
        "1.000 mm": "Métrica",
        "1600 mm": "Métrica",
        "1,600 m \"Bitola Larga\"": "Larga",
        "1.600 mm": "Larga",
        "1,00m": "Métrica",
        "1000 mm (Brasil) a 1676 mm (Argentina)": "Métrica",
        "1.600mm": "Larga",
    }

    if info not in map_dict:
        logging.warning("Unknown gauge: {}".format(info))
        return None

    return map_dict[info]


def parse_values(response_dict: Dict) -> Dict:

    if 'prime_mover_type' in response_dict:
        response_dict['prime_mover_type'] = parse_prime_mover_type(response_dict['prime_mover_type'])
    if 'manufacturer' in response_dict:
        response_dict['manufacturer'] = parse_manufacturer(response_dict['manufacturer'])
    if 'first_unit_year' in response_dict:
        response_dict['first_unit_year'] = parse_first_year_occurrence(response_dict['first_unit_year'])
    if 'adhesion_factor' in response_dict:
        response_dict['adhesion_factor'] = parse_percentage(response_dict['adhesion_factor'])
    if 'allow_multiple_units' in response_dict:
        response_dict['allow_multiple_units'] = parse_multiple_units(response_dict['allow_multiple_units'])
    if 'brake_system' in response_dict:
        response_dict['brake_system'] = parse_brake_system(response_dict['brake_system'])
    if 'cooling_fluid_capacity' in response_dict:
        response_dict['cooling_fluid_capacity'] = parse_liters(response_dict['cooling_fluid_capacity'])
    if 'cylinders_size' in response_dict:
        response_dict['cylinders_size'] = parse_cylinders_size(response_dict['cylinders_size'])
    if 'fuel_capacity' in response_dict:
        response_dict['fuel_capacity'] = parse_fuel_capacity(response_dict['fuel_capacity'])
    if 'generator' in response_dict:
        response_dict['generator'] = parse_generator(response_dict['generator'])
    if 'minimum_track_radius' in response_dict:
        response_dict['minimum_track_radius'] = parse_meters(response_dict['minimum_track_radius'])
    if 'height' in response_dict:
        response_dict['height'] = parse_millimeters(response_dict['height'])
    if 'length' in response_dict:
        response_dict['length'] = parse_millimeters(response_dict['length'])
    if 'width' in response_dict:
        response_dict['width'] = parse_millimeters(response_dict['width'])
    if 'wheelbase' in response_dict:
        response_dict['wheelbase'] = parse_millimeters(response_dict['wheelbase'])
    if 'horsepower_available' in response_dict:
        response_dict['horsepower_available'] = parse_horsepower(response_dict['horsepower_available'])
    if 'horsepower_total' in response_dict:
        response_dict['horsepower_total'] = parse_horsepower(response_dict['horsepower_total'])
    if 'lubricant_oil_capacity' in response_dict:
        response_dict['lubricant_oil_capacity'] = parse_liters(response_dict['lubricant_oil_capacity'])
    if 'motor_capacity' in response_dict:
        response_dict['motor_capacity'] = parse_motor_capacity(response_dict['motor_capacity'])
    if 'rpm_limit' in response_dict:
        response_dict['rpm_limit'] = parse_int_with_unit(response_dict['rpm_limit'], "RPM")
    if 'sand_capacity' in response_dict:
        response_dict['sand_capacity'] = parse_float_with_unit(response_dict['sand_capacity'], "m³")
    if 'traction_effort' in response_dict:
        response_dict['traction_effort'] = parse_int_with_unit(response_dict['traction_effort'], "kgf")
    if 'truck_type' in response_dict:
        response_dict['truck_type'] = parse_truck_type(response_dict['truck_type'])
    if 'velocity_max' in response_dict:
        response_dict['velocity_max'] = parse_float_with_unit(response_dict['velocity_max'], "km/h")
    if 'velocity_min' in response_dict:
        response_dict['velocity_min'] = parse_float_with_unit(response_dict['velocity_min'], "km/h")
    if 'weight' in response_dict:
        response_dict['weight'] = parse_weight(response_dict['weight'])
    if 'weight_adherent' in response_dict:
        response_dict['weight_adherent'] = parse_weight(response_dict['weight_adherent'])
    if 'weight_per_axle' in response_dict:
        response_dict['weight_per_axle'] = parse_weight(response_dict['weight_per_axle'])
    if 'wheel_arrangement_aar' in response_dict:
        response_dict['wheel_arrangement_aar'] = parse_wheel_arrangement_aar(response_dict['wheel_arrangement_aar'])
    if 'wheel_arrangement_whyte' in response_dict:
        response_dict['wheel_arrangement_whyte'] = parse_wheel_arrangement_whyte(response_dict['wheel_arrangement_whyte'])
    if 'wheel_diameter' in response_dict:
        response_dict['wheel_diameter'] = parse_wheel_diameter(response_dict['wheel_diameter'])
    if 'gauge' in response_dict:
        response_dict['gauge'] = parse_gauge(response_dict['gauge'])
    if 'motor_builder' in response_dict:
        response_dict['motor_builder'] = parse_manufacturer(response_dict['motor_builder'])

    return response_dict


def extract_data_from_row(row) -> Optional[Tuple]:

    # title = row.find_all("th")
    # if len(title) > 0 and len(title[0].find_all('font')) > 0:
    #     return 'title', title[0].find_all('font')[0].text

    columns = row.find_all("td")
    if len(columns) < 2:
        return None

    string_to_key_map = {
        'Propulsão': 'prime_mover_type',
        'Fabricante': 'manufacturer',
        # 'Número de série': 'serial_number',
        'Modelo': 'name',
        'Ano de fabricação': 'first_unit_year',
        # 'Locomotivas fabricadas': 'total_units',
        'Classificação AAR': 'aar_wheel_arrangement',
        'Bitola': 'gauge',
        'truques': 'trucks_type',
        'Diâmetro das rodas': 'wheel_diameter',
        'Distância entre eixos': 'wheelbase',
        'Comprimento': 'length',
        'Largura': 'width',
        'Altura': 'height',
        'Peso da locomotiva': 'weight',
        'Peso por eixo': 'weight_per_axle',
        'Peso aderente': 'weight_adherent',
        # 'Tipo de combustível': 'fuel_type',
        'Capacidade de combustível': 'fuel_capacity',
        'Capacidade de óleo lubrificante': 'lubricant_oil_capacity',
        'Capacidade de líquido refrigerante': 'cooling_fluid_capacity',
        'Capacidade de areia':	'sand_capacity',
        'Fabricante do motor': 'motor_builder',
        'Motor primário': 'primary_motor',
        'RPM': 'rpm_limit',
        'Tipo de motor': 'motor_type',
        'Cilindradas do motor': 'motor_capacity',
        'Gerador': 'generator',
        'Motores de tração': 'traction_motors',
        'Tamanho dos cilindros': 'cylinders_size',
        'Tração múltipla': 'allow_multiple_units',
        'Velocidade máxima': 'velocity_max',
        'Velocidade mínima': 'velocity_min',
        'Potência total': 'horsepower_total',
        'Potência disponível para tração': 'horsepower_available',
        'Esforço de tração': 'traction_effort',
        'Fator de adesão': 'adhesion_factor',
        'Raio mínimo de inscrição': 'minimum_track_radius',
        'Sistema de freio': 'brake_system',
        # 'Ferrovias Originais': 'original_railroads',
        # 'Ferrovias que operou': 'operated_railroads',
        'SIGO': 'sigo_numeric_range',
        'Apelidos': 'nickname',
        # 'Local de operação': 'operation_locations',
        # 'Data de entrega': 'delivered_date',
        # 'Ano da entrada em serviço': 'first_service_year',
        # 'Proprietário atual': 'actual_owner',
        # 'Situação': 'status',
    }

    actual_key = columns[0].text if len(columns[0].find_all('a')) == 0 else columns[0].find_all('a')[0].text
    actual_key = str(actual_key).strip()

    if str(actual_key) not in string_to_key_map:
        return None

    return string_to_key_map[str(actual_key)], str(columns[1].text).replace("\n", "")


def parse_locomotive_url(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")

    response_dict = {
        'wikipedia_url': url,
    }

    info_table = soup.find_all("table", "infobox_v2")

    if not len(info_table):
        return {}

    for row in info_table[0].find_all("tr"):
        data = extract_data_from_row(row)
        if data is not None:
            response_dict[data[0]] = data[1]

    response_dict = parse_values(response_dict)

    return response_dict


if __name__ == '__main__':
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()

    log_filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "wikipedia_locomotives_crawler.log")
    fileHandler = logging.FileHandler(log_filename)
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)
    rootLogger.setLevel(logging.INFO)

    locomotives_urls = [
        'https://pt.wikipedia.org/wiki/ALCO_FA-1',
        'https://pt.wikipedia.org/wiki/ALCO_PA-2',
        'https://pt.wikipedia.org/wiki/ALCO_RS-3',
        'https://pt.wikipedia.org/wiki/ALCO_RSC-1',
        'https://pt.wikipedia.org/wiki/ALCO_RSC-3',
        'https://pt.wikipedia.org/wiki/ALCO_RSD-8',
        'https://pt.wikipedia.org/wiki/Baldwin_AS616E',
        'https://pt.wikipedia.org/wiki/Baldwin-Westinghouse_1-B%2BB-1',
        'https://pt.wikipedia.org/wiki/Baldwin-Westinghouse_C%2BC',
        'https://pt.wikipedia.org/wiki/EE_VFFLB',
        'https://pt.wikipedia.org/wiki/EE_RFN',
        'https://pt.wikipedia.org/wiki/EE_EFSJ',
        'https://pt.wikipedia.org/wiki/EMAQ_MX620',
        'https://pt.wikipedia.org/wiki/EMD_B12',
        'https://pt.wikipedia.org/wiki/EMD_BB40-2',
        'https://pt.wikipedia.org/wiki/EMD_BB45-2',
        'https://pt.wikipedia.org/wiki/EMD_DDM45',
        'https://pt.wikipedia.org/wiki/EMD_G12',
        'https://pt.wikipedia.org/wiki/EMD_G16',
        'https://pt.wikipedia.org/wiki/EMD_G22CU',
        'https://pt.wikipedia.org/wiki/EMD_G22U',
        'https://pt.wikipedia.org/wiki/EMD_G26CU',
        'https://pt.wikipedia.org/wiki/EMD_G8',
        'https://pt.wikipedia.org/wiki/EMD_GL8',
        'https://pt.wikipedia.org/wiki/EMD_GP18',
        'https://pt.wikipedia.org/wiki/EMD_GP9',
        'https://pt.wikipedia.org/wiki/EMD_GT18MC',
        'https://pt.wikipedia.org/wiki/EMD_GT22CUM-1',
        'https://pt.wikipedia.org/wiki/EMD_GT22CUM-2',
        'https://pt.wikipedia.org/wiki/EMD_GT26CUM',
        'https://pt.wikipedia.org/wiki/EMD_GT26MC',
        'https://pt.wikipedia.org/wiki/EMD_SD18',
        'https://pt.wikipedia.org/wiki/EMD_SD38-2',
        'https://pt.wikipedia.org/wiki/EMD_SD38M',
        'https://pt.wikipedia.org/wiki/EMD_SD40',
        'https://pt.wikipedia.org/wiki/EMD_SD40-2',
        'https://pt.wikipedia.org/wiki/EMD_SD60M',
        'https://pt.wikipedia.org/wiki/EMD_SD70',
        'https://pt.wikipedia.org/wiki/EMD_SD70M',
        'https://pt.wikipedia.org/wiki/EMD_SW',
        'https://pt.wikipedia.org/wiki/GE_1-C%2BC-1_(CPEF)',
        'https://pt.wikipedia.org/wiki/GE_1-C%2BC-1_(EFS)',
        'https://pt.wikipedia.org/wiki/GE_100T',
        'https://pt.wikipedia.org/wiki/GE_15T',
        'https://pt.wikipedia.org/wiki/GE_2-B%2BB-2',
        'https://pt.wikipedia.org/wiki/GE_2-C%2BC-2',
        'https://pt.wikipedia.org/wiki/GE_2-D%2BD-2',
        'https://pt.wikipedia.org/wiki/GE_244',
        'https://pt.wikipedia.org/wiki/GE_25T',
        'https://pt.wikipedia.org/wiki/GE_47T',
        'https://pt.wikipedia.org/wiki/GE_70T',
        'https://pt.wikipedia.org/wiki/GE_88T',
        'https://pt.wikipedia.org/wiki/GE_AC44i',
        'https://pt.wikipedia.org/wiki/GE_B%2BB_(CPEF)',
        'https://pt.wikipedia.org/wiki/GE_B-B_(CPEF_-_Baratinha)',
        'https://pt.wikipedia.org/wiki/GE_B-B_(EFS)',
        'https://pt.wikipedia.org/wiki/GE_B36-7',
        'https://pt.wikipedia.org/wiki/GE_BB33',
        'https://pt.wikipedia.org/wiki/GE_BB40-8M',
        'https://pt.wikipedia.org/wiki/GE_BB40-9M',
        'https://pt.wikipedia.org/wiki/GE_BB40-9WM',
        'https://pt.wikipedia.org/wiki/GE_C-C_(CPEF)',
        'https://pt.wikipedia.org/wiki/GE_C-C_(RFFSA)',
        'https://pt.wikipedia.org/wiki/GE_C22-7i',
        'https://pt.wikipedia.org/wiki/GE_C30-7',
        'https://pt.wikipedia.org/wiki/GE_C32-8',
        'https://pt.wikipedia.org/wiki/GE_C36-7',
        'https://pt.wikipedia.org/wiki/GE_C36ME',
        'https://pt.wikipedia.org/wiki/GE_C40-8',
        'https://pt.wikipedia.org/wiki/GE_C44-9WM',
        'https://pt.wikipedia.org/wiki/GE_C44-EMi',
        'https://pt.wikipedia.org/wiki/GE_ES43BBi',
        'https://pt.wikipedia.org/wiki/GE_ES58ACi',
        'https://pt.wikipedia.org/wiki/GE_SL100',
        'https://pt.wikipedia.org/wiki/GE_SL65T',
        'https://pt.wikipedia.org/wiki/GE_U10B',
        'https://pt.wikipedia.org/wiki/GE_U12B',
        'https://pt.wikipedia.org/wiki/GE_U12C',
        'https://pt.wikipedia.org/wiki/GE_U13B',
        'https://pt.wikipedia.org/wiki/GE_U18C',
        'https://pt.wikipedia.org/wiki/GE_U20C',
        'https://pt.wikipedia.org/wiki/GE_U22C',
        'https://pt.wikipedia.org/wiki/GE_U23C',
        'https://pt.wikipedia.org/wiki/GE_U26C',
        'https://pt.wikipedia.org/wiki/GE_U50',
        'https://pt.wikipedia.org/wiki/GE_U5B',
        'https://pt.wikipedia.org/wiki/GE_U6B',
        'https://pt.wikipedia.org/wiki/GE_U8B',
        'https://pt.wikipedia.org/wiki/GE_U9B',
        'https://pt.wikipedia.org/wiki/GE_UM10B',
        'https://pt.wikipedia.org/wiki/GMD_GMDH-1',
        'https://pt.wikipedia.org/wiki/LEW_DE_I_PA',
        'https://pt.wikipedia.org/wiki/LEW_DE_II_S',
        'https://pt.wikipedia.org/wiki/LEW_DE_III_M',
        'https://pt.wikipedia.org/wiki/Winterthur-BBC_1-D-1',
    ]

    fields = [
        'aar_wheel_arrangement', 'actual_owner', 'adhesion_factor', 'brake_system', 'manufacturer', 'cooling_fluid_capacity',
        'cylinders_size', 'delivered_date', 'first_service_year', 'first_unit_year', 'fuel_capacity', 'fuel_type',
        'gauge', 'generator', 'height', 'horsepower_total', 'horsepower_traction', 'length', 'lubrificant_oil_capacity',
        'minimum_radius', 'model', 'motor_builder', 'motor_capacity', 'motor_primary', 'motor_type',
        'multiple_traction_units', 'nickname', 'operated_railroads', 'operation_locations', 'original_railroads',
        'prime_mover_type', 'rpm_limit', 'sand_capacity', 'serial_number', 'sigo_numeric_range', 'status',
        'total_units', 'traction_effort', 'traction_motors', 'trucks_type', 'url', 'velocity_max', 'velocity_min',
        'weight', 'weight_adherent', 'weight_per_axle', 'wheel_diameter', 'wheelbase', 'width',
    ]

    parsed_locos = []
    for locomotive_url in locomotives_urls:
        logging.info("Parsing URL {}".format(locomotive_url))
        parsed_locos.append(parse_locomotive_url(locomotive_url))
    logging.info("Parsed {} locomotives".format(len(parsed_locos)))

    csv_output_filename = 'wikipedia_locomotives_crawler_output.csv'
    with open(csv_output_filename, 'w+', newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(fields)
        for locomotive in parsed_locos:
            writer.writerow([locomotive[field] if field in locomotive else '' for field in fields])
    logging.info("Exported CSV results to {}".format(csv_output_filename))

    json_output_filename = 'wikipedia_locomotives_crawler_output.json'
    with open(json_output_filename, 'w+', newline="") as json_file:
        json_file.write("[\n")
        for locomotive in parsed_locos:
            if len(locomotive.items()) == 0:
                continue
            json_file.write("\t{\n")
            for field in locomotive:
                if locomotive[field] is None:
                    continue
                if isinstance(locomotive[field], int):
                    json_file.write("\t\t\"{}\": {},\n".format(field, locomotive[field]))
                elif isinstance(locomotive[field], float):
                    json_file.write("\t\t\"{}\": {:.4f},\n".format(field, locomotive[field]))
                else:
                    json_file.write("\t\t\"{}\": \"{}\",\n".format(field, locomotive[field].replace('"', '\\"')))

            json_file.write("\t},\n")
        json_file.write("]\n")
    logging.info("Exported JSON results to {}".format(json_output_filename))

    print('Finished')
