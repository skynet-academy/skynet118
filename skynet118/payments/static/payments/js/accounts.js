const btn = document.querySelector('#info-bank');
const bankAccount = document.querySelector('#bank-account');

const eu_account ={
    "Region": "EU", 
    "Account holder":"nicolas humberto sulca vega", 
    "BIC": "TRWIBEB1XXX", "IBAN": "BE34967239660690", 
    "Wise's address": "Avenue Louise 54, Room S52, Brussels 1050, Belgium" 
}

const usa_account = {
    "Region": "USA",
    "Account holder": "nicolas humberto sulca vega",
    "Routing number": 084009519,
    "Account number": 9600001624272964,
    "Account type": "Checking",
    "Wise's address": "19 W 24th Street New York NY 10010, United States"
}

const canada_account = {
    "Region": "Canada",
    "Account holder": "nicolas humberto sulca vega",
    "Institution number": 621,
    "Account number": 200110159811,
    "Transit number": 16001,
    "Wise's address": "99 Bank Street, Suite 1420, Ottawa ON K1P 1H4, Canada"
}

let displayInfo = (account) =>{
    const info = document.querySelector('#info-account');
    if(info.hasChildNodes()){
        for(const p in account){
            info.removeChild(info.firstChild)
        }
    }
    for(const x in account){
        var item = document.createElement("P");
        item.innerHTML = `<strong>${x}</strong> : ${account[x]}`;
        info.appendChild(item)
    }
}

let changeAccount = (selection) =>{
    if(selection == "usa"){
        displayInfo(usa_account);
    }else if(selection == "europe"){
        displayInfo(eu_account)
    }else if(selection == "canada"){
        displayInfo(canada_account)
    }
}
