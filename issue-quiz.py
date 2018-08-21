#Tamer Abdalla's issue quiz

testScore = 0

#Q1: What percentage of the city of Toronto's populations do Somali-Canadians make up?
somaliPopulation = 1

q1Answer = input("What percentage of the City of Toronto's population do Somali-Canadians make up? Enter the percentage as a value without the % symbol. Example '10%' as '10'.")
if q1Answer is "1":
        testScore = testScore + 5
        print("Correct! Somali-Canadians make up 1% of the population in the City of Toronto. Yet, they are over-represented at 16% of homocide victims. Congratulations! You scored 5 points on this question. Your new score is " + str(testScore))
else:
        print("Incorrect. Somali-Canadians make up 1% of the population in the City of Toronto. Yet, they are over-represented at 16% of homocide victims.")

#Q2: What age range are Somali-Canadian victims of homocide?
ageRange = ["0", "Under 18", "18-29", "30+"]

q2Answer = input("What age range are Somali-Canadian victims of homocide? Enter 1 for Under 18, 2 for 18-29, or 3 for 30+. ")
if q2Answer is "2":
        testScore = testScore + 5
        print("Correct! 67.5% of Somali-Canadians who are victims of homocide are between 18-29.")
        print("Congratulations! You scored 5 points on this question.")
        print("Your new score is " + str(testScore))
else:
        print("Incorrect. 67.5% Somali-Canadian victims of homocide are between 18-29, almost a decade younger than the national average.")

#Q3: What percentage of youth surveyed directly knew a victim of homocide?
youthSurvyed = 75

q3Answer = input("What percentage of youth surveyed directly knew a victim of homocide? Enter the numerical value only.")
if q3Answer == "75":
    testScore = testScore + 5
    print("Correct! 67.5% of Somali-Canadians who are victims of homocide are between 18-29.")
    print("Congratulations! You scored 5 points on this question.")
else:
    print("Incorrect. 75% of youth surveyed said they knew a victim of homocide.")

#final score
print("Your final score is " + str(testScore))