# EB BILL
consumer_name = input("Enter consumer name: ")
tariff = input("Enter tariff domestic or commercial: ")
units = int(input("Enter consumed units: "))

bill = 0

if tariff == "domestic":
    if units <= 200:
        bill = 0
    elif units <= 250:
        bill = (units - 200) * 4.80
    elif units <= 300:
        bill = (units - 200) * 6.45
    else:
        bill = (units - 200) * 9.65

    # Subsidy
    cc_subsidy = 480.0
    new_subsidy = 960.0

    total_current = bill + cc_subsidy + new_subsidy

    print("Consumer name:", consumer_name)
    print("Total current charges Rs.:", total_current)
    print("CC subsidy Rs.:", cc_subsidy)
    print("CC new subsidy Rs.:", new_subsidy)
    print("EB bill:", bill)


else:
    bill = units * 10.15

    print("Consumer name:", consumer_name)
    print("EB bill:", bill)
