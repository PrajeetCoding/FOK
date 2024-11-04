import numpy as np
import pandas as pd

# Initial information needed to get the file
date = input("What date do you want? (format = YYYY/M/D) ")
input_file = input("What is the filepath? ")

input_df = pd.read_csv(input_file)
input_df = input_df[input_df["Date"] == date]

# Empty output dataframe
columns = ["Start Date", "End Date", "Activity Name","Impact Area","Full Name","First Name","Last Name","Email","Hours","Description"]

out_data = dict.fromkeys(columns)
for key in out_data.keys():
    out_data[key] = []

#Populate output file
for index, row in input_df.iterrows():
    out_data["Start Date"].append(date)
    out_data["End Date"].append(date)
    out_data["Full Name"].append(row["First Name"] + " " + row["Last Name"])
    out_data["First Name"].append(row["First Name"])
    out_data["Last Name"].append(row["Last Name"])
    out_data["Activity Name"].append("Food Sort")
    out_data["Impact Area"].append("Food Sort")
    out_data["Email"].append(row["Email"])

    hours = row["Hours tracking"]

    out_data["Hours"].append(hours)
    
    if hours > 2:
        out_data["Description"].append("This person brought " + str(hours - 1) + " people with them")
    elif hours == 2:
        out_data["Description"].append("This person brought " + str(hours - 1) + " person with them")

    else:
        out_data["Description"].append("")


output_df = pd.DataFrame(out_data, columns=columns)
agg_dict = {"Hours": "sum"}
agg_dict.update( { x:"first" for x in columns.remove("Hours") } )

output_df = output_df.groupby('Full Name').agg(agg_dict)
output_df.to_csv(str(date) + " Food Sort ")