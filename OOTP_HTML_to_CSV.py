# Imports
from bs4 import BeautifulSoup
import csv
from tkinter import *

# Tkinter setup
root = Tk()
root.title('OOTP 23 HTML2CSV')
root.geometry('340x290+10+10')
root.resizable(width=False, height=False)
root.iconbitmap('ootp.ico')

# Tkinter objects
# Text
header = Label(root, text="OOTP 23 HTML2CSV")
header.configure(font=("Arial", 20))
header.place(x=32, y=5)
text1 = Label(root, text="HTML File Name:")
text1.place(x=5, y=45)
text2 = Label(root, text="Teams in your league:")
text2.place(x=5, y=75)
result_text = Label(root, text="Result:")
result_text.place(x=5, y=258)
# Buttons
button1 = Button(root, text="Convert to CSV", width=45, command=lambda: option1())
button1.place(x=5, y=105)
button2 = Button(root, text="Convert to CSV and Get Underperforming Players (Hitters)", width=45, command=lambda: option2())
button2.place(x=5, y=135)
button3 = Button(root, text="Convert to CSV and Get Underperforming Players (Pitchers)", width=45, command=lambda: option3())
button3.place(x=5, y=165)
button4 = Button(root, text="Convert to CSV and Get Undervalued College Hitters", width=45, command=lambda: option4())
button4.place(x=5, y=195)
button5 = Button(root, text="Convert to CSV and Get Undervalued College Pitchers", width=45, command=lambda: option5())
button5.place(x=5, y=225)
# Entry Fields
entry1 = Entry(root, width=37)
entry1.place(x=105, y=45)
result = Entry(root, width=46)
result.place(x=48, y=260)
# Option Menu
options = ["5-10 Teams", "11-15 Teams", "16 Teams", "17-22 Teams", "23-29 Teams", "30 Teams", "31-35 Teams", "36+ Teams"]
clicked = StringVar()
clicked.set("16 Teams")
dropdown1 = OptionMenu(root, clicked, *options)
dropdown1.config(width=27)
dropdown1.place(x=125, y=70)

# I love BeautifulSoup!!! 10/10

def option1():
    global main_option
    main_option = "1"
    main_menu_input = entry1.get()
    result.delete(0, 'end')
    if main_menu_input[-5::1] == ".html":
        result.insert(END, "Success! CSV Written to output.csv")
    else:
        result.insert(END, "Invalid file name!")
    function(main_menu_input)

def option2():
    global main_option
    global teams_num
    main_option = "2"
    main_menu_input = entry1.get()
    teams_primary = clicked.get()
    if teams_primary == "5-10 Teams":
        teams_num = .55
    elif teams_primary == "11-15 Teams":
        teams_num = .6
    elif teams_primary == "16 Teams":
        teams_num = .65
    elif teams_primary == "17-22 Teams":
        teams_num = .7
    elif teams_primary == "23-29 Teams":
        teams_num = .75
    elif teams_primary == "30 Teams":
        teams_num = .8
    elif teams_primary == "31-35 Teams":
        teams_num = .85
    elif teams_primary == "36+ Teams":
        teams_num == .95
    result.delete(0, 'end')
    if main_menu_input[-5::1] == ".html":
        result.insert(END, "Players written to console and hitters.txt!")
    else:
        result.insert(END, "Invalid file name!")
    function(main_menu_input)
    getHitters()

def option3():
    global main_option
    global teams_num
    main_option = "3"
    main_menu_input = entry1.get()
    teams_primary = clicked.get()
    if teams_primary == "5-10 Teams":
        teams_num = 0.5
    elif teams_primary == "11-15 Teams":
        teams_num = 0.5
    elif teams_primary == "16 Teams":
        teams_num = 0.5
    elif teams_primary == "17-22 Teams":
        teams_num = 2
    elif teams_primary == "23-29 Teams":
        teams_num = 3
    elif teams_primary == "30 Teams":
        teams_num = 5
    elif teams_primary == "31-35 Teams":
        teams_num = 7
    elif teams_primary == "36+ Teams":
        teams_num = 9
    result.delete(0, 'end')
    if main_menu_input[-5::1] == ".html":
        result.insert(END, "Players written to console and pitchers.txt!")
    else:
        result.insert(END, "Invalid file name!")

    function(main_menu_input)
    getPitchers()

def option4():
    global main_option
    global teams_num
    main_option = "4"
    main_menu_input = entry1.get()
    teams_primary = clicked.get()
    if teams_primary == "5-10 Teams":
        teams_num = 1
    elif teams_primary == "11-15 Teams":
        teams_num = 1.25
    elif teams_primary == "16 Teams":
        teams_num = 1.5
    elif teams_primary == "17-22 Teams":
        teams_num = 1.5
    elif teams_primary == "23-29 Teams":
        teams_num = 1.75
    elif teams_primary == "30 Teams":
        teams_num = 1.75
    elif teams_primary == "31-35 Teams":
        teams_num = 2
    elif teams_primary == "36+ Teams":
        teams_num = 2.5
    result.delete(0, 'end')
    if main_menu_input[-5::1] == ".html":
        result.insert(END, "Players written to console and collegeHitters.txt!")
    else:
        result.insert(END, "Invalid file name!")

    function(main_menu_input)
    getCollegeHitters()

def option5():
    global main_option
    global teams_num
    main_option = "5"
    main_menu_input = entry1.get()
    teams_primary = clicked.get()
    if teams_primary == "5-10 Teams":
        teams_num = .5
    elif teams_primary == "11-15 Teams":
        teams_num = .5
    elif teams_primary == "16 Teams":
        teams_num = .5
    elif teams_primary == "17-22 Teams":
        teams_num = 1.5
    elif teams_primary == "23-29 Teams":
        teams_num = 3
    elif teams_primary == "30 Teams":
        teams_num = 4
    elif teams_primary == "31-35 Teams":
        teams_num = 5.5
    elif teams_primary == "36+ Teams":
        teams_num = 7
    result.delete(0, 'end')
    if main_menu_input[-5::1] == ".html":
        result.insert(END, "Players written to console and collegeHitters.txt!")
    else:
        result.insert(END, "Invalid file name!")

    function(main_menu_input)
    getCollegePitchers()

def function(main_menu_input):
    global names
    global positions
    try:
            # Open the html file, parse it with BeautifulSoup
        with open(main_menu_input) as f:
            soup = BeautifulSoup(f, 'html.parser')

        # Sift through html data, find what we need
        temp = soup.find_all('th', class_="dr")
        names_temp = soup.find_all('th', class_="dl")
        stats = soup.find_all('td', class_="dr")
        names = soup.find_all('td', class_="dL")

        # Extract the data we need from the narrowed down data
        list = []
        for element in temp:
            new_temp = element.contents
            list.append(new_temp[0])

        names_header = []
        for element in names_temp:
            new_names_temp = element.contents
            names_header.append(new_names_temp[0])

        stats_list = []
        for element in stats:
            new_stats = element.contents
            stats_list.append(new_stats[0])

        names_list = []
        for element in names:
            new_names = element.contents
            try:
                names_list.append(new_names[0])
            except:
                continue

        # Weird stuff for the names header
        names_header.pop(0)
        names_header.pop(3)

        # Get the list of names
        names = names_list[2::(len(names_temp)-2)]
        positions = names_list[0::(len(names_temp)-2)]

        # Write the output CSV
        with open('output.csv', 'w', newline='') as csvfile:
            filecsv = csv.writer(csvfile) # Read the file into a CSV writer
            filecsv.writerow(names_header + list)
            length = int(len(stats_list) / len(temp))
            for i in range(0, length):
                filecsv.writerow(names_list[0:(len(names_temp)-2):] + stats_list[0:len(temp):])
                for i in range(0, len(temp)):
                    stats_list.pop(0)
                for i in range(0, len(names_temp)-2):
                    names_list.pop(0)
    except:
        print("Not a valid file name!")

def getHitters():
    # Print out a list of undervalued players
    if main_option == "2":
        print("Recommended Targets:")
        with open('output.csv', newline='') as f:
            rating_list = []
            output_names_list = []
            output_rating_list = []
            data = csv.reader(f, delimiter=' ', quotechar='|')
            for row in data:
                output = str(row)
                try:
                    new_output = output.split(',')
                    # Get stats
                    babip = float(new_output[-4])
                    bb = int(new_output[-15])
                    pa = int(new_output[8])
                    war = float(new_output[-3])
                    if war >= .7 and war <= 3:
                        rating = float((bb/pa) - (babip*5) + 2)
                    else:
                        rating = 0
                    rating_list.append(rating) 
                except:
                    continue

            for i in range(0, len(rating_list)):
                if rating_list[i] >= teams_num:
                    print(names[i] + '--' + positions[i] + '--' + str(rating_list[i]))
                    output_names_list.append(names[i])
                    output_rating_list.append(rating_list[i])

            if len(output_names_list) == 0:
                print("There are no recommended players!")
                print("Check the CSV file to see if there is something wrong or reach out to the creator of the tool.")
        with open('hitters.txt', 'w') as g:
            for i in range(0, len(output_names_list)):
                g.write(output_names_list[i] + '--' + str(output_rating_list[i]) + '\n')

def getPitchers():
    # Print out a list of undervalued players
    if main_option == "3":
        print("Recommended Targets:")
        with open('output.csv', newline='') as f:
            rating_list = []
            output_names_list = []
            output_rating_list = []
            data = csv.reader(f, delimiter=' ', quotechar='|')
            # Main loop; analyze each row/player
            for row in data:
                output = str(row)
                try:
                    new_output = output.split(',')
                    # Get stats
                    fip = float(new_output[-2])
                    kbb = float(new_output[-4])
                    era = float(new_output[-11])
                    diff = float(era-fip)
                    if diff >= 0:
                        rating = ((diff*2)-era/2) + (kbb**2+kbb) - (fip*2)
                    else:
                        rating = 0
                    rating_list.append(rating) 
                except:
                    continue
            # Get the outputs ready to be written
            for i in range(0, len(rating_list)):
                if rating_list[i] >= teams_num:
                    print(names[i] + '--' + positions[i] + '--' + str(rating_list[i]))
                    output_names_list.append(names[i])
                    output_rating_list.append(rating_list[i])

            if len(output_names_list) == 0:
                print("There are no recommended players!")
                print("Check the CSV file to see if there is something wrong or reach out to the creator of the tool.")
        with open('pitchers.txt', 'w') as g:
            for i in range(0, len(output_names_list)):
                g.write(output_names_list[i] + '--' + str(output_rating_list[i]) + '\n')

def getCollegeHitters():
    # Print out a list of undervalued players
    if main_option == "4":
        print("Recommended Targets:")
        with open('output.csv', newline='') as f:
            rating_list = []
            output_names_list = []
            output_rating_list = []
            data = csv.reader(f, delimiter=' ', quotechar='|')
            for row in data:
                output = str(row)
                try:
                    new_output = output.split(',')
                    # Get stats
                    babip_primary = new_output[-1]
                    babip_secondary = babip_primary[0:-2:1]
                    babip = float(babip_secondary)
                    obp = float(new_output[-4])
                    hr = int(new_output[-8])
                    rating = float((obp*20) + (hr/10) - (babip*20))
                    rating_list.append(rating) 
                except:
                    continue

            for i in range(0, len(rating_list)):
                if rating_list[i] >= teams_num:
                    print(names[i] + '--' + positions[i] + '--' + str(rating_list[i]))
                    output_names_list.append(names[i])
                    output_rating_list.append(rating_list[i])

            if len(output_names_list) == 0:
                print("There are no recommended players!")
                print("Check the CSV file to see if there is something wrong or reach out to the creator of the tool.")
        with open('collegeHitters.txt', 'w') as g:
            for i in range(0, len(output_names_list)):
                g.write(output_names_list[i] + '--' + str(output_rating_list[i]) + '\n')

def getCollegePitchers():
    # Print out a list of undervalued players
    if main_option == "5":
        print("Recommended Targets:")
        with open('output.csv', newline='') as f:
            rating_list = []
            output_names_list = []
            output_rating_list = []
            data = csv.reader(f, delimiter=' ', quotechar='|')
            for row in data:
                output = str(row)
                try:
                    new_output = output.split(',')
                    # Get stats
                    fip = float(new_output[-3])
                    kbb = float(new_output[-6])
                    era = float(new_output[-4])
                    rating = ((era-fip*2)-era/5) + (kbb**2+kbb*2) - (fip*1.25)
                    rating_list.append(rating) 
                except:
                    continue

            for i in range(0, len(rating_list)):
                if rating_list[i] >= teams_num:
                    print(names[i] + '--' + positions[i] + '--' + str(rating_list[i]))
                    output_names_list.append(names[i])
                    output_rating_list.append(rating_list[i])

            if len(output_names_list) == 0:
                print("There are no recommended players!")
                print("Check the CSV file to see if there is something wrong or reach out to the creator of the tool.")
        with open('collegePitchers.txt', 'w') as g:
            for i in range(0, len(output_names_list)):
                g.write(output_names_list[i] + '--' + str(output_rating_list[i]) + '\n')

# Tkinter mainloop
root.mainloop()