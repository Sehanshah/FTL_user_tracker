
# FTL User Activity Tracker

A simple python django based application that stores basic user info and the activity of the user

To run the application in local,
1. Install python3 
2. Open cmd or Terminal in the Project Root Folder and type the command 
	> pip install virtualenv
	
   If already found ignore this step
3. Create a virtual environment to run the project by running the command,
	  >virtualenv venv
4. After creating venv, A folder named **venv** will be created in Project Directory
5. Windows users , In cmd type, 
	>venv\Scripts\activate
   
   Linux Users, In Terminal type,
	>source venv\bin\activate
6. You will find (venv) at the start of the prompt if it's activated
7. Install the dependencies by running the following command,
	>pip install -r requirements.txt
8. After Installation, To start the server Run
	>python manage.py runserver

# Features and Usage
This path **/users_list/** provides all the data  available in the system

Example Response
<pre>
{
	"ok": true,
	"members": [{
			"id": "W012A3CDE",
			"real_name": "Egon Spengler",
			"tz": "America/Los_Angeles",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		},
		{
			"id": "W07QCRPA4",
			"real_name": "Glinda Southgood",
			"tz": "Asia/Kolkata",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		}
	]
}
</pre>


## Update DB with dummy data

To update the database with dummy data, Activate the virtual environment and run the following command
  >python manage.py generate_data --user_count <user_count>  --max_activity_entries <maximum_activity_entry_count>

Here,
 **user_count** is the number of users 
 **maximum_activity_entry_count** is the maximum number of entry of user activity in DB
 For example,
  If 5 is given random number from 0 to 5 will be taken, and that much activity period entries will be added for that particular user
