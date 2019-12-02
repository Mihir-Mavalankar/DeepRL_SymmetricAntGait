**Status:** Active (under active development, breaking changes may occur)

# About the project

First, refer to the OpenAI Baselines project first as this project uses is built off it. OpenAI Baselines is a set of high-quality implementations of reinforcement learning algorithms. Refer to [OpenAI baselines](https://github.com/openai/baselines)

## Prerequisites 
Baselines requires python3 (>=3.5) with the development headers. You'll also need system packages CMake, OpenMPI and zlib. Those can be installed as follows
### Ubuntu 
    
```bash
sudo apt-get update && sudo apt-get install cmake libopenmpi-dev python3-dev zlib1g-dev
```
    
### Mac OS X
Installation of system packages on Mac requires [Homebrew](https://brew.sh). With Homebrew installed, run the following:
```bash
brew install cmake openmpi
```

## Tensorflow versions
The master branch supports Tensorflow from version 1.4 to 1.14

## Installation
- Clone the repo and create a conda environment or virtula environment in pip.
- If you don't have TensorFlow installed already, install your favourite flavor of TensorFlow. In most cases, 
    ```bash 
    pip install tensorflow-gpu # if you have a CUDA-compatible gpu and proper drivers
    ```
    or 
    ```bash
    pip install tensorflow
    ```
    should be sufficient. Refer to [TensorFlow installation guide](https://www.tensorflow.org/install/)
    for more details. 
    
- Also install gym and pytbullet using pip

- Install baselines package
    ```bash
    pip install -e .
    ```

## Training models
There are four differnt launch scripts for each model and you can just run the script from the terminal to train the models.
Use the render_ant.py to see the video for the trainied models on the Ant simulation. 
The scripts themselves ahve the command shown below and has different variables defined that you can tweak according to your requirements:
```bash
python -m baselines.run --alg=<name of the algorithm> --env=<environment_id> [additional arguments]
```
There are already agruments in place for saving and loadingg the models which can be cjhanged according to your needs.

