# Electrical Measurement Code Repository

Welcome to the Electrical Measurement Code Repository! This repository contains a collection of codes designed to facilitate the automation of electrical measurements using source-measure units. The codes were developed to simplify measurement procedures and enhance efficiency in various measurement tasks. They have been thoroughly tested on Keithley 2400 and Keithley 2450 instruments utilizing the GPIB communication mode.

## Contents

- [Device Discovery Code](./SEARCH.py/): This code allows you to discover available measurement devices connected via GPIB and provides information about them.

- [IV Curve Measurement Code](./I-V.py/): Use this code to perform I-V (current-voltage) curve measurements on connected devices, helping you analyze their characteristics.

- [VI Curve Measurement Code](./V-I.py/): The V-I (voltage-current) curve measurement code enables you to carry out voltage-current curve measurements for detailed analysis.


## Getting Started

To get started with automating your electrical measurements using the provided codes, follow these steps:

1. Install the [NI-VISA package](https://www.ni.com/en/support/downloads/drivers/download.ni-visa.html#484351) to enable communication with the measurement instruments.

2. Install Python on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

3. Install the required Python libraries by running:
pip install -r requirements.txt


4. Run the `SEARCH.py` code to discover available measurement devices and copy the address of the instrument you intend to use.

5. Depending on the type of measurement you want to perform:
- For I-V (current-voltage) measurements, open the [I-V.py](./I-V.py/) file and insert the copied instrument address. Configure the measurement mode (RSEN variable), maximum voltage, maximum protection current, and number of measurements.
- For V-I (voltage-current) measurements, open the [V-I.py](./V-I.py/) file and insert the copied instrument address. Set the measurement mode (RSEN variable), maximum current, maximum protection voltage,
and number of measurements (in progress)

6. Execute the desired code (`I-V.py` or `V-I.py`) to automate your electrical measurements.

## Contributing

We welcome contributions from the community. If you have improvements, bug fixes, or new measurement codes to add, please feel free to submit a pull request. Make sure to follow our [Contribution Guidelines](CONTRIBUTING.md) for a smooth collaboration.

## License

This repository is licensed under the [MIT License](LICENSE), which means you can freely use and modify the code, but kindly provide attribution.

## Contact

If you have any questions or suggestions, feel free to contact me!

Happy measuring!
