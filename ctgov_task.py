#Retrieve list of trials from clinical trial data set based on start year of the trial and 
# on condition of trial. Plotting number of trials started over different years and plotting number of trials 
#related to a specific condition over different years.


import xml.etree.ElementTree as ET
import glob
import matplotlib.pyplot as plt
import numpy as np



year = {}	
status_dict = {}
conditions = {}


file_list= glob.glob('/home/musadiq/Desktop/data/*.xml')




def plot_bar_x(years, year_frequency):
    # this is for plotting purpose
    index = np.arange(len(years))
    plt.bar(index, year_frequency)
    plt.xlabel('Year', fontsize=5)
    plt.ylabel('No of Studies', fontsize=5)
    plt.xticks(index, years, fontsize=5, rotation=30)
    plt.yticks(year_frequency, fontsize=5, rotation=30)
    plt.title('Number of Studies for years 1957-2020')
    plt.show()


def plot_year_condition(years):

	inp_cond = input("Enter the conditon: ")

	condition_frequency = []
	for yr in years:
		count = 0
		for elem in year[yr]:
			if elem['Condition']==inp_cond:
				count += 1
		condition_frequency.append(count)
    # this is for plotting purpose


	index = np.arange(len(years))
	plt.bar(index, condition_frequency)
	plt.xlabel('Year', fontsize=5)
	plt.ylabel('No of Studies', fontsize=5)
	plt.xticks(index, years, fontsize=5, rotation=30)
	plt.yticks(condition_frequency, fontsize=5, rotation=30)
	plt.title('Number of Studies for years 1957-2020 for ', inp_cond)
	plt.show()

def searchTitlesByYear():
	yr =  input("Please Enter the year: ")

	for elem in year[yr]:
		print("*:",elem['Title'])
		print("\n")




def searchTitlesByCondition():
	#print("list of conditions :",condition)
	cond = input("Enter the Condition: ")

	if cond in conditions.keys():
		for elem in conditions[cond]:
			print("*:",elem['Title'])
			print("\n")
	else:
		print("Entered Condition not Found")



# def searchTitlebyYear_Condition():
# 	cond = input("Enter the Condition : ")
# 	yr = input("Enter the Year : ")

# 	if yr in year.keys() and cond in conditions.keys():
# 		for elem in conditions[cond]:
# 			print(elem['Title'])
# 			print("\n")



def main():



	#print(file_list)

	for elements in file_list:
	    xmltree = ET.parse(elements) 
	    root = xmltree.getroot()


	    
	    #Extracting title
	    for official_title in root.iter('official_title'):
	        title = official_title.text
	    if title == '':
	        for brief_title in root.iter('brief_title'):
	            title = brief_title.text
	            
	    #Extracting conditions
	    for condition in root.iter('condition'):
	        condition = condition.text
	    
	    #Extracting Status
	    for overall_status in root.iter('overall_status'):
	         status = overall_status.text
	            
	     #Extracting Detailed Description
	    for detailed_description in root.iter('detailed_description'):
	        description = detailed_description[0].text
	    
	    #Extracting the Year
	    for start_date in root.iter('start_date'):
	        date = start_date.text
	    date = date[-4:]
	    
	    if date not in year.keys():
	        year[date] = [{'Title' : title, 'Condition' : condition, 'Status' : status, 'Description' : description}]
	                      #(title, condition,status,description)]
	    else: 
	        year[date].append({'Title' : title, 'Condition' : condition, 'Status' : status, 'Description' : description})
	        #(title,condition,status,description))



	    if condition not in conditions.keys():
	        conditions[condition] = [{'Title' : title, 'Status' : status, 'Description' : description}]
	                      #(title, condition,status,description)]
	    else: 
	        conditions[condition].append({'Title' : title, 'Status' : status, 'Description' : description})
	        #(title,condition,status,description))




	years  = [y for y in year.keys()]
	years.sort()
	year_frequency = []
	for y in years:
	    year_frequency.append(len(year[y]))

	#plot_bar_x(years,year_frequency)


	# searchTitlesByYear()
	# searchTitlesByCondition()
	# searchTitlebyYear_Condition()
	#plot_year_condition(years)
	
	
	
	while True:
		print(" Enter '1' for Search for Title by Year \n Enter '2' to Search Title by Condition \n Enter '3' for Plotting Trial Frequency over Years \n Enter '4' for Plotting Frequency of Trials Realted to Specific Condition over different years \n Enter any other key to exit") 
		choice = input("Enter you choice")
		if choice == "1":
			searchTitlesByYear()
		elif choice == '2':
			searchTitlesByCondition()
		elif choice == "3":
			plot_bar_x(years,year_frequency)
		elif choice == "4":
			plot_year_condition(years)
		else:
			break


if __name__ == "__main__":
	main()
