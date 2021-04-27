# What is the score?
#score = int(input("What is your test score? "))

# Determine the grade.
#if score >= 90:
    #print('Your grade is an A.')
#elif score >= 80:
    #print('Your grade is a B.')
#elif score >= 70:
    #print('Your grade is a C.')
#elif score >= 60:
    #print('Your grade is a D.')
#else:
    #print('Your grade is an F.')

#In/Not in practice
#counties = ["Arapahoe","Denver","Jefferson"]
#if "Arapahoe" in counties or "El Paso" in counties:
    #print("Arapahoe or El Paso are in the list of counties.")
#else:
     #print("Arapahoe or El Paso is not in the list of counties.")

#while loop practice
#x = 0
#while x <= 5:
    #print(x)
    #x = x + 1

#for loop practice
#counties = ["Arapahoe","Denver","Jefferson"]
#for county in counties:
    #print(county)

#numbers = [0, 1, 2, 3, 4]
#for num in numbers:
    #print(num)

#for num in range(5):
    #print(num)

#Key-value practice
#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict:
    #print(counties_dict.get(county))

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county, voters in counties_dict.items():
    #print(county,"county has",voters,"registered voters")

#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                #{"county":"Denver", "registered_voters": 463353},
                #{"county":"Jefferson", "registered_voters": 432438}]

#Iterate through list of dictionaries
#for county_dict in voting_data:
    #print(county_dict)

#Range function
#for i in range(len(voting_data)):
    #print(voting_data[i])

#Nested for loops
#for county_dict in voting_data:
    #for value in county_dict.values():
        #print(value)

#Retrieve registered voters
#for county_dict in voting_data:  
    #print(county_dict['registered_voters'])

#F strings
#for county, voters in counties_dict.items():
    #print(f"{county} county has {voters} registered voters.")

#F-string
#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
    #f"You received {candidate_votes:,} number of votes. "
    #f"The total number of votes in the election was {total_votes:,}. "
    #f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
#print(message_to_candidate)

#skill drill
#for county_dict in voting_data:  
    #print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters")
    
