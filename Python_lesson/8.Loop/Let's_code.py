bread=["Rye bread","Wheat","White"]
meat=["Meatball","Sausages","Chicken breast"]
vegetable=["Lettuce","Tomata","Cucumber"]
sauce=["Mayounnaise","Honey mustard","Chili sauce"]

print("Possible combinations of Lyeng's sandwich shops")
for i in bread:
    for j in meat:
        for k in vegetable:
            for l in sauce:
                print(i +" +", j +" +", k +" +", l)

