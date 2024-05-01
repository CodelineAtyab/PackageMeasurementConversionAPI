# Package Measurement Conversion API

## Introduction

This API converts measurement input strings into a list of total values of measured inflows for each package. It follows a specific encoding format where a number represents the count of values measured in each cycle, followed by measured values encoded using alphabetical characters ('a' for 1, 'b' for 2, and so on).

### Algorithm Summary

- Each character in the input sequence corresponds to a specific value.
- The algorithm processes the input sequence character by character.
- Special cases, such as 'z', are handled where a single character may represent multiple characters.
- The algorithm calculates the sum of values based on specific rules for each character.
- The sequence restarts after each calculation until the end of the input sequence is reached.

## Operation

1. Start with the first character in the input sequence.
2. Determine the value of the character based on predefined rules.
3. If a special case like 'z' is encountered, treat it and the following characters as a single continuous character.
4. Calculate the sum of values for a specified number of characters after the current character.
5. Repeat the process until the end of the input sequence is reached.

## Examples

1. **Input:** abbcc
   - **Response:** [2, 6]
   - **Explanation:**
     - 'a' -> 1
     - 'b' -> 2 (consider 2 characters after 'b': 'c', 'c')
     - 'c' -> 3 (consider 2 characters after 'c': 'c')
     - Sum: 2 + 6 = 8

2. **Input:** abcdabcdab
   - **Response:** [2, 7, 7]
   - **Explanation:**
     - 'a' -> 1
     - 'b' -> 2 (consider 2 characters after 'b': 'c', 'd')
     - 'c' -> 3 (consider 3 characters after 'c': 'd', 'a', 'b')
     - 'd' -> 4
     - Sum: 2 + 7 + 7 = 16

3. **Input:** dz_a_aazzaaa
   - **Response:** [28, 53, 1]
   - **Explanation:** (Include the detailed explanation of the 'z' case here)

4. **Input:** zd_aaaaaaaaaabaaaaaaaabaaaaaaaabbaa
   - **Response:** [34]
   - **Explanation:** (Include the detailed explanation of the 'z' case here)

This algorithm effectively encodes or decodes input sequences by assigning values to characters and summing them according to specified rules, providing a concise representation of the sequence.


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

1. Execute the test cases in the following:

``` python -m unittest .\tests\test_sequence_processor.py 


License
This project is licensed under the MIT License - see the LICENSE file for details.
