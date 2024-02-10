import sqlite3
import uuid
con = sqlite3.connect('thesis.db')
cur = con.cursor()

class InvestmentEntity():

    def __init__(self):
        cur.execute('CREATE TABLE IF NOT EXISTS investmentPipeline (companyName TEXT, companyEmail TEXT, website TEXT, contactName TEXT, bio TEXT, investmentDate DATE, percentCompanyOwned FLOAT, uuid TEXT PRIMARY KEY, pipelineLocation TEXT)')
        cur.execute('DELETE FROM investment')


    def new(self, companyName, companyEmail, website, contactName, bio, investmentDate, percentCompanyOwned):    
        #Error checking to see if this investment already in the system 
        id = uuid.uuid1() 
        id = str(id.int)
        cur.execute('INSERT INTO investmentPipeline (companyName, companyEmail, website, contactName, bio, investmentDate, percentCompanyOwned, uuid) VALUES ("' + companyName + '","' + companyEmail + '","' + website + '","' + contactName + '","' + bio + '","' + investmentDate + '","' + str(percentCompanyOwned) + '","' + id + '")')
        return id


    def get(self, id):
        result = cur.execute('SELECT* FROM investmentPipeline WHERE uuid = "' + id + '"')
        result = result.fetchall()
         
        if (result == None):
            print('No company with that uuid found in investment pipeline')
            return None
        
        else:
             return result
        
        
    def getAll(self):

        allRows = []

        result = cur.execute('SELECT* FROM investmentPipeline')
        result = result.fetchall()

        for element in result:
            allRows.append(element)

        return allRows
    

    def delete(self, id):

        cur.execute('DELETE FROM investmentPipeline WHERE uuid = "' + id + '"')

        result = cur.execute('SELECT changes()')
        changes = result.fetchall()

        return changes


    def updatePipelineLocation(self, newPipelineLocation, uuid):
        cur.execute('UPDATE investmentPipeline SET pipelineLocation = "' + newPipelineLocation + '" WHERE uuid = "' + uuid + '"')


#Testing of code ________________________________________________
investment = InvestmentEntity()

companyName = 'Groove Capital'
companyEmail = 'grace@email.com'
website = 'www.GrooveCapital.com'
contactName = 'Grace'
bio = 'Angel Investing Comapny'
investmentDate = '11-30-2023'
percentCompanyOwned = .5

id = investment.new(companyName, companyEmail, website, contactName, bio, investmentDate, percentCompanyOwned) 
print (id)
print( investment.get(id))
print( investment.getAll())
investment.updatePipelineLocation('Accepted',id)
print( investment.get(id))
print( investment.delete(id))
print( investment.getAll())

con.close()