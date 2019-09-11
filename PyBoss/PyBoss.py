import pandas as pd
import csv

# variable with the State and abbreviation
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# defining my conversion function
def Data_Conversion():
    #setting my path to the csv file
    csv_path = ("employee_data.csv")
    with open (csv_path, newline='') as csv_file:
        csvreader = csv.reader(csv_file, delimiter = ',')
        csvheader = next(csv_file)
        # defining my empty list to hold each column
        emp_id =[]
        names = []
        DOB = []
        formated_DOB = []
        SSN = []
        formatted_ssn = []
        State = []
        formatted_State = []

        # looping through row in my csv file
        for row in csvreader :
            emp_id.append(row[0])
            names.append(row[1])
            DOB.append(row[2])
            SSN.append(row[3])
            State.append(row[4])
        # Splitting my Name column into two columns FirstName, and LastName
        firstName = [N.split()[0] for N in names]
        lastName = [N.split()[1] for N in names]
        # looping through my DOB and formatting it
        for d in DOB:
            d = d.split("-")
            d = f"{d[1]}/{d[2]}/{d[0]}"    
            formated_DOB.append(d)
        # lopping through SSN and formatting it
        for s in SSN:
            s = s.split("-")
            s = f"***-**-{s[2]}"
            formatted_ssn.append(s)
        # looping through my state column, and formatting it to state abbreviations
        for st in State:
            for k, v in us_state_abbrev.items():
                if k == st:
                    st = v
            formatted_State.append(st)
        # Creating new formatted table using Pandas dataframe.
        new_headers = ["Emp_id", "FirstName", "LastName", "DOB", "SSN", "State"]
        data = [emp_id, firstName, lastName, formated_DOB, formatted_ssn, formatted_State]
        new_emplyee = dict(zip(new_headers, data))
        df = pd.DataFrame(new_emplyee)
        print (df.dtypes)
     
Data_Conversion()
