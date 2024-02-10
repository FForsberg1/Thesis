import sqlite3
import uuid
con = sqlite3.connect('thesis.db')
cur = con.cursor()

class InvestorPipelineEntity():

    def __init__(self):
        cur.execute('CREATE TABLE IF NOT EXISTS investor (currentTotalCash FLOAT, totalCashInvested FLOAT, name TEXT, email TEXT, thesis TEXT, uuid TEXT PRIMARY KEY, pipelineLocation TEXT)')
        cur.execute('DELETE FROM investor')


    def new(self, currentTotalCash, totalCashInvested, name, email, thesis):    
        #Error checking to see if this investor already in the system 
        id = uuid.uuid1() 
        id = str(id.int)
        cur.execute('INSERT INTO investorPipeline (currentTotalCash, totalCashInvested, name, email, thesis, uuid) VALUES ("' + str(currentTotalCash) + '","' + str(totalCashInvested) + '","' + name + '","' + email + '","' + thesis + '","' + id + '")')
        return id


    def get(self, uuid):
        result = cur.execute('SELECT* FROM investorPipeline WHERE uuid = "' + uuid + '"')
        result = result.fetchall()

        if (result == None):
            print('No person with that uuid found in investor pipeline')
            return None
         
        else:
            return result
         

    def getAll(self):

        allRows = []

        result = cur.execute('SELECT* FROM investorPipeline')
        result = result.fetchall()

        for element in result:
            allRows.append(element)

        return allRows
    

    def delete(self, uuid):

        cur.execute('DELETE FROM investorPipeline WHERE uuid = "' + uuid + '"')

        result = cur.execute('SELECT changes()')
        changes = result.fetchall()

        return changes
    

    def updateCurrentTotalCash(self, newTotalCash, uuid):
        cur.execute('UPDATE investorPipeline SET currentTotalCash = "' + str(newTotalCash) + '" WHERE uuid = "' + uuid + '"')


    def updateTotalCashInvested(self, newTotalCashInvested, uuid):
        cur.execute('UPDATE investorPipeline SET totalCashInvested = "' + str(newTotalCashInvested) + '" WHERE uuid = "' + uuid + '"')


    def updatePipelineLocation(self, newPipelineLocation, uuid):
        cur.execute('UPDATE investorPipeline SET pipelineLocation = "' + newPipelineLocation + '" WHERE uuid = "' + uuid + '"')
         

#Testing of code ________________________________________________

investor = InvestorPipelineEntity()

currentTotalCash = 5.1
totalCashInvested = 50.5
investorName = 'Fremont'
investorEmail = 'Fremont@mail.com'
investorThesis = 'I am broke college student you think I have money to invest?'

idInvestor =  investor.new(currentTotalCash, totalCashInvested, investorName, investorEmail, investorThesis) 
print (idInvestor)
print( investor.get(idInvestor))
print( investor.getAll())
investor.updateCurrentTotalCash(.1,idInvestor)
investor.updateTotalCashInvested(999.9,idInvestor)
investor.updatePipelineLocation("Accept",idInvestor)
print( investor.get(idInvestor))
print( investor.delete(idInvestor))
print( investor.getAll())

con.close()