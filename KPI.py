import sqlite3
import uuid
con = sqlite3.connect('thesis.db')

class KPIEntity():

    def __init__(self):
        curKPI = con.cursor()
        curKPI.execute('CREATE TABLE IF NOT EXISTS kpi (headcount INTEGER, epitda FLOAT, grossProfit FLOAT, numLocations INTEGER, roi FLOAT, totalValueOfCompany FLOAT, quarter INTEGER, year INTEGER, kpiUUID TEXT, investmentUUID TEXT)')
        curKPI.execute('DELETE FROM kpi')
        curKPI.close()

    def new(self, headcount, epitda, grossProfit, numLocations, roi, totalValueOfCompany, quarter, year, investmentUUID):    
        #Error checking to see if this investor already in the system 
        curKPI = con.cursor()
        id = uuid.uuid1() 
        id = str(id.int)
        curKPI.execute('INSERT INTO kpi(headcount, epitda, grossProfit, numLocations, roi, totalValueOfCompany, quarter, year, kpiUUID, investmentUUID) VALUES ("' + str(headcount) + '","' +  str(epitda) + '","' + str(grossProfit) + '","' + str(numLocations) + '","' + str(roi) + '","' + str(totalValueOfCompany) + '","' + str(quarter) + '","' + str(year) + '","' + str(id) + '","' + str(investmentUUID) + '")')
        curKPI.close()
        return id, investmentUUID
    
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

#Testing of code ________________________________________________

kpi = KPIEntity()

headcount = 87
epitda = 123.456
grossProfit = 7
numLocations = 15
roi = 1.1
totalValueOfCompany = 3500
quarter = 4
year = 2023
investmentUUID = 'Colorado College'

kpiID, investmentUUID = kpi.new(headcount, epitda, grossProfit, numLocations, roi, totalValueOfCompany, quarter, year, investmentUUID)
print(kpiID, investmentUUID)
print( kpi.get(kpiID))
print( kpi.getAll())
print( kpi.delete(kpiID))
print( kpi.getAll())
