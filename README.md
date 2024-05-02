# Package Measurement Conversion

## Overview

This Measurement Conversion application allows users to input a character string and receive the output in JSON format. 
The input is processed into a list showing the total values of measured inflows. 
Accessible via a RESTful API endpoint, the application is designed with scalability and extensibility in mind, facilitating easy modifications and expansions.

## Features 
- **Sequence Input Handling:** Accepts a sequence of characters and underscores as input for conversion.
- **Efficient Conversion Algorithms:** Implements efficient algorithms for converting the input sequence into a list of measurements.
- **Clear and adaptable:** Easily modified and extended to include additional functionalities.
- **Handling Special Cases:** Handle special cases, such as, the charecter "z" which acts differently.

## Installation
- Clone the following url in your command prompt: https://github.com/Abbas-Abdulrab/PackageMeasurementConversionAPI.git

### Prerequisites
- Python 3.x
- CherryPy

### Setup
1. Clone the repository (see the Installation section above).
2. Install required Python packages from requirements.txt: 
    ```pip install -r requirements.txt```
## Usage
- Get a specific string: 

    Default: http://localhost:8080/api/sequence/<enter_string_here>
    Specific port: http://localhost:<enter_port_here>/api/sequence/<enter_string_here>

- Get history of all conversions: 

    Default: http://localhost:8080/api/sequence

    Specific port: http://localhost:<enter_port_here>/api/sequence

### Running the Program
- **Script**:

    Default: ```python main.py```
    
    Specific port: ```python main_app.py <enter_port>```
- **Access URL**: 

    Default: http://localhost:8080/
    
    Specific port: http://localhost:<enter_port>/

## Contributing
Contributions to this project are prohibited due to the course restrictions.

## License
This project is licensed under the MIT License.

## Contact
For any queries, please contact Abbas@gmail.com

## Acknowledgements
Project by Abbas Abdul Rab
