import sqlite3
import uuid
conInvestor = sqlite3.connect('thesis.db')

class InvestorEntity():

    def __init__(self):
        curInvestor = conInvestor.cursor()
        curInvestor.execute('CREATE TABLE IF NOT EXISTS investor (currentTotalCash FLOAT, totalCashInvested FLOAT, name TEXT, email TEXT, thesis TEXT, uuid TEXT PRIMARY KEY)')
        curInvestor.execute('DELETE FROM investor')
        curInvestor.close()


    def new(self, currentTotalCash, totalCashInvested, name, email, thesis):    
        #Error checking to see if this investor already in the system 
        curInvestor = conInvestor.cursor()
        id = uuid.uuid1() 
        id = str(id.int)
        curInvestor.execute('INSERT INTO investor (currentTotalCash, totalCashInvested, name, email, thesis, uuid) VALUES ("' + str(currentTotalCash) + '","' + str(totalCashInvested) + '","' + name + '","' + email + '","' + thesis + '","' + id + '")')
        curInvestor.close()
        return id


    def get(self, uuid):
        curInvestor = conInvestor.cursor()

        result = curInvestor.execute('SELECT* FROM investor WHERE uuid = "' + uuid + '"')
        result = result.fetchall()

        curInvestor.close()
        if (result == None):
            print('No person with that uuid found in investor')
            return None
         
        else:
            return result
         

    def getAll(self):
        
        curInvestor = conInvestor.cursor()
        allRows = []

        result = curInvestor.execute('SELECT* FROM investor')
        result = result.fetchall()

        for element in result:
            allRows.append(element)

        curInvestor.close()
        return allRows
    

    def delete(self, uuid):

        curInvestor = conInvestor.cursor()
        curInvestor.execute('DELETE FROM investor WHERE uuid = "' + uuid + '"')

        result = curInvestor.execute('SELECT changes()')
        changes = result.fetchall()

        curInvestor.close()
        return changes
    

    def updateCurrentTotalCash(self, newTotalCash, uuid):
        curInvestor = conInvestor.cursor()
        curInvestor.execute('UPDATE investor SET currentTotalCash = "' + str(newTotalCash) + '" WHERE uuid = "' + uuid + '"')
        curInvestor.close()


    def updateTotalCashInvested(self, newTotalCashInvested, uuid):
        curInvestor = conInvestor.cursor()
        curInvestor.execute('UPDATE investor SET totalCashInvested = "' + str(newTotalCashInvested) + '" WHERE uuid = "' + uuid + '"')
        curInvestor.close()   

#Testing of code ________________________________________________

investor = InvestorEntity()

currentTotalCash = 5.1
totalCashInvested = 50.5
investorName = 'Fremont'
investorEmail = 'Fremont@mail.com'
investorThesis = 'I am broke college student you think I have money to invest?'

idInvestor =  investor.new(currentTotalCash, totalCashInvested, investorName, investorEmail, investorThesis) 
print (idInvestor)
#print( investor.get(idInvestor))
#print( investor.getAll())
#investor.updateCurrentTotalCash(.1,idInvestor)
#investor.updateTotalCashInvested(999.9,idInvestor)
#print( investor.get(idInvestor))
#print( investor.delete(idInvestor))
#print( investor.getAll())

#conInvestor.close()               #This is what is edited out