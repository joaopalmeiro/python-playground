#!/usr/bin/env python
# coding: utf-8

import string
from typing import Dict

ALPHA: Dict[str, str] = {c: str(ord(c) % 55) for c in string.ascii_uppercase}

COUNTRY_CODE: str = "PT"
IBAN_CHECK_DIGITS: str = "50"
TOTAL_LENGTH: int = 25


def make_pt_iban(national_bank_code: str, branch_code: str, account_number: str) -> str:
    nib = f"{national_bank_code}{branch_code}{account_number}"

    complement = 98 - (int(nib + "00") % 97)
    national_check_digits = str(complement).zfill(2)

    return f"{COUNTRY_CODE}{IBAN_CHECK_DIGITS}{nib}{national_check_digits}"


def check_pt_iban(iban: str) -> bool:
    if len(iban) != TOTAL_LENGTH:
        return False

    iban_to_validate = iban[4:] + iban[:4]

    check = int("".join(ALPHA.get(c, c) for c in iban_to_validate))

    return check % 97 == 1


if __name__ == "__main__":
    national_bank_code = "1234"
    branch_code = "4321"
    account_number = "12345678901"

    iban = make_pt_iban(national_bank_code, branch_code, account_number)

    print(iban)
    print(check_pt_iban(iban))
