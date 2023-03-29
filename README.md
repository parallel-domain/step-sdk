# Parallel Domain Python Step and Stream SDK

The Parallel Domain Python Step and Stream SDK provides convenient
access to the Parallel Domain Image Generator API from Python
applications.
It provides utilities to simplify common tasks such as
constructing the world state,
communicating with a Step or Stream server,
and querying the server for rendered sensor data.


## Documentation

See the [Parallel Domain Portal](https://app.paralleldomain.com/docs)
for detailed documentation.


## Installation

### From Github

You can install the SDK as a library directly from Github:

```shell
pip install git+ssh://git@github.com/parallel-domain/pd-api-py.git
```

### From Source

To run or modify the examples, clone this repo and install from source:
```shell
git clone git@github.com:parallel-domain/pd-api-py.git
cd pd-api-py
pip install .
```

If running in a GUI environment, you may also want to install dependencies for visualization with:
```shell
pip install .[visualization]
```

### Docker

You can also run the examples via the included docker environment.
To build the docker image, run:
```shell
docker build -t pd-api-py .
```
The source code will be available in `/app` inside the container. Run examples like so:
```shell
docker run --rm -it --net host pd-api-py python /app/examples/step/hello_world.py
```

### Requirements

* Python 3.8+
* `libgl1-mesa-glx` on Linux (required by OpenCV2 GUI functions)


## Usage

### Hello World Example (Step Mode)

The Hello World example demonstrates how to use Step Mode to render
sensor data for a simulation loop.
First, ensure you have the following environment variables set.
```shell
ORG='<my org name>'
STEP_API_KEY='<my api key>'
CLIENT_CERT='<path to pem file>'
```
Then run the Hello World example as follows.
```shell
python ./examples/step/hello_world.py \
    --org $ORG \
    --apikey $STEP_API_KEY \
    --client-cert-file $CLIENT_CERT_FILE \
    --ig <ig name>
```
Here `<ig name>` refers to the name of your Step IG server instance.
This name is found at the end of the `self_url` parameter.
For example, the name of a Step IG with the server url
`"self_url": "https://step-api.paralleldomain.com/v1/step/org/ig/abcdefgh"` is `abcdefgh`.


By default, the Hello World example uses the level `SF_6thAndMission_medium v2.0.1`.
If you do not have access to this level, pass the `--location <name> <version>` option to select a different level.
For example, if you have access to the level `SJ_EssexAndBradford v2.1.4`, then your command will look as follows.
```shell
python ./examples/step/hello_world.py \
    --org $ORG \
    --apikey $STEP_API_KEY \
    --client-cert-file $CLIENT_CERT \
    --ig <ig name> \
    --location SJ_EssexAndBradford v2.1.4
```


See the [Step Management API documentation](https://app.paralleldomain.com/docs/step-mode-management-api)
for instructions on provisioning a Step server instance.
