# Assuming that first SIP goes with invested_amt
def final_calculator(interest_rate, sip, number_of_years, principal_amount=0):
    months = number_of_years * 12
    invested_amt = principal_amount
    monthly_interest = interest_rate / 12
    
    for month in range(months):
        invested_amt = invested_amt + invested_amt * monthly_interest/100
        invested_amt  += sip
    return invested_amt

print(final_calculator(12, 1, 1, 100))
        