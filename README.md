# Package Converter API
## Overview
The Package Converter API is a web service that
provides functionality to convert package measurements
based on user input. It exposes endpoints for converting
measurements and retrieving conversion history.

## Features
- **Sequence Input Handling:** Accepts a sequence of characters and underscores as input for conversion.
- **Efficient Conversion Algorithms:** Implements efficient algorithms for converting the input sequence into a list of measurements.
- **Clear and adaptable:** Easily modified and extended to include additional functionalities.

## Installation
Clone the repository:
```
git clone https://github.com/Rudainasaleh/PackageMeasurementConversionAPI.git
```

## Install dependencies:
```
pip install -r requirements.txt
```

## Usage
- Start the server:
```python main_app.py```
- ```GET http://localhost:8080/convert_measurements?input=aa``` Convert package measurements based on user input
- ```GET http://localhost:8080/get_history``` Retrieve conversion history.

## Testing

- To run unit tests:

``` python -m unittest ./services/test/test_package_conversion.py```