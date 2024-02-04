#holiday_short_name = ["holiday_name", "student_name", "holiday_date", "recipe_URL", "relevance_explanation", "recipe_advice"]


holidays_data = [
["Christmas", "Avanlee", "1225", "https://www.allrecipes.com/recipe/235104/peppermint-holiday-cookies/",
    "This is a fun recipe to fill Santa's tummy! Enjoyable and easy to make, merry Christmas!", "don't eat the ingredients"],

["St. Patrick's Day", "Clare", "0317", "https://www.thecountrycook.net/st-paddys-day-oreo-bark/",
    "This is a good dessert for St Patrick's day because the green on the bar matches the holiday", "follow the recipe"],

["Halloween", "Abran", "1031", "https://www.pillsbury.com/recipes/crescent-mummy-dogs/d52a57d7-ab8a-4a1c-8dae-f9f90d03b912",
    "It looks like a spooky treat", "follow the recipe"],

["National Star Wars Day", "Carter", "0504", "https://www.yummly.com/recipe/Baby-Yoda-Deviled-Eggs-with-Avocado-9369868",
    "Hello this is Carter and I got National Star Wars day and this is a recipe for Grogu deviled eggs", "follow the recipe"],

["Thanksgiving", "Shane", "1123", "https://www.gimmesomeoven.com/best-mashed-potatoes-recipe/",
    "Mine was Thanksgiving. I chose a mashed potatoes recipe and it fits Thanksgiving because mashed potatoes have become a staple dish on Thanksgiving tables across America.", "actually have a recipe!"],

["Veterans Day", "Conner", "1111", "https://www.yummly.com/recipe/National-Cherry-Pie-Day-_-Almond-Cherry-Pie-1133881?prm-v1",
    "Pie goes to any holiday", "I like pie"],

["Easter", "Violet", "0409", "https://www.southernliving.com/butterscotch-bird-nests-7152086",
    "It's Easter related because it's eggs in a nest and most eggs hatch in the spring. Also, his name is Jeremy.", "follow the recipe"],
    
["Valentine's Day", "Grace", "0214", "https://wilton.com/valentines-day-cake-pops/wlproj-9093/",
    "Here is my recipe for Valentine's Day cake pops. I think this goes well with the whole Valentine's Day idea because you can make these with red velvet cake and frost them with red, white, and pink icing and coat them with cutesy-pootsie sprinkles. My idea for the name of our program is Yummy Holiday Recipes.", "follow the recipe"]
]

print("Thank you for running our recipe program")
user_date = input("Enter a date in the format MMDD:")
def find_closest_holiday(input_date, holidays_data):
    min_diff = float('inf')
    closest_holiday = None
    
    for holiday in holidays_data:
        holiday_date = holiday[2]
        diff = abs(int(holiday_date) - int(input_date))
        if diff < min_diff:
            min_diff = diff
            closest_holiday = holiday
    return closest_holiday
while True:
    input_date = input("Please enter a date in MMDD format")
    closest_holiday = find_closest_holiday(input_date, holidays_data)
    if closest_holiday:
        print(f"This {closest_holiday[0]} recipe was provided by {closest_holiday[1]} and can be found on the website {closest_holiday[3]}."
                f"The reason that {closest_holiday[1]} thinks that it is relevant is: {closest_holiday[4]} and they want to remind you to {closest_holiday[5]}")
    else:
        print("No matching holiday found.")
    another_check = input("Do you want to check another date? (yes/no): ").lower()
    if another_check != "yes":
        break
print("Thank you for using the program!")

    
    
