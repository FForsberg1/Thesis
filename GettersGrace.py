import sqlite3
import uuid
import AllTogether
con = sqlite3.connect('thesis.db')

#Investor Network functiosn 
class investorNetwork():

    def queryPeopleByName(self, name):
        cur = con.cursor()
        result = cur.execute('SELECT currentTotalCash, totalCashInvested, name, email, thesis FROM investor WHERE pipelineLocation = ? AND name = ?', ['Investor',name])
        result = result.fetchall()
        cur.close()

        return result

    def queryPeopleByThesis(self, thesis):
        cur = con.cursor()
        result = cur.execute('SELECT currentTotalCash, totalCashInvested, name, email, thesis FROM investor WHERE pipelineLocation = ? AND thesis = ?', ['Investor',thesis])
        result = result.fetchall()
        cur.close()

        return result
        
    def queryPeopleByCashInvested(self, cashInvested):
        cur = con.cursor()
        result = cur.execute('SELECT currentTotalCash, totalCashInvested, name, email, thesis FROM investor WHERE pipelineLocation = ? AND totalCashInvested = ?', ['Investor',cashInvested])
        result = result.fetchall()
        cur.close()

        return result
    
    def queryPeopleAll(self):
        cur = con.cursor()
        result = cur.execute('SELECT currentTotalCash, totalCashInvested, name, email, thesis FROM investor WHERE pipelineLocation = ?', ['Investor'])
        result = result.fetchall()
        cur.close()

        return result

#Invetment Network function
class investmentNetwork():

    def queryCompanyByName(self, name):
        cur = con.cursor()
        result = cur.execute('SELECT companyName, companyEmail, website, contactName, bio, dateJoinNetwork, percentCompanyOwned FROM investment WHERE pipelineLocation = ? AND companyName = ?', ['Investment',name])
        result = result.fetchall()
        cur.close()

        return result

    def queryCompanyByBio(self, bio):
        cur = con.cursor()
        result = cur.execute('SELECT companyName, companyEmail, website, contactName, bio, dateJoinNetwork, percentCompanyOwned FROM investment WHERE pipelineLocation = ? AND bio = ?', ['Investment', bio])
        result = result.fetchall()
        cur.close()

        return result
        
    def queryCompanyByPercentCompanyOwned(self, percentOwned):
        cur = con.cursor()
        result = cur.execute('SELECT companyName, companyEmail, website, contactName, bio, dateJoinNetwork, percentCompanyOwned FROM investment WHERE pipelineLocation = ? AND percentCompanyOwned = ?', ['Investment', percentOwned])
        result = result.fetchall()
        cur.close()

        return result
    
    def queryCompanyAll(self):
        cur = con.cursor()
        result = cur.execute('SELECT companyName, companyEmail, website, contactName, bio, dateJoinNetwork, percentCompanyOwned FROM investment WHERE pipelineLocation = ?', ['Investment'])
        result = result.fetchall()
        cur.close()

        return result

#Investor Pipeline function
class investorPipeline():

    def queryPeopleByName(self, name):
        cur = con.cursor()
        result = cur.execute('SELECT currentTotalCash, totalCashInvested, name, email, thesis FROM investor WHERE NOT pipelineLocation = ? AND name = ?', ['Investor',name])
        result = result.fetchall()
        cur.close()

        return result

    def queryPeopleByThesis(self, thesis):
        cur = con.cursor()
        result = cur.execute('SELECT currentTotalCash, totalCashInvested, name, email, thesis FROM investor WHERE NOT pipelineLocation = ? AND thesis = ?', ['Investor', thesis])
        result = result.fetchall()
        cur.close()

        return result
    
    def queryPeopleAll(self):
        cur = con.cursor()
        result = cur.execute('SELECT currentTotalCash, totalCashInvested, name, email, thesis FROM investor WHERE NOT pipelineLocation = ?', ['Investor'])
        result = result.fetchall()
        cur.close()

        return result

#Investment Pipeline function
class investmentPipeline():

    def queryCompanyByName(self, name):
        cur = con.cursor()
        result = cur.execute('SELECT companyName, companyEmail, website, contactName, bio, dateJoinNetwork, percentCompanyOwned FROM investment WHERE NOT pipelineLocation = ? AND companyName = ?', ['Investment', name])
        result = result.fetchall()
        cur.close()

        return result

    def queryCompanyByBio(self, bio):
        cur = con.cursor()
        result = cur.execute('SELECT companyName, companyEmail, website, contactName, bio, dateJoinNetwork, percentCompanyOwned FROM investment WHERE bio = ?', [bio])
        result = result.fetchall()
        cur.close()

        return result
    
    def queryCompanyAll(self):
        cur = con.cursor()
        result = cur.execute('SELECT companyName, companyEmail, website, contactName, bio, dateJoinNetwork, percentCompanyOwned FROM investment WHERE NOT pipelineLocation = ?', ['Investment'])
        result = result.fetchall()
        cur.close()

        return result

#Analysis function  
class analysis():

    def customQuery(self, companyName, kpiToQuery):
        cur = con.cursor()
        result = cur.execute('SELECT uuid FROM investment WHERE companyName = ?', [companyName])
        result = result.fetchall()

        actualResult = cur.execute('SELECT ' + kpiToQuery + ' FROM kpi WHERE investmentUUID = ?', [result[0][0]])
        actualResult = actualResult.fetchall()

        cur.close()

        return actualResult
    
    def dates(self, companyName):
        cur = con.cursor()
        result = cur.execute('SELECT uuid FROM investment WHERE companyName = ?', [companyName])
        result = result.fetchall()

        actualResult = cur.execute('SELECT quarter, year FROM kpi WHERE investmentUUID = ?', [result[0][0]])
        actualResult = actualResult.fetchall()

        hold = 0

        for element in actualResult:
            element = list(element)
            element.append(hold)
            actualResult[hold] = tuple(element)
            hold = hold + 1

        cur.close()

        return actualResult

  
# investNetwork = investmentNetwork()
# print( investNetwork.queryCompanyByName('Groove Capital') )
# print( investNetwork.queryCompanyByBio('Angel Investing Company') )
# print( investNetwork.queryCompanyByPercentCompanyOwned(0.2) )
# print( investNetwork.queryCompanyAll() )
# print('\n\n')

# torNetwork = investorNetwork()
# print( torNetwork.queryPeopleByName('Fund') )
# print( torNetwork.queryPeopleByThesis('Red Pandas') )
# print( torNetwork.queryPeopleByCashInvested(1000.0) )
# print( torNetwork.queryPeopleAll() )
# print('\n\n')

# peoplePipeline = investorPipeline()
# print( peoplePipeline.queryPeopleByName('Fremont') )
# print( peoplePipeline.queryPeopleByThesis('ROBOTS') )
# print( peoplePipeline.queryPeopleAll() )
# print('\n\n')


# companyPipeline = investmentPipeline()
# print( companyPipeline.queryCompanyByName('Rasta Pasta') )
# print( companyPipeline.queryCompanyByBio('News station') )
# print( companyPipeline.queryCompanyAll() )
# print('\n\n')

analysisKPI = analysis()
print( analysisKPI.customQuery('Groove Capital', 'headcount') )
print( analysisKPI.dates('Groove Capital') )