# -*- coding: utf-8 -*-

"""
Author: Scott Burgert
Contact me at: https://github.com/quantumech3/
Date written: 2/1/2019

Project name: Payroll
Purpose: 
   Calculates a persons net pay given gross pay, hours worked and pay per hour, etc.
"""


# record must be tuple in format:  (firstName: str,
#                                   lastName: str,
#                                   employeeNum: str,
#                                   employeeType: "M" or "S" depending on if management or staff,
#                                   hrsWorked: float,
#                                   payRate: float,
#                                   deductionAmt: int)
def payroll(record):
    if record[3] != "M": # Ignore management
        grossPay = record[4] * record[5]            # grossPay = hrsWorked * payRate
        _401k = grossPay * 0.05                     # 401k = 5% of grossPay
        ssMedi = grossPay * .765                    # ssMedi = 7.65% of grossPay
        deductions = record                         # deductions = 'Given data'... Whatever that is haha
        fed_taxes = deductions                      # I know this wont work... I need clarification on the requirements
                                                    # What does it mean when deductions = 'given data'?




