## Last week our homework included completing a task to create a variable entry for each persons holiday / recipe

## So everyone should have something like this:

hoilday_data = ["Christmas", "Avanlee", "1225", "https://www.allrecipes.com/recipe/235104/peppermint-holiday-cookies/", "This is a fun recipe to fill santas tummy! Enjoyable and easy to make, merry Cristmas!", "dont eat the ingreidients"
hoilday_data = ["St. Patricks day", "Clare", "0317", "https://www.thecountrycook.net/st-paddys-day-oreo-bark/", "This is a good desert for St patrick’s day because the green on the bar matches the holiday", "follow the recipe"]
hoilday_data = ["Haloween", "Abran", "1031", "https://www.pillsbury.com/recipes/crescent-mummy-dogs/d52a57d7-ab8a-4a1c-8dae-f9f90d03b912", "it looks like a spooky treat", "follow the recipe"]
hoilday_data = ["National Star Wars Day", "Carter", "0504", "https://www.yummly.com/recipe/Baby-Yoda-Deviled-Eggs-with-Avocado-9369868", "Hello this is Carter and I got National starwas day and this is a recipe for Grogu deviled eggs", "follow the recipe"]
hoilday_data = ["Thanksgiving", "Shane", "1123", "https://www.gimmesomeoven.com/best-mashed-potatoes-recipe/", "mine was thanksgiving I chose mashed potatoes recipe and it fits thanksgiving because  Mashed potatoes have become a staple dish on Thanksgiving tables across America. and I call it Thanksgiving food.", "actually have a recipe!"]
hoilday_data = ["Vetrans Day", "Conner", "1111", "", "", ""]
hoilday_data = ["Easter", "Violet", "0409", "https://www.southernliving.com/butterscotch-bird-nests-7152086 ", "its easter related bc its eggs in a nest because most eggs hatch in the spring also his name is jeremy", "follow the recipe"]
hoilday_data = ["Valentines Day", "Grace", "0214", "https://wilton.com/valentines-day-cake-pops/wlproj-9093/", "Here is my recipe for Valentine's Day cake pops. I think this goes well with the whole Valentine's Day idea because you can make these with red velvet cake and frost them with red, white, and pink icing and coat them with cutsie-pootsie sprinkles. My idea for the name of our program is Yummy Holiday Recipes.", "follow the recipe"]

## created in their "student folder"
                
                
##  So now that everyone has a github account we want to upload our code for everyone to see.
## First we need to create a special key that we will use to authenticate
                
                cd
                ## entering "cd " and pressing enter will return you to your HOME directory
                pwd
                ## you should get a return file path that is like /home/yourusername
                mkdir .ssh
                # we are creating a folder named .ssh
                cd .ssh
                # we are goign into the folder we just created
                ssh-keygen -t RSA
                ENTER
                ENTER
                ENTER
                ENTER
                ## this command will generate the special key.  It will prompt you several times for input, you can just hit ENTER
                ## we will use all the default settings.
                cat id_rsa.pub
                ## the keygen command generated two files, a linked public and private key.  The public bit is like the lock, and the
                ## private bit is like the key.   So we need to give github a copy of the public bit.
                ## You're gonna copy the ssh-rsa bit all the way to the end
                
                ## Then go to your browser, log into your github.com account, then go to User -> setttings -> ssh & gpg keys
                ## we're gonna paste in the key where it says "add ssh key"
                
                
## Ok, now we have our SSH keys loaded into our github accounts  -
## we need to tell our local system to use SSH instead of the HTTPS we were using before                
               
               
cd
cd creeksidecoding
git remote remove origin
git remote add origin git@github.com:daretogo/creeksidecoding.git
                
                
                
## Now we're all set up, we should verify we have the latest copy of the software:
                
git pull
git status
                
git add (file you want to upload)
                
git commit -m "message about your code here"
                
git push
                
                
## also, if you've made changes to a file but want to get the latest versions of that file you can use
                
git stash
                
git pulll
                
git stash apply
                
############################################################################################################
                ##  All of the above just gets us to the point where you can upload data to the creeksidecoding repo
                ## Please keep all files that you upload in your OWN student account.  You may LOOK at other sudents files
                ## but please do not modify them.
                
If you do accidentally modify another students file and save it, GIT will track that change.  You would not want to add or commit
that so please use:
                
                git restore path/to/file/to/revert     to revert it to original state.
                
                
#################################################################################################################        
                
# Let's talk requirements! 

# 1. Understanding the Project Requirements 📋
# First, we need to outline what our application must do. This is like creating a recipe for our code! Here's what we've got:

# Input: 
# Output: 

# 2. Date Tracking and Parsing

# Current Date: 
# Input Date: 

# 3. Comparing Dates 🔍


# 4. Displaying the Recipe 🥘

#????  

# While Loop: We can use a while True loop to keep our program running. It's like saying, "Keep going until we decide to stop."
# Breaking the Loop: We'll provide a way to exit the program, maybe by typing 'exit'.


# 6. Handling Errors 🚫
# What if someone types in an invalid date? We need to handle such situations gracefully.

# List of Requirements: Write down everything our application needs to do. Think about the inputs, outputs, and special cases.
# Program Structure Thoughts: Discuss with your team how we should structure our program. How do we keep it running? How do we handle different inputs?
                
                
