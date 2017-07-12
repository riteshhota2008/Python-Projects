tax_rates = {
    'State': {
        'AZ': .056,
        'CO': .029,
        'MT': 0.0,
        'NV': .0685,
        'TX': .0625
    },
    'Country': {
        'CAN': .05,
        'UK': .2,
        'ESP': .21,
        'GER': .19,
        'JAP': .08
    }
}

print("Enter tax lookup \n \
1: Country \n \
2: State\n")

tax_lookup = int(input("\nselect:"))
if tax_lookup == 1:
    choice = 'Country'
else:
    choice = 'State'
cost = float(input("Enter Cost: "))
rate = str(input("Select Tax Rate (%s): " % ','.join(tax_rates[choice].keys())))

print("Cost of %.2f in %s is %.2f" % (cost, rate, float(cost + (cost * tax_rates[choice][rate]))))
