counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" not in counties:
    print("True for El paso")
else:
     print("False")   
if "Arapahoe" in counties:
    print("True for Arapahoe")
else:
     print("False")        

if "Arapahoe" in counties or "El Paso" in counties:
    print("one of them is present")
else:
    print("one of them is not there")   
if not("El Paso") in counties:
    print("El paso not present===true")
else:
     print("El paso is present")   

x=0
while(x<=5):
    print(x)
    x=x+1

for county in counties:
    print(county)

for county in range(len(counties)):
    print(counties[county])    


 

coun_dict = {"Araphoe11":55667,
              "Denver22":4456,
              "Jefferson33":778} 

for i in coun_dict.keys():
    print(i) 
for i in coun_dict:
    print((coun_dict.get(i))) 

for key,value in coun_dict.items():
    print(key +" county has " + str(value) + " registered voters")        
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

for i in range(len(voting_data)):
    
      print(voting_data[i]['county'])  


for county_dict in voting_data:  

     print(county_dict.values())  


for county_dict in voting_data:
    
     for key, value in county_dict.items():

         print(value)  



for county_dict in voting_data:
    
     print(county_dict['registered_voters'])

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))

print(f"I received {(my_votes / total_votes) * 100}% of the total votes.")

