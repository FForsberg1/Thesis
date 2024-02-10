import sqlite3
import uuid
conRelationship = sqlite3.connect('thesis.db')

class Invest_RelationshipEntity():

    def __init__(self):
        curRelationship = conRelationship.cursor()

        #Foregin key is not working
        #cur.execute('CREATE TABLE IF NOT EXISTS investRelationship (investmentAmount FLOAT, investmentDate DATE, percentOfCompany FLOAT, investorOrFund TEXT, investmentName TEXT), FOREGIN KEY(investorOrFund) REFERENCES investor(uuid)')    #, FOREGIN KEY investmentName RELATES companyName FROM investment DELETE CASCADE

        curRelationship.execute('CREATE TABLE IF NOT EXISTS investRelationship (investmentAmount FLOAT, investmentDate DATE, percentOfCompany FLOAT, investorOrFund TEXT, investmentName TEXT)')
        curRelationship.execute('DELETE FROM invest')

        curRelationship.close()

    def new(self, investmentAmount, investmentDate, percentOfCompany, investorOrFund, investmentName):    
        #Error checking to see if this investor already in the system 
        curRelationship = conRelationship.cursor()
        curRelationship.execute('INSERT INTO investRelationship (investmentAmount, investmentDate, percentOfCompany, investorOrFund, investmentName) VALUES ("' + str(investmentAmount) + '","' + str(investmentDate) + '","' + str(percentOfCompany) + '","' + investorOrFund + '","' + investmentName +'")')
        curRelationship.close()

        return  investorOrFund, investmentName
    
    def getInvestorOrFund(self, id):
        curRelationship = conRelationship.cursor()
        result = curRelationship.execute('SELECT* FROM investRelationship WHERE investorOrFund = "' + id + '"')
        result = result.fetchall()
        
        curRelationship.close()

        if (result == None):
            print('No invest or fund with that UUID found in investment')
            return None
        
        else:
             return result
        
    def getInvestmentName(self, id):
        curRelationship = conRelationship.cursor()
        result = curRelationship.execute('SELECT* FROM investRelationship WHERE investmentName = "' + id + '"')
        result = result.fetchall()
        
        curRelationship.close()

        if (result == None):
            print('No investment name with that UUID found in investment')
            return None
        
        else:
             return result
        
    def getAll(self):

        curRelationship = conRelationship.cursor()
        allRows = []

        result = curRelationship.execute('SELECT* FROM investRelationship')
        result = result.fetchall()

        curRelationship.close()

        for element in result:
            allRows.append(element)

        return allRows
    
    def deleteInvestorOrFund(self, id):
        
        curRelationship = conRelationship.cursor()
        curRelationship.execute('DELETE FROM investRelationship WHERE investorOrFund = "' + id + '"')

        result = curRelationship.execute('SELECT changes()')
        changes = result.fetchall()

        curRelationship.close()
        return changes

#Testing of code    
invest_Relationship = Invest_RelationshipEntity()

investmentAmount = 100.0
investmentDate = 12/5/23
percentOfCompany = .9
idInvestor = 'Fremont'
idInvestment = 'Colorado College'

testingID = invest_Relationship.new(investmentAmount, investmentDate, percentOfCompany, idInvestor, idInvestment)
print(testingID)
print(invest_Relationship.getInvestorOrFund(testingID[0]))
print(invest_Relationship.getInvestmentName(testingID[1]))
print(invest_Relationship.getAll)
print(invest_Relationship.deleteInvestorOrFund(testingID[0]))

#conRelationship.close()                   This is what I had to edit out
