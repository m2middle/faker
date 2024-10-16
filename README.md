# GenerateUser

The `generateuser.py` script uses the Python Faker library to generate realistic user data. It is designed to create fictitious data sets, such as names, email addresses, job titles and departments, to simulate a corporate environment.

## Features

Generation of user data such as:
- Full name
- Professional email address
- Position and department
- Telephone number

Production of `.csv` files suitable for mass import into identity management services such as Microsoft Entra ID.

Easily customized to meet specific data simulation needs.

## Prerequisites

- Python 3.x

## Installation

Clone the repository: `git clone https://github.com/m2middle/faker.git`

Navigate to the project directory: `cd faker`

Create a virtual environment: `python -m venv env`

Activate the virtual environment:
- On Windows: `.\env\Scripts\activate`
- On macOS and Linux: `source env/bin/activate`

Install the required dependencies: `pip install -r requirements.txt`

Run the script to generate user data: `python generateuser.py`

## Customization

The `generateuser.py` script can be easily modified to generate different types of data or to adjust the output formats. Refer to the [Faker documentation](https://faker.readthedocs.io/en/master/) for more information on available options.

## Extra

If you want also to proceed a bulk deletion of the users by providing a CSV file with the Azure specifications, run the deleteuser.py script following the same process as the generateuser.py

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss the changes you would like to make.
