# PaiQ
ML on a stick

Youll need to add a secret.py file with the following:

- project_ID = "found on edge impulse URL while in target project"
- API_Key = "ei_XXXfound in DashBoard/Keys in your EI project"
- deploy_type = "rp2040"
- device_ID = "found in devices in your EI project - may need to add device first"
- device_name = "DEVICENAME"
- device_type = "RASPBERRY_PI_RP2040"

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
