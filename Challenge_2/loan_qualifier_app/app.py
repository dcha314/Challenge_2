# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
import sys
import fire
import questionary
from pathlib import Path

from qualifier.utils.fileio import (
    load_csv, 
    load_bank_data,
    get_applicant_info,
    save_qualifying_loans
)

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
    find_qualifying_loans
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value

def save_csv(qualifying_loans)

    header = []

    prompt = questionary.text("Would you like to save your information?")
    
    if prompt == True:
        csvpath = questionary.text("Please enter your file name: [.csv]").ask()
        with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(header)
        for row in data:
        csvwriter.writerow(row.values())

def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)
