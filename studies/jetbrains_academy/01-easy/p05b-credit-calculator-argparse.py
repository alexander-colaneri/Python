from math import ceil, log
import argparse
import sys

parser = argparse.ArgumentParser(description='Credit Calculator')
parser.add_argument('--type', type=str,
                    help='Type "diff" for differentiated payment or "annuity".')
parser.add_argument('--principal', type=int,
                    help='Total amount of money you will have.')
parser.add_argument('--periods', type=int,
                    help='Total of months to pay.')
parser.add_argument('--payment', type=int,
                   help='Monthly payment.')
parser.add_argument('--interest', type=float,
                    help='Interest rate.')
args = parser.parse_args()
principal = args.principal
periods = args.periods
payment = args.payment


if args.interest is None:
    print('Incorrect parameters')

elif len(sys.argv) < 4:
    print('Incorrect parameters')

elif args.type == 'diff':
    interest = float(args.interest) / (100 * 12)
    overpayment = diff = 0
    for m in range(1, periods + 1):
        diff = ceil(principal / periods + interest * (principal - (principal * (m - 1) / periods)))
        overpayment += diff
        print(f'Month {m}: payment is {diff}')
    print()
    print(f'Overpayment = {overpayment - principal}')

elif args.type == 'annuity':
    interest = float(args.interest) / (100 * 12)
    # Principal:
    if payment and periods and interest:
        principal = round(payment / (
                    interest * pow((1 + interest), periods) / (pow(1 + interest, periods) - 1)))
        print(f'Your credit principal = {principal}!')
        print(f'Overpayment = {payment * periods - principal}')
    # Payments:
    elif principal and periods and interest:
        divider = pow(1 + interest, periods) - 1
        payment = ceil(principal * interest * pow((1 + interest), periods) / divider)
        print(f'\nYour monthly payment = {payment}!')
    # Months:
    elif principal and payment and interest:
        years = months_with_years = 0
        periods = ceil(log(payment / (payment - interest * principal), 1 + interest))
        if periods < 12:
            print(f'\nIt takes {periods:.0f} {"month" if periods == 1 else "months"} to repay this credit!')
        else:
            years = periods // 12  # full complete years.
            months_with_years = periods % 12  # the remainder = months.
            if years >= 1 and months_with_years == 0:
                print(f'You need {years} {"year" if years == 1 else "years"} to repay this credit!')
            else:
                print(f'You need {years} {"year" if years == 1 else "years"} and '
                      f'{months_with_years} {"month" if months_with_years == 1 else "months"} to repay this credit!')
            print(f'Overpayment = {(payment * periods) - principal}')

elif args.type != 'diff' and args.type != 'annuity':
    print('Incorrect parameters')