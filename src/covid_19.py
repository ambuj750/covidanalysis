import pandas as pd
from utility import convert_to_num
from utility import get_percentage

url = 'https://www.mohfw.gov.in/'

covid_data = pd.read_html(url)

df = covid_data[0]

total_cases = 'Total Confirmed cases (Including 111 foreign Nationals)'
total_cured_cases = 'Cured/Discharged/Migrated'
total_death = 'Deaths ( more than 70% cases due to comorbidities )'
name_of_state = 'Name of State / UT'

df[total_cases] = df[total_cases].apply(lambda x: convert_to_num(x))
df[total_cured_cases] = df[total_cured_cases].apply(lambda x: convert_to_num(x))
df[total_death] = df[total_death].apply(lambda x: convert_to_num(x))

percentage = get_percentage()

more_than_given = (df[total_death]) > ((df[total_cases] / 100) * percentage)

print(f'List of all Indian state having death more than {percentage} percent :')

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df[more_than_given][name_of_state][:-1].to_string(index=False))
