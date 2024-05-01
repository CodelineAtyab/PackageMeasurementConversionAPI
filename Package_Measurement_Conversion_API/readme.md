# Package Measurement Conversion API

This API is designed to convert measurement input strings into a list of total values of measured inflows for each package. The input strings follow a specific encoding format, where each package consists of a number indicating the count of values measured in each measurement cycle, followed by the measured values encoded using alphabetical characters.

## Pre-requisites

- Python 3.x
- CherryPy
- SQLite

## Installation

### 1. Clone the repository: 

    https://github.com/Sughiya-AlSaid/PackageMeasurementConversionAPI


### 2. Navigate to the project directory:

    cd Package_Measurement_Conversion_API

### 3. Install the required dependencies:
   
      pip install -r requirements.txt

## Running the Application

### 1. Start the server application:

      python main_app.py [port_number]

Replace `[port_number]` with the desired port number. If no port number is provided, the application will run on the default port.

### 2. The server will start, and you should see log messages indicating the application's status.

## API Usage
### 1. To view the converted alphabet input string into the corresponding list of numbers in JSON format.

The API provides a GET endpoint `/convert_measurements` that accepts a query parameter `input` containing the measurement input string.

### Example requests:

    GET /convert_measurements?input="aa"

    GET /convert_measurements?input="abbcc"

    GET /convert_measurements?input="dz_a_aazzaaa"

### 2. To view the list of total values of the parsed string and return the result in JSON format.

The API provides a GET endpoint `/conversion_results` that accepts a query parameter `input` containing the measurement input string.

### Example requests:

    GET /conversion_results?input="aa"

    GET /conversion_results?input="abbcc"

    GET /conversion_results?input="dz_a_aazzaaa"
### To retrieve the stored request history, use the following endpoint:

    GET /get_data_from_db

This endpoint will return the persisted history of all requests made to the conversion endpoint.

## Testing

The application follows the principles of Test-Driven Development (TDD). Unit tests are provided in the `test/` directory. To run the tests, execute the following command:

    python -m unittest Package_Measurement_Conversion_API/services/test/test_converter.py

## Contributing
Contributing to this project is **prohibited**.

## Acknowledgements
This project was done by **Sughiya Al Said**