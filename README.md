# PaiQ
ML on a stick

Youll need to add a secret.py file with the following:

- project_ID = "found on edge impulse URL while in target project"
- API_Key = "ei_XXXfound in DashBoard/Keys in your EI project"
- deploy_type = "rp2040"
- device_ID = "found in devices in your EI project - may need to add device first"
- device_name = "DEVICENAME"
- device_type = "RASPBERRY_PI_RP2040"

## PaiQ Device Overview

The PaiQ device is a pool cue with an IMU (Inertial Measurement Unit) sensor attached. The IMU sensor collects data on the movement and orientation of the pool cue, which is then used for analysis and machine learning purposes. The PaiQ device leverages Edge Impulse for data collection, processing, and analysis.

### Components

- **Pool Cue**: The main body of the device.
- **IMU Sensor**: Attached to the pool cue to collect movement and orientation data.
- **Raspberry Pi Pico W**: Used to run the scripts and interface with Edge Impulse.
- **Edge Impulse**: A platform for developing and deploying machine learning models on edge devices.

## How PaiQ Uses Edge Impulse

The PaiQ device uses Edge Impulse to collect and analyze data from the IMU sensor. The data is sent to Edge Impulse for processing, where machine learning models can be trained and deployed to the device. The following scripts are used to interact with Edge Impulse:

- `checkIfDaemonRunning.py`: Checks if the Edge Impulse daemon is running and starts it if necessary.
- `sendData2.py`: Sends data from the IMU sensor to Edge Impulse for analysis.

## Setting Up and Using PaiQ with Edge Impulse

### Prerequisites

- A Raspberry Pi with Python installed.
- An Edge Impulse account and project set up.
- The `secret.py` file with the necessary credentials.

### Instructions

1. **Set up the Raspberry Pi Pico W**:
   - Install the required Python libraries:
     ```sh
     pip install RPi.GPIO
     pip install edge-impulse-linux
     ```

2. **Prepare the `secret.py` file**:
   - Create a `secret.py` file in the project directory with the following content:
     ```python
     project_ID = "your_project_id"
     API_Key = "your_api_key"
     deploy_type = "rp2040"
     device_ID = "your_device_id"
     device_name = "your_device_name"
     device_type = "RASPBERRY_PI_RP2040"
     ```

3. **Run the scripts**:
   - To check if the Edge Impulse daemon is running and start it if necessary, run:
     ```sh
     python3 checkIfDaemonRunning.py
     ```
   - To send data from the IMU sensor to Edge Impulse, run:
     ```sh
     python3 SendData.py
     ```
   - Alternatively, you can use the `sendData2.py` script to send data:
     ```sh
     python3 sendData2.py
     ```

## Running Unit Tests

To run the unit tests, follow these steps:

1. Install the `pytest` framework if you haven't already:

```sh
pip install pytest
```

2. Navigate to the root directory of the project.

3. Run the unit tests using the following command:

```sh
pytest
```

This will automatically discover and run all the unit tests in the `tests` directory.
