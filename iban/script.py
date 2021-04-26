#!/usr/bin/env python
# coding: utf-8

import string
from textwrap import wrap
from typing import Dict

ALPHA: Dict[str, str] = {c: str(ord(c) % 55) for c in string.ascii_uppercase}

COUNTRY_CODE: str = "PT"
IBAN_CHECK_DIGITS: str = "50"
TOTAL_LENGTH: int = 25


def format_pt_iban(
    country_code: str,
    iban_check_digits: str,
    national_bank_code: str,
    branch_code: str,
    account_number: str,
    national_check_digits: str,
    format: str = "print",
) -> str:
    if format == "electronic":
        nib = (
            f"{national_bank_code}{branch_code}{account_number}{national_check_digits}"
        )
        return f"{country_code}{iban_check_digits}{nib}"
    elif format == "print":
        account_number = " ".join(wrap(account_number, 4))
        national_check_digits = " ".join(wrap(national_check_digits, 1))

        account_number_with_check = f"{account_number}{national_check_digits}"

        nib = f"{national_bank_code} {branch_code} {account_number_with_check}"

        return f"{country_code}{iban_check_digits} {nib}"
    elif format == "structure":
        nib = f"{national_bank_code} {branch_code} {account_number} {national_check_digits}"
        return f"{country_code}{iban_check_digits} {nib}"
    else:
        raise ValueError(f"{repr(format)} is not supported.")


def make_pt_iban(
    national_bank_code: str, branch_code: str, account_number: str, format="print"
) -> str:
    nib = f"{national_bank_code}{branch_code}{account_number}"

    complement = 98 - (int(nib + "00") % 97)
    national_check_digits = str(complement).zfill(2)

    return format_pt_iban(
        COUNTRY_CODE,
        IBAN_CHECK_DIGITS,
        national_bank_code,
        branch_code,
        account_number,
        national_check_digits,
        format=format,
    )


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

    iban = make_pt_iban(national_bank_code, branch_code, account_number, format="print")

    print(iban)
    print("Valid?", check_pt_iban(iban.replace(" ", "")))
