import csv
from django.core.management.base import BaseCommand
from funds.models import Fund

class Command(BaseCommand):
    help = 'Load data from a CSV file into the Fund model'
    
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)
    
    def handle(self, *args, **options):
        csv_file = options['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Fund.objects.create(
                    fund_id=row['idstatementnav'],
                    fund_full_name=row['Fund_full_Name'],
                    ticker=row['Ticker'],
                    date=row['Date'],
                    statement_of_nav=row['StatementOfNav'],
                    investments=row['Investments'],
                    listed_securities=row['ListedSecurities'],
                    registered_equities=row['RegisteredEquities'],
                    ipo_investment=row['IpoInvestment'],
                    government_bonds=row['GovernmentBonds'],
                    corporate_debentures=row['CorporateDebentures'],
                    other_government_securities=row['OtherGovernmentSecurities'],
                    bank_fixed_deposits=row['BankFixedDeposits'],
                    other_investments=row['OtherInvestments'],
                    current_assets=row['CurrentAssets'],
                    bank_balance=row['BankBalance'],
                    other_current_assets=row['OtherCurrentAssets'],
                    current_liabilities=row['CurrentLiabilities'],
                    net_asset_value_gross=row['NetAssetValueGross'],
                    fund_management_and_depository_fee1=row['FundManagementAndDepositoryFee1'],
                    fund_supervisor_fee1=row['FundSupervisorFee1'],
                    net_asset_value=row['NetAssetValue'],
                    units_outstanding=row['UnitsOutstanding'],
                    nav_per_unit=row['NavPerUnit'],
                    income_statement=row['IncomeStatement'],
                    income=row['Income'],
                    realised_income=row['RealisedIncome'],
                    unrealised_income=row['UnrealisedIncome'],
                    expenses=row['Expenses'],
                    preoperating_expenses=row['PreoperatingExpenses'],
                    notice_publication_fee=row['NoticePublicationFee'],
                    audit_fee=row['AuditFee'],
                    fund_management_and_depositary_fee2=row['FundManagementAndDepositaryFee2'],
                    fund_supervisor_fee2=row['FundSupervisorFee2'],
                    other_expenses=row['OtherExpenses'],
                    net_income=row['NetIncome']
                )
        self.stdout.write(self.style.SUCCESS('Successfully imported CSV data'))
