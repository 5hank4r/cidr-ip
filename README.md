# Subnet to IP Address Generator

## Description
This Python script takes a list of subnets in CIDR notation and generates all possible IP addresses within each subnet. The results can be saved to a text file or displayed in the console.

## Features
- Generates all IP addresses from given subnets.
- Outputs results to both the console and a specified file.
- Handles multiple subnets in a single input file.

## Requirements
- Python 3.x
- `ipaddress` library (included with Python 3)

## Usage
1. Create a text file named `subnet.txt` containing the subnets in CIDR notation.
2. Use the following command to generate IP addresses:

   ```bash
   cat subnet.txt | python generate_ips.py | tee result.txt
