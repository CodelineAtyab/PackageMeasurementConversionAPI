## Package Conversion API Overview
The Package Conversion API functions is a web-based service designed to facilitate the conversion of package measurements as per user specifications. It offers endpoints specifically for converting measurements and accessing conversion records.

## Features
- **Seamless Handling of Sequence Input:** Capable of processing sequences comprising characters and underscores, facilitating smooth conversion.
- **Optimized Conversion Algorithms:** Incorporates streamlined algorithms for the swift transformation of input sequences into lists of measurements.
- **Transparent and Flexible:** Exhibits clarity in design and is easily customizable, allowing for seamless integration of supplementary features.

## Installation
Clone the repository:
```
git clone https://github.com/aljab017/PackageMeasurementConversionAPI.git
```

## Install dependencies:
```
pip install -r requirements.txt
```

## Usage
- Start the server:  
```python main.py```
- Convert measurement:  
```GET http://127.0.0.1:8080/convert_measurements?input_str=INPUT STRING HERE``` 
- Get conversion history   
```GET http://127.0.0.1:8080/get_history``` 
## Testing

- To run tests:   
``` python -m unittest .\models\tests\measurement_converter_tests.py                            ```