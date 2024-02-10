function addDataInvestment(event) {
    event.preventDefault();
    let companyName = document.getElementById('companyName');
    let companyEmail = document.getElementById('companyEmail');
    let website = document.getElementById('website');
    let contactName = document.getElementById('contactName');
    let biography = document.getElementById('biography');
    let dateCompanyJoined = document.getElementById('dateCompanyJoined');
    let percentCompanyOwnened = document.getElementById('percentCompanyOwnened');
    let pipeLineLocation = document.getElementById('pipeLineLocation');
    
    console.log(companyName.value);
    console.log(companyEmail.value);
    console.log(website.value);
    console.log(contactName.value);
    console.log(biography.value);
    console.log(dateCompanyJoined.value);
    console.log(percentCompanyOwnened.value);
    console.log(pipeLineLocation.value);

    let list = [companyName,companyEmail,website,contactName,biography,dateCompanyJoined,percentCompanyOwnened,pipeLineLocation]

    sendInfoToDatabase(0,list)
}

function addDataInvest(event) {
    event.preventDefault();

    let investAmount = document.getElementById('investAmount');
    let investDate = document.getElementById('investDate');
    let webpercentCompanysite = document.getElementById('percentCompany');
    let investorUUID = document.getElementById('investorUUID');
    let investmentUUID = document.getElementById('investmentUUID');

    
    console.log(investAmount.value);
    console.log(investDate.value);
    console.log(webpercentCompanysite.value);
    console.log(investorUUID.value);
    console.log(investmentUUID.value);

    let list = [investAmount,investDate,webpercentCompanysite,investorUUID,investmentUUID]

    sendInfoToDatabase(1,list)
}

function addDataKPI(event) {
    event.preventDefault();
    let headcount = document.getElementById('headcount');
    let epitda = document.getElementById('epitda');
    let grossProfit = document.getElementById('grossProfit');
    let numLocations = document.getElementById('numLocations');
    let roi = document.getElementById('roi');
    let totalValueCompany = document.getElementById('totalValueCompany');
    let quarter = document.getElementById('quarter');
    let year = document.getElementById('year');
    let investmentUUID = document.getElementById('investmentUUIDKPI');
    
    console.log(headcount.value);
    console.log(epitda.value);
    console.log(grossProfit.value);
    console.log(numLocations.value);
    console.log(roi.value);
    console.log(totalValueCompany.value);
    console.log(quarter.value);
    console.log(year.value);
    console.log(investmentUUID.value);

    let list = [headcount,epitda,grossProfit,numLocations,roi,totalValueCompany,quarter,year,investmentUUID]

    sendInfoToDatabase(2,list)
}

function addDataInvestor(event) {
    event.preventDefault();

    let currentTotalCash = document.getElementById('currentTotalCash');
    let totalCashInvested = document.getElementById('totalCashInvested');
    let name = document.getElementById('name');
    let email = document.getElementById('email');
    let thesis = document.getElementById('thesis');
    let pipelineLocation = document.getElementById('pipelineLocation');
    
    console.log(currentTotalCash.value);
    console.log(totalCashInvested.value);
    console.log(name.value);
    console.log(email.value);
    console.log(thesis.value);
    console.log(pipelineLocation.value);

    let list = [currentTotalCash,totalCashInvested,name,email,thesis,pipelineLocation]

    sendInfoToDatabase(3, list)

}

function sendInfoToDatabase(whichTable, listOfData){
    //Change the connection to whatever grace uses
    //Test to make sure this works 
    //What about the UUID?
    
    const db = new sqlite3.Database("test/form_test/database/readTest.db", sqlite3.OPEN_READWRITE, (err)=> {
        
        if(err) {
            return console.error(err.message);

        } else{
            console.log ( "connected");

            if (whichTable == 0){
                let insertInvestment = 'INSERT INTO investment (companyName, companyEmail, website, contactName, bio, dateJoinNetwork, percentCompanyOwned, uuid, pipelineLocation) VALUES (?,?,?,?,?,?,?,?,?)'; 

                db.run(
                    insertInvestment,
                    listOfData,
                    (err)=>{
                        if (err){
                            return console.error(err.message);
                        } else {
                            console.log("inserting information...")
                        }
                        
                });

            } else if(whichTable == 1) {
                let insertInvestor = 'INSERT INTO investor (currentTotalCash, totalCashInvested, name, email, thesis, uuid, pipelineLocation) VALUES (?,?,?,?,?,?,?)';

                db.run(
                    insertInvestor,
                    listOfData,
                    (err)=>{
                        if (err){
                            return console.error(err.message);
                        } else {
                            console.log("inserting information...")
                        }
                        
                });

            } else if(whichTable == 2) {
                let insertRelationship = 'INSERT INTO investRelationship (investmentAmount, investmentDate, percentOfCompany, investorOrFundUUID, investmentUUID) VALUES (?,?,?,?,?)';

                db.run(
                    insertRelationship,
                    listOfData,
                    (err)=>{
                        if (err){
                            return console.error(err.message);
                        } else {
                            console.log("inserting information...")
                        }
                        
                });

            }else if(whichTable == 3) {
                let insertKPI = 'INSERT INTO kpi(headcount, epitda, grossProfit, numLocations, roi, totalValueOfCompany, quarter, year, kpiUUID, investmentUUID) VALUES (?,?,?,?,?,?,?,?,?,?)';

                db.run(
                    insertKPI,
                    listOfData,
                    (err)=>{
                        if (err){
                            return console.error(err.message);
                        } else {
                            console.log("inserting information...")
                        }
                        
                });

            }   

            console.log ( "closing...");
            db.close();
        }
    })
}

function openPage(pageName, elmnt, color) {
    // Hide all elements with class="tabcontent" by default */
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
  
    // Remove the background color of all tablinks/buttons
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
    }
  
    // Show the specific tab content
    document.getElementById(pageName).style.display = "block";
  
    // Add the specific color to the button used to open the tab content
    elmnt.style.backgroundColor = color;
}
  
// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();


