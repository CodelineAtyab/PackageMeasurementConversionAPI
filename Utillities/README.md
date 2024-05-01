# Package Measurement Conversion API

## Introduction

This API converts measurement input strings into a list of total values of measured inflows for each package. It follows a specific encoding format where a number represents the count of values measured in each cycle, followed by measured values encoded using alphabetical characters ('a' for 1, 'b' for 2, and so on).

### Explanation of the 'z' Case:

In the encoding format, the letter 'z' represents a value greater than 26. When 'z' is encountered in the input string, it indicates that the following sequence of characters represents a value greater than 26. The characters following 'z' are added together until a non-'z' character is encountered. For example, 'zz' represents 26 + 26 = 52, and 'zzaa' represents 26 + 26 + 1 + 1 = 54.

## Prerequisites

- Python 3.x
- CherryPy

## Installation

1. Clone the repository to your local machine:

git clone https://github.com/jnulia/PackageMeasurementConversionAPI.git


2. Install dependencies:

pip install -r requirements.txt


## Running the Application

1. Navigate to the project directory.
2. Run the main application file with Python:

python main_app.py


You can specify a custom port using the --port argument:

python main_app.py --port <port-number>


## API Usage

### Conversion Endpoint

- **Endpoint:** /convert-measurements
- **Method:** GET
- **Query Parameter:**
- input: Measurement input string
- **Response:** JSON array containing the total values of measured inflows for each package

#### Example Usage:

Assuming the API is running locally on http://localhost:8080:

1. Convert measurements:

GET http://localhost:8080/convert-measurements?input=dz_a_aazzaaa


**Response:**

[28, 53, 1]


### History Endpoint

- **Endpoint:** /get-history
- **Method:** GET
- **Response:** JSON array containing the history of all data from requests

#### Example Usage:

Assuming the API is running locally on http://localhost:8080:

2. Retrieve history:

GET http://localhost:8080/get-history


**Response:**
[
{
"sequence": "dz_a_aazzaaa",
"compressed_values": [28, 53, 1],
"timestamp": "2024-04-29 12:00:00"
},
...
]


## Testing

1. Execute the following test cases:

```python
print(pmc("dz_a_aazzaaa"))  # Output: [28, 53, 1]
print(pmc("za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa"))  # Output: [40, 1]
print(pmc("aa"))  # Output: [1]
print(pmc("abbcc"))  # Output: [2, 6]
print(pmc("a_"))  # Output: [0]
print(pmc("abcdabcdab"))  # Output: [2, 7, 7]
print(pmc("abcdabcdab_"))  # Output: [2, 7, 7, 0]
print(pmc("zdaaaaaaaabaaaaaaaabaaaaaaaabbaa"))  # Output: [34]
print(pmc("za_a_a_a_a_a_a_a_a_a_a_a_a_azaaa"))  # Output: [40, 1]
print(pmc("zza_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_a_"))  # Output: [26]


License
This project is licensed under the MIT License - see the LICENSE file for details.
