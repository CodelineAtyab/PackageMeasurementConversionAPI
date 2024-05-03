# Package Measurement Conversion

## Overview
This Measurement Conversion application enables users to input a string of characters, and receive the output in a JSON format. The inputted string will be transformed  into a list of the total values of measured inflows. The application can be accessed through the RESTful API endpoint. The application is constructed with scalability and extensibility in focus, allowing for modifications and expansions.

## Features 
- **Sequence Input Handling:** Accepts a sequence of characters and underscores as input for conversion.
- **Efficient Conversion Algorithms:** Implements efficient algorithms for converting the input sequence into a list of measurements.
- **Clear and adaptable:** Easily modified and extended to include additional functionalities.

## Installation
- Clone the following url in your command prompt: https://github.com/sarah-alshukaily/PackageMeasurementConversionAPI.git

### Prerequisites
- Python 3.x
- CherryPy

### Setup
1. Clone the repository (see the Installation section above).
2. Install required Python packages from requirements.txt: 
    ```pip install -r requirements.txt```
## Usage
- Get a specific string: 

    Default: http://localhost:8080/convert?user_input=<enter_string_here> 
    Specific port: http://localhost:<enter_port>/convert?user_input=<enter_string_here>

- Get history of all conversions: 

    Default: http://localhost:8080/get_history
    Specific port: http://localhost:<enter_port>/get_history

### Running the Program
- **Script**:

    Default: ```python main_app.py```
    
    Specific port: ```python main_app.py <enter_port>```
- **Access URL**: 

    Default: http://localhost:8080/
    
    Specific port: http://localhost:<enter_port>/

## Contributing
Contributions to this project are prohibited due to the course restrictions.

## License
This project is licensed under the MIT License.

## Contact
For any queries, please contact sara@gmail.com

## Acknowledgements
Project by Sara Al Shukaili