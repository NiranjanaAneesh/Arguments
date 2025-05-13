def total_cal(bill_amt,perc_tip):
    total=bill_amt*(1+0.01*perc_tip)
    total=round(total,2)
    print(f"please pay ${total}")
total_cal(200,24)