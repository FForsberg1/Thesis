import sqlite3
import uuid
con = sqlite3.connect('thesis.db')

#This class represents the table of investments (the companies) in the database design. These are the companies being invested in by investors
#The columns in this table are called, in this order, with the associated data type
#TABLE NAME investment( companyName TEXT, companyEmail TEXT, website TEXT, contactName TEXT, bio TEXT, dateJoinNetwork DATE, percentCompanyOwned FLOAT, uuid TEXT PRIMARY KEY, pipelineLocation TEXT)
class InvestmentEntity():

    def __init__(self):
        curInvestment = con.cursor()
        curInvestment.execute('CREATE TABLE IF NOT EXISTS investment (companyName TEXT, companyEmail TEXT, website TEXT, contactName TEXT, bio TEXT, dateJoinNetwork DATE, percentCompanyOwned FLOAT, uuid TEXT PRIMARY KEY, pipelineLocation TEXT)')
        curInvestment.close()

    def new(self, companyName, companyEmail, website, contactName, bio, investmentDate, percentCompanyOwned, pipelineLication):    
        curInvestment = con.cursor() 
        id = uuid.uuid1() 
        id = str(id)
        curInvestment.execute('INSERT INTO investment (companyName, companyEmail, website, contactName, bio, dateJoinNetwork, percentCompanyOwned, uuid, pipelineLocation) VALUES ("' + companyName + '","' + companyEmail + '","' + website + '","' + contactName + '","' + bio + '","' + investmentDate + '","' + str(percentCompanyOwned) + '","' + id + '","' + pipelineLication + '")')
        curInvestment.close()
        return id

    def deleteRows(self):
        curInvestment = con.cursor()
        curInvestment.execute('DELETE FROM investment')
        curInvestment.close()

    #The rest of these methods are not used in this code, I used them for testing of the database

    def get(self, id):
        curInvestment = con.cursor()
        result = curInvestment.execute('SELECT* FROM investment WHERE uuid = "' + id + '"')
        result = result.fetchall()
        
        curInvestment.close()

        if (result == None):
            print('No company with that UUID found in investment')
            return None
        
        else:
             return result
        
    def getAll(self):

        curInvestment = con.cursor()
        allRows = []

        result = curInvestment.execute('SELECT* FROM investment')
        result = result.fetchall()

        curInvestment.close()

        for element in result:
            allRows.append(element)

        return allRows
    
    def delete(self, id):
        
        curInvestment = con.cursor()
        curInvestment.execute('DELETE FROM investment WHERE uuid = "' + id + '"')

        result = curInvestment.execute('SELECT changes()')
        changes = result.fetchall()

        curInvestment.close()
        return changes
    
    def updatePipelineLocation(self, newPipelineLocation, uuid):
        curInvestment = con.cursor()
        curInvestment.execute('UPDATE investment SET pipelineLocation = "' + newPipelineLocation + '" WHERE uuid = "' + uuid + '"')
        curInvestment.close()

#This class represents the table of investor (people and the fund) in the database design. These are the people who make investments on investments.
#The columns in this table are called, in this order, with the associated data type
#TABLE NAME investor (currentTotalCash FLOAT, totalCashInvested FLOAT, name TEXT, email TEXT, thesis TEXT, uuid TEXT PRIMARY KEY, pipelineLocation TEXT)
class InvestorEntity():

    def __init__(self):
        curInvestor = con.cursor()
        curInvestor.execute('CREATE TABLE IF NOT EXISTS investor (currentTotalCash FLOAT, totalCashInvested FLOAT, name TEXT, email TEXT, thesis TEXT, uuid TEXT PRIMARY KEY, pipelineLocation TEXT)')
        curInvestor.close()

    def new(self, currentTotalCash, totalCashInvested, name, email, thesis, pipelineLocation):    
        curInvestor = con.cursor()
        id = uuid.uuid1() 
        id = str(id)
        curInvestor.execute('INSERT INTO investor (currentTotalCash, totalCashInvested, name, email, thesis, uuid, pipelineLocation) VALUES ("' + str(currentTotalCash) + '","' + str(totalCashInvested) + '","' + name + '","' + email + '","' + thesis + '","' + id + '","' + pipelineLocation + '")')
        curInvestor.close()
        return id

    def deleteRows(self):
        curInvestor = con.cursor()
        curInvestor.execute('DELETE FROM investor')
        curInvestor.close()

    #The rest of these methods are not used in this code, I used them for testing of the database

    def get(self, uuid):
        curInvestor = con.cursor()

        result = curInvestor.execute('SELECT* FROM investor WHERE uuid = "' + uuid + '"')
        result = result.fetchall()

        curInvestor.close()
        if (result == None):
            print('No person with that uuid found in investor')
            return None
         
        else:
            return result
         
    def getAll(self):
        
        curInvestor = con.cursor()
        allRows = []

        result = curInvestor.execute('SELECT* FROM investor')
        result = result.fetchall()

        for element in result:
            allRows.append(element)

        curInvestor.close()
        return allRows
    
    def delete(self, uuid):

        curInvestor = con.cursor()
        curInvestor.execute('DELETE FROM investor WHERE uuid = "' + uuid + '"')

        result = curInvestor.execute('SELECT changes()')
        changes = result.fetchall()

        curInvestor.close()
        return changes
    
    def updateCurrentTotalCash(self, newTotalCash, uuid):
        curInvestor = con.cursor()
        curInvestor.execute('UPDATE investor SET currentTotalCash = "' + str(newTotalCash) + '" WHERE uuid = "' + uuid + '"')
        curInvestor.close()

    def updateTotalCashInvested(self, newTotalCashInvested, uuid):
        curInvestor = con.cursor()
        curInvestor.execute('UPDATE investor SET totalCashInvested = "' + str(newTotalCashInvested) + '" WHERE uuid = "' + uuid + '"')
        curInvestor.close()   

    def updatePipelineLocation(self, newPipelineLocation, uuid):
        curInvestor = con.cursor()
        curInvestor.execute('UPDATE investor SET pipelineLocation = "' + newPipelineLocation + '" WHERE uuid = "' + uuid + '"')
        curInvestor.close()  

#This class represents the table of investment relationships (who invested in what, and associated data). These are all the investments done by people or the fund on companies
#The columns in this table are called, in this order, with the associated data type
#TABLE NAME investRelationship (investmentAmount FLOAT, investmentDate DATE, percentOfCompany FLOAT, investorOrFundUUID TEXT, investmentUUID TEXT)
class Invest_RelationshipEntity():

    def __init__(self):
        curRelationship = con.cursor()

        #Foreign Key are not being nice
        #curRelationship.execute('CREATE TABLE IF NOT EXISTS investRelationship (investmentAmount FLOAT, investmentDate DATE, percentOfCompany FLOAT, investorOrFund TEXT FOREGIN KEY(investorOrFund) REFERENCES investor(uuid), investmentName TEXT FOREGIN KEY investmentName REFERENCES investment(uuid) )')
        
        curRelationship.execute('CREATE TABLE IF NOT EXISTS investRelationship (investmentAmount FLOAT, investmentDate DATE, percentOfCompany FLOAT, investorOrFundUUID TEXT, investmentUUID TEXT)')
        curRelationship.close()

    def new(self, investmentAmount, investmentDate, percentOfCompany, investorOrFund, investmentName):    
        curRelationship = con.cursor()
        curRelationship.execute('INSERT INTO investRelationship (investmentAmount, investmentDate, percentOfCompany, investorOrFundUUID, investmentUUID) VALUES ("' + str(investmentAmount) + '","' + str(investmentDate) + '","' + str(percentOfCompany) + '","' + investorOrFund + '","' + investmentName +'")')
        curRelationship.close()
        return  investorOrFund, investmentName
    
    def deleteRows(self):
        curRelationship = con.cursor()
        curRelationship.execute('DELETE FROM investRelationship')
        curRelationship.close()
    
    #The rest of these methods are not used in this code, I used them for testing of the database

    def getInvestorOrFund(self, id):
        curRelationship = con.cursor()
        result = curRelationship.execute('SELECT* FROM investRelationship WHERE investorOrFundUUID = "' + id + '"')
        result = result.fetchall()
        
        curRelationship.close()

        if (result == None):
            print('No invest or fund with that UUID found in investment')
            return None
        
        else:
             return result
        
    def getInvestmentName(self, id):
        curRelationship = con.cursor()
        result = curRelationship.execute('SELECT* FROM investRelationship WHERE investmentUUID = "' + id + '"')
        result = result.fetchall()
        
        curRelationship.close()

        if (result == None):
            print('No investment name with that UUID found in investment')
            return None
        
        else:
             return result
        
    def getAll(self):

        curRelationship = con.cursor()
        allRows = []

        result = curRelationship.execute('SELECT* FROM investRelationship')
        result = result.fetchall()

        curRelationship.close()

        for element in result:
            allRows.append(element)

        return allRows
    
    def deleteInvestorOrFund(self, id):
        
        curRelationship = con.cursor()
        curRelationship.execute('DELETE FROM investRelationship WHERE investorOrFundUUID = "' + id + '"')

        result = curRelationship.execute('SELECT changes()')
        changes = result.fetchall()

        curRelationship.close()
        return changes

#This class represents the table of KPI (Key Perfomance indicators) data. KPI is info about the company giving a quick overview of how well the company is doing
#The columns in this table are called, in this order, with the associated data type
#TABLE NAME kpi (headcount INTEGER, epitda FLOAT, grossProfit FLOAT, numLocations INTEGER, roi FLOAT, totalValueOfCompany FLOAT, quarter INTEGER, year INTEGER, kpiUUID TEXT, investmentUUID TEXT)
class KPIEntity():

    def __init__(self):
        curKPI = con.cursor()
        curKPI.execute('CREATE TABLE IF NOT EXISTS kpi (headcount INTEGER, epitda FLOAT, grossProfit FLOAT, numLocations INTEGER, roi FLOAT, totalValueOfCompany FLOAT, quarter INTEGER, year INTEGER, kpiUUID TEXT, investmentUUID TEXT)')
        curKPI.close()

    def new(self, headcount, epitda, grossProfit, numLocations, roi, totalValueOfCompany, quarter, year, investmentUUID):    
        curKPI = con.cursor()
        id = uuid.uuid1() 
        id = str(id)
        curKPI.execute('INSERT INTO kpi(headcount, epitda, grossProfit, numLocations, roi, totalValueOfCompany, quarter, year, kpiUUID, investmentUUID) VALUES ("' + str(headcount) + '","' +  str(epitda) + '","' + str(grossProfit) + '","' + str(numLocations) + '","' + str(roi) + '","' + str(totalValueOfCompany) + '","' + str(quarter) + '","' + str(year) + '","' + str(id) + '","' + str(investmentUUID) + '")')
        curKPI.close()
        return id, investmentUUID
    
    def deleteRows(self):
        curKPI = con.cursor()
        curKPI.execute('DELETE FROM kpi')
        curKPI.close()
    
    #The rest of these methods are not used in this code, I used them for testing of the database

    def get(self, id):
        curKPI = con.cursor()
        result = curKPI.execute('SELECT* FROM kpi WHERE kpiUUID = "' + id + '"')
        result = result.fetchall()
        
        curKPI.close()

        if (result == None):
            print('No KPI with that email found in investment')
            return None
        
        else:
             return result
        
    def getAll(self):

        curKPI = con.cursor()
        allRows = []

        result = curKPI.execute('SELECT* FROM kpi')
        result = result.fetchall()

        curKPI.close()

        for element in result:
            allRows.append(element)

        return allRows
    
    def delete(self, id):
        
        curKPI = con.cursor()
        curKPI.execute('DELETE FROM kpi WHERE kpiUUID = "' + id + '"')

        result = curKPI.execute('SELECT changes()')
        changes = result.fetchall()

        curKPI.close()
        return changes

#Main run method, run this to create and populate the data. You only need (and should) to run this once
def runMe():

    investor = InvestorEntity()
    investment = InvestmentEntity()
    investRelationship = Invest_RelationshipEntity()
    kpi = KPIEntity()

    idInvestor = []

    with open('FakeData_Investor.txt','r') as fakeData:
        for line in fakeData:
            line = line.split(',')

            idInvestor.append( investor.new(line[0], line[1], line[2], line[3], line[4], line[5]) )

    idInvestment = []
    
    with open('FakeData_Investment.txt','r') as fakeData:
        for line in fakeData:
            line = line.split(',')

            idInvestment.append( investment.new(line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7]) )

    idRelationship = []

    value = 0

    with open('FakeData_Relationship.txt','r') as fakeData:
        for line in fakeData:
            line = line.split(',')

            if (value == 0):
                idRelationship.append( investRelationship.new(line[0],line[1],line[2], idInvestor[0], idInvestment[0]) )

            elif (value == 1 or value == 2):
                idRelationship.append( investRelationship.new(line[0],line[1],line[2], idInvestor[0], idInvestment[1]) )
            
            elif(value == 3):
                idRelationship.append( investRelationship.new(line[0],line[1],line[2], idInvestor[1], idInvestment[0]) )

            value = value + 1

    idKPI = []
    value = 0

    with open('FakeData_KPI.txt','r') as fakeData:
        for line in fakeData:
            line = line.split(',')

            if (value < 4):
                idKPI.append( kpi.new(line[0],line[1],line[2], line[3], line[4], line[5], line[6], line[7], idInvestment[0]) )
            else:
                idKPI.append( kpi.new(line[0],line[1],line[2], line[3], line[4], line[5], line[6], line[7], idInvestment[1]) )

            value = value + 1

    con.commit()

#Helper method, prints all rows from all tables
def printTables():

    investor = InvestorEntity()
    investment = InvestmentEntity()
    investRelationship = Invest_RelationshipEntity()
    kpi = KPIEntity()

    print('\nInvestor\n')
    print(investor.getAll())

    print('\nInvestment\n')
    print(investment.getAll())

    print('\nRelationship\n')
    print(investRelationship.getAll())  

    print('\nKPI\n')
    print(kpi.getAll()) 

    con.commit() 

#Helper method. delelets all rows from all tables
def deleteAllRows():
    investor = InvestorEntity()
    investment = InvestmentEntity()
    investRelationship = Invest_RelationshipEntity()
    kpi = KPIEntity()

    investor.deleteRows()
    investment.deleteRows()
    investRelationship.deleteRows()
    kpi.deleteRows()

    con.commit()

#Demo method, for week 2 presentation 
def runMeDEMO():

    investor = InvestorEntity()

    with open('FakeData_Investor.txt','r') as fakeData:
        for line in fakeData:
            line = line.split(',')

            currentTotalCash = line[0]
            totalCashInvested = line[1]
            investorName = line[2]
            investorEmail = line[3]
            investorThesis = line[4]

            print(line)

            idInvestor =  investor.new(currentTotalCash, totalCashInvested, investorName, investorEmail, investorThesis, line[5]) 

    con.commit() 


#Testing of code_____________________________________________________________________________________
#To get thus set up uncommet out line 450 and run the file, then commet line 450 and uncommetn line 451 to confim that the database is filled

#runMe()             
printTables()
#deleteAllRows()
#runMeDEMO()