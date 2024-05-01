# Package Measurement Conversion

## Overview
This application exposes a RESTful API endpoint that accepts a masurement input as string of characters, and returns a response of a list of total values of measured inflows.

## Features 
- **Package Measurement Conversion:** Accepts a sequence of characters and returns a result list of measured inflows.
- **Clear and adaptable:** Easily modified and extended to include additional functionalities.

## Installation
- Clone the following url in your command prompt: https://github.com/ziyadabd/PackageMeasurementConversionAPI.git

### Prerequisites
- Python 3.x
- CherryPy

### Setup
1. Clone the repository (see the Installation section above).
2. Install CherryPy package: 
    ```pip install CherryPy==18.9.0```

### Running the Program
- **Script**:

    Default: ```python main_app.py```
    
    Specific port: ```python main_app.py <enter_port>```

### Usage
- Call the API using the following URLs: 

    http://localhost:8080/?convert_measurements=<enter_string_here> 


- Get history of all conversions: 

    Default: http://localhost:8080/get_history

## Contributing
Contributions to this project are prohibited due to the course restrictions.

## License
This project is licensed under the MIT License.

## Contact
For any queries, please contact ziyadalhashar@gmail.com

## Acknowledgements
Project by Ziyad Al Hashar