<h2>Documentation</h2>

This django app aims to load stock data from CSV file into local database and api to fetch data for individuals stock based on the idstatementnav.

<br>

<h2>Tech Stack</h2>

    Backend (Django)
    Database (SQLite)
    API (REST API)

<br>

<h2>Project Structure</h2>

    Statement_Nav/
    	├── funds/
    	│   ├── management/
    	│   │   ├── commands/
    	│   │   │   ├── __init__.py
    	│   │   │   └── import_csv.py
    	│   ├── migrations/
    	│   │   ├── __init__.py
    	│   ├── __init__.py
    	│   ├── admin.py
    	│   ├── apps.py
    	│   ├── models.py
    	│   ├── serial/
    	│   ├── serializer.py
    	│   ├── tests.py
    	│   ├── views.py
    	├── statement/
    	│   ├── __init__.py
    	│   ├── asgi.py
    	│   ├── settings.py
    	│   ├── urls.py
    	│   ├── wsgi.py
    	├── db.sqlite3
    	├── manage.py

<br>

<h2>Step-By-Step Implementation</h2>

1. CSV Data Loading

  	Created a script import_csv.py which will read the data from the CSV file and store it in the local database.

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


3. Database Model

	  Define the database model based on the fields from the CSV file.

   		from django.db import models

		class Fund(models.Model):
		    fund_id = models.CharField(max_length=100, primary_key=True)
		    fund_full_name = models.CharField(max_length=255)
		    ticker = models.CharField(max_length=100)
		    date = models.DateField()
		    statement_of_nav = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    investments = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    listed_securities = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    registered_equities = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    ipo_investment = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    government_bonds = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    corporate_debentures = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    other_government_securities = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    bank_fixed_deposits = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    other_investments = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    current_assets = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    bank_balance = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    other_current_assets = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    current_liabilities = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    net_asset_value_gross = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    fund_management_and_depository_fee1 = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    fund_supervisor_fee1 = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    net_asset_value = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    units_outstanding = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    nav_per_unit = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    income_statement = models.TextField(null=True, blank=True)
		    income = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    realised_income = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    unrealised_income = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    expenses = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    preoperating_expenses = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    notice_publication_fee = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    audit_fee = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    fund_management_and_depositary_fee2 = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    fund_supervisor_fee2 = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    other_expenses = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		    net_income = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
		
		    def __str__(self):
		        return self.fund_full_name

5. API Implementation

	  Created API using the rest framework that fetches stock data based on the idstatementnav.

   		from django.shortcuts import render
		from rest_framework.views import APIView
		from rest_framework.response import Response
		from rest_framework import status
		from .models import Fund
		from .serializer import FundsSerializer
		
		class FundDetail(APIView):
		    def get(self, request, fund_id, format=None):
		        try:
		            fund = Fund.objects.get(fund_id=fund_id)
		            serializer = FundsSerializer(fund)
		            return Response(serializer.data)
		        except Fund.DoesNotExist:
		            return Response(status=status.HTTP_404_NOT_FOUND)

<br>

<h2>Running the Project</h2>

1. Loading the data in local database using python manage.py import_csv /path/to/csv_file
2. Running the server using python manage.py runserver
3. The API is then available in https://127.0.0.1:8000/funds/<str:fund_id>/

<br>

<h2>Fetching the Data</h2>

Sending a GET request to the https://127.0.0.1:8000/funds/258/

<h2>Response:</h2>
<img src="https://github.com/user-attachments/assets/7e2ef9f9-dd1c-452a-b1c3-694259f6a383">
<br>

<h2>Conclusion</h2>

This Django app loads data from CSV file into the local database and provides API to fetch data based in each stock.
