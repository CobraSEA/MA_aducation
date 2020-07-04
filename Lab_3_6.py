countries = {"Ukraine":"UA", "Poland":"PL", "Norway":"NO", "Maldives":"MV", "Qatar":"QA"}
capitals = {"UA":"Kyiv", "PL":"Warsaw", "NO":"Oslo", "MV":"Male", "QA":"Doha"}

countries.update({"Austria":"AT"})
capitals["AT"] = "Wien"

for i in countries :
    print(f"Domain for country {i} is {countries[i]}")

for i in capitals :
    for j in countries :
        if i == countries[j] :
            print(f"The capital of country {j} is {capitals[i]}")
            break

for i in capitals :     # in one cycle
    for j in countries :
        if i == countries[j] :
            print(f"Domain for country {j} is {countries[j]}", end='; ')
            print(f"The capital of country {j} is {capitals[i]}")
            break

for i in countries :
    countries[i] = [countries[i], "COM", "GOV"]

print(countries)
#print(capitals)