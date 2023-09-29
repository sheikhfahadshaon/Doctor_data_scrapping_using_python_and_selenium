import os
import pandas as pd
from selenium import webdriver

#Take the required information
Available_location = ['Dhaka', 'Chittagong', 'Rajshahi', 'Sylhet', 'Rangpur', 'Khulna', 'Barisal', 'Mymensingh', 'Pabna', 'Bogra', 'Comilla', 'Narayanganj', 'Kushtia']
Available_dept = ['Cancer', 'Cardiology', 'Infertility', 'Eye', 'Medicine', 'Orthopedic']
print(f'Available departments: {Available_dept}')
department = input("Enter the department of the doctor to find: ")
department.lower()
print(f'Available Locations: {Available_location}')
location = input("Enter the location from where you want to get the doctor data: ")
location.lower()

#Settings to 
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


os.environ['PATH'] += r"C:/SeleniumChromeDriver"

driver = webdriver.Chrome(options=options)


# URL of the website to scrape
url = f'https://www.doctorbangladesh.com/{department}-specialist-{location}/'

# Open the website
driver.get(url)

# Initialize lists to store scraped data
doctor_names = []
workplaces = []

# Find all the doctor elements using a different method
doctor_elements = driver.find_elements('xpath', '//li[contains(@class, "doctor")]')

# Loop through each doctor element and extract data
for doctor_element in doctor_elements:
    # Extract doctor name and workplace
    name_element = doctor_element.find_element('xpath', './/h3[@class="title"]/a')
    workplace_element = doctor_element.find_element('xpath', './/li[@title="Workplace"]')

    doctor_name = name_element.text
    workplace = workplace_element.text

    # Append data to lists
    doctor_names.append(doctor_name)
    workplaces.append(workplace)

# Create a DataFrame from the scraped data
data = {'Doctor Name': doctor_names, 'Workplace': workplaces}
df = pd.DataFrame(data)

# Save the data to an Excel file
file_name = f'{department}_{location}_doctor_data.xlsx'
df.to_excel(file_name, index=False)

# Close the Chrome WebDriver
driver.quit()
