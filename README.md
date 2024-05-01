# Package Measurement Conversion API

This API is designed to convert measurement input strings into a list of total values of measured inflows for each package. The input strings follow a specific encoding format, where each package consists of a number indicating the count of values measured in each measurement cycle, followed by the measured values encoded using alphabetical characters.

## Pre-requisites

- Python 3.x
- CherryPy
- SQLite

## Installation

### 1. Clone the repository: 

    https://github.com/HaithamAlMaamari/PackageMeasurementConversionAPI.git


### 2. Navigate to the project directory:

    cd Package_Measurement_Conversion_API

### 3. Install the required dependencies:
   
      pip install python
      pip install pycharm
      pip install sqlite3

## Running the Application

### 1. Start the server application:

      python main_app.py 

### 2. The server will start, and you will see a status message.

## API Usage
### 1. To view the converted alphabet input string into the corresponding list of numbers in JSON format.

   

### Example requests:

    http://localhost:8888/convert_measurements/abbcc

    http://localhost:8888/convert_measurements/aa

### To retrieve the stored request history, use the following endpoint:

    GET /get_data_from_db

This endpoint will return the persisted history of all requests made to the conversion endpoint.

## Contributing
Contributing to this project is prohibited due to Course Restrictions.