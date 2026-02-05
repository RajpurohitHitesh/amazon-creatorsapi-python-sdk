[![PyPI](https://img.shields.io/pypi/v/amazon-creatorsapi-python-sdk?color=%231182C2&label=PyPI)](https://pypi.org/project/amazon-creatorsapi-python-sdk/)
[![Python](https://img.shields.io/badge/Python->3.9-%23FFD140)](https://www.python.org/)
[![Amazon API](https://img.shields.io/badge/Amazon%20CreatorsAPI-%23FD9B15)](https://affiliate-program.amazon.in/creatorsapi/docs/en-us/introduction)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/amazon-creatorsapi-python-sdk?label=Installs)](https://pypi.org/project/amazon-creatorsapi-python-sdk/)
![Static Badge](https://img.shields.io/badge/License-Apache_2.0-blue)
[![Python application](https://github.com/RajpurohitHitesh/amazon-creatorsapi-python-sdk/actions/workflows/python-app.yml/badge.svg)](https://github.com/RajpurohitHitesh/amazon-creatorsapi-python-sdk/actions/workflows/python-app.yml)
[![Python Package using Conda](https://github.com/RajpurohitHitesh/amazon-creatorsapi-python-sdk/actions/workflows/python-package-conda.yml/badge.svg)](https://github.com/RajpurohitHitesh/amazon-creatorsapi-python-sdk/actions/workflows/python-package-conda.yml)
[![Python package](https://github.com/RajpurohitHitesh/amazon-creatorsapi-python-sdk/actions/workflows/python-package.yml/badge.svg)](https://github.com/RajpurohitHitesh/amazon-creatorsapi-python-sdk/actions/workflows/python-package.yml)

# Creators API Python SDK Example

## Prerequisites

### Python Version Support
- **Supported**: To run the SDK you need Python version 3.7 or higher.

## Setup Instructions

### 1. Install and Configure Python

For Python installation, you can download it from the official website: https://www.python.org/downloads/

```bash
# Check Python version 
python3 --version  
```

### 3. Install Dependencies
```bash
cd {path_to_dir}/creatorsapi-python-sdk
# Install package dependencies
pip3 install -r requirements.txt
```

### 4. Run Sample Code
Navigate to the examples directory to run the samples.

```bash
cd examples
```

Before running the samples, you'll need to configure your API credentials in the sample files by replacing the following placeholders:

- `<YOUR CREDENTIAL ID>` - Your API credential ID
- `<YOUR CREDENTIAL SECRET>` - Your API credential secret  
- `<YOUR CREDENTIAL VERSION>` - Your credential version (e.g., "2.1" for NA, "2.2" for EU, "2.3" for FE region)
- `<YOUR MARKETPLACE>` - Your marketplace to which you want to send the request (e.g., "www.amazon.com" for US marketplace)
- `<YOUR PARTNER TAG>` - Your Partner Tag for the requested marketplace in applicable sample code snippet files

Run the following commands to run the sample files:

**Get detailed product information:**
```bash
python3 sample_get_items.py
```

**Search for products:**
```bash
python3 sample_search_items.py
```

#### Other Samples
Check the `examples` directory for additional sample files with various API operations.
