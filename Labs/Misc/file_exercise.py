# exercise - open a new text file called teams.txt, add the names of 5 sports teams.
# read and display teh names of teh 1st and 4th team . strip()
# edit the file so that teh top line is replaced with "this is a new line"
# print out teh edited file, line by line.

'''
sports_teams = ["West Ham", "Bayern Munich", "AC Milan", "Barcelona", "Real Madrid"]

file = open("teams.txt", "w")

for i in sports_teams:
    team = i + "\n"
    file.write(team)

file.close()


file = open("teams.txt", "r")

teams_copy = file.readlines()

teams_copy[0] = "this is a new line"
file = open("teams.txt", "w")
for i in range(len(teams_copy)):
    if i == len(teams_copy)-1:
        file.write(teams_copy[i])
    else:
        file.write(teams_copy[i]).strip() + "\n"

file.close()

file = open("teams.txt", "r")
for teams_copy in file:
    print(teams_copy.strip())
file.close
'''


# With statemeent - closes automatically

with open("filename.txt","w") as file: #aliase
    for n in range(1, 11):
        new_line = "this is line " + str(n) + "\n"
        file.write(new_line)
