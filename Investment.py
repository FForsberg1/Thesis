import sqlite3
import uuid
conInvestment = sqlite3.connect('thesis.db')

class InvestmentEntity():

    def __init__(self):
        curInvestment = conInvestment.cursor()
        curInvestment.execute('CREATE TABLE IF NOT EXISTS investment (companyName TEXT, companyEmail TEXT, website TEXT, contactName TEXT, bio TEXT, investmentDate DATE, percentCompanyOwned FLOAT, uuid TEXT PRIMARY KEY)')
        curInvestment.execute('DELETE FROM investment')
        curInvestment.close()

    def new(self, companyName, companyEmail, website, contactName, bio, investmentDate, percentCompanyOwned):    
        #Error checking to see if this investment already in the system
        curInvestment = conInvestment.cursor() 
        id = uuid.uuid1() 
        id = str(id.int)
        curInvestment.execute('INSERT INTO investment (companyName, companyEmail, website, contactName, bio, investmentDate, percentCompanyOwned, uuid) VALUES ("' + companyName + '","' + companyEmail + '","' + website + '","' + contactName + '","' + bio + '","' + investmentDate + '","' + str(percentCompanyOwned) + '","' + id + '")')
        curInvestment.close()
        return id

    def get(self, id):
        curInvestment = conInvestment.cursor()
        result = curInvestment.execute('SELECT* FROM investment WHERE uuid = "' + id + '"')
        result = result.fetchall()
        
        curInvestment.close()

        if (result == None):
            print('No company with that email found in investment')
            return None
        
        else:
             return result
        
    def getAll(self):

        curInvestment = conInvestment.cursor()
        allRows = []

        result = curInvestment.execute('SELECT* FROM investment')
        result = result.fetchall()

        curInvestment.close()

        for element in result:
            allRows.append(element)

        return allRows
    
    def delete(self, id):
        
        curInvestment = conInvestment.cursor()
        curInvestment.execute('DELETE FROM investment WHERE uuid = "' + id + '"')

        result = curInvestment.execute('SELECT changes()')
        changes = result.fetchall()

        curInvestment.close()
        return changes
        
#Testing of code ________________________________________________
#investment = InvestmentEntity()

#companyName = 'Groove Capital'
#companyEmail = 'grace@email.com'
#website = 'www.GrooveCapital.com'
#contactName = 'Grace'
#bio = 'Angel Investing Comapny'
#investmentDate = '11-30-2023'
#percentCompanyOwned = .5

#id = investment.new(companyName, companyEmail, website, contactName, bio, investmentDate, percentCompanyOwned) 
#print (id)
#print( investment.get(id))
#print( investment.getAll())
#print( investment.delete(id))
#print( investment.getAll())

#conInvestment.close()                   This is what I had to edit out