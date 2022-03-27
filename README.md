# Election Results
## Overview of Project
### Purpose
The Colorado Board of Elections need to complete an audit from a large amount of data including the vote counts for candidates in multiple counties.  The coding needs to be very user friendly to non-technical individuals and present information such as, total numbers of votes, list of candidates, number of votes for each candidate and the percentage of votes in a text file. This file should also include number and percentage of voters in each county, county with the highest turnout, and the winner of the election by popular vote. Creating an easy-to-follow code and presentation of important information ensures that the file can be used in future elections to provide the same results.
## Analysis
### Election Audit Results
![Election Results](https://user-images.githubusercontent.com/100329223/160261681-86b11c7a-2cd6-4dec-ab99-bc0e098ff0e7.png)
- How many votes were cast in this congressional election?

In this election, there were a total of 369,711 voters. The following image shows how our code generated this number from the provided election results csv file. By creating a for loop through the rows, after establishing a header row and setting the total votes count to zero, we created a counter to add the number rows.
![Total votes code](https://user-images.githubusercontent.com/100329223/160261689-17aa37ff-b9fe-413f-90cb-4074e7363447.png)
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

Continuing on the for loop initiated before the total votes counter, we established the column to cycle through for county names in column 1. Our second if statement (line 67) cycles through the data and creates a list of all the counties (line 70) and sets the number of counties to zero so they aren’t all combined into one total (line 73). Line 76 begins the counter and every time a county is present, a tally is added to their total. In line 93, a new for loop pulls the information of each county from the dictionary (established on line 22). On line 96 the code asks for the total votes cast in each county. The county vote percentage is then calculated in line 98 by taking the total votes cast in a county and dividing it by the total votes in the election and multiplying that by 100. In order to complete the equation county votes and the total votes were established as floats because different variable types cannot be divided by each other.
- Which county had the largest number of votes?

In order to figure out the largest number of votes we will nest an if statement within the for loop determining the votes per county. The statement in line 108 will cycle through the county votes totals until the statement is true that county vote count is the largest value. In this case the county with the largest turnout would be Denver.
![highest county](https://user-images.githubusercontent.com/100329223/160261951-b27e6f96-99a6-47b9-8fe5-3ce05b9838c6.png)

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

Additionally, in the for loop initiated before the total votes counter, we established the column to cycle through for candidate names in column 2. The if statement cycles through the data and creates a list of all the candidates (line 57) and sets the number of candidates votes to zero so they aren’t all combined into one total (line 60). Line 63 begins the counter and every time the candidate’s name is present on the list a vote is added to their total. In line 122, a new for loop pulls the information of each candidate from the dictionary (established on line 18). On line 125 the code asks for the total votes received by a given candidate. The vote percentage is then calculated in line 126 by taking the total votes for a given candidate and dividing it by the total votes in the election and multiplying that by 100.
![vote counts](https://user-images.githubusercontent.com/100329223/160261766-3e8a71e2-8f97-4793-83ec-f7f439df019c.png)
![county percent](https://user-images.githubusercontent.com/100329223/160261849-8a40c95f-19a8-4fa8-b82e-2ca96af343eb.png)
![candidate percentage](https://user-images.githubusercontent.com/100329223/160261854-c1e54ca1-c902-48ae-87e5-9b0260b6883f.png)
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

A nested if statement in the for loop pertaining to the candidate vote counts determines the winner on line 137. Much like determining the county with the most votes, this statement cycles through the votes until it find the candidate with the largest votes and the largest percentage.  In this election, the winner of the election is Diana DeGette with 272,892 votes which is 73.8% of the total votes.
![winning candidate](https://user-images.githubusercontent.com/100329223/160261887-44da80e9-12a8-4f4b-a940-b86bcd1fab73.png)
### Election Audit Summary
This script would be very useful in future elections for anyone with basic knowledge of coding or the capability to interpret pseudo coding. Slight modifications can be made to variable names, print scripts, and variable definition (i.e. integer, floats, Booleans). If there were more data points to be considered in the provided data, such as term limitation (yes or no), we could add another if statement below row 41 and follow the same formatting as the candidate and county vote tabulations. If someone wanted to, they could insert more nested loops to determine the votes per candidate per county to see if there is a part of the state that tends to lean more in favor of a certain type of candidate. With the easy printing of information to a text file, this could be a very useful tool for quick election results and avoiding human error in calculations.
