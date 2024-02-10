import sqlite3
import uuid
import Investor
#import Investment
#import Invest_Relationship

investor = Investor.InvestorEntity()
#investment = Investment.InvestmentEntity()

print('done')


#Run this,  Cannot operate on a closed database. fails on initlize
#Then go to line 97 on investor and re-run. Works
#Add back line 4 and 8 on this file and re run, fails but on the delete? Wait a second it takes a bit to run