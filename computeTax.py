def computTax(status, TaxableIncome):
    if status == "single":
        if TaxableIncome <= 8350:
            tax = TaxableIncome * 0.10
        else:
            pass
    elif status == "Married Joint":
        if TaxableIncome <= 16700:
            pass
       
    elif status == "Married Separate":
        if TaxableIncome <= 8350:
            pass
    elif status == "Family Head":
        if TaxableIncome <= 8350:
            pass
    else: 
        return "invalid status"
       