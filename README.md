# Checkout_System

At the local Farmer’s Market Chai, Apple, Coffee, Milk and Oatmeal sold every week. This week, to celebrate one year anniversary few special offers are made. Following are the offers:
1. BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)
2. APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.
3. CHMK -- Purchase a box of Chai and get milk free. (Limit 1)
4. APOM -- Purchase a bag of Oatmeal and get 50% off a bag of Apples

The task is to implement a checkout system such that fulfills the above requirements.
At any given time, it should be able to print out the current register to see the state of the basket and include price and applied discounts, if any.

## Prerequisites

You will need Python version 2.7 or greater to be installed on your system.
You can download and install from following link.

https://www.python.org/download/releases/2.7/

You will need Docker for containerization. Windows user can download it from here:
https://docs.docker.com/toolbox/toolbox_install_windows/


## Optional requirement

To run this program I have used PyCharm Community Edition 2016 IDE on Windows. However, you can run this program by using any other IDE or from command line.

## Running the Program

To run this program from windows command prompt, enter the following command:

python checkout_system.py

To run this program on IDE look for their instructions.

## Running Test cases:

To run these test cases on windows command prompt, enter the following command

Python test_checkout_system.py

## Containerization using Docker

First of all copy the Dockerfile above in your current directory. Then navigate to working directory in Docker command line interface. 
Enter following command to build project.

docker build -t checkout .

Here checkout is tag of dockerfile. Now to run this project enter following command:

docker run --name=challenge -t -i checkout python checkout_system.py

Make sure all above files are in same folder. By default Docker uses the json-file driver to record containers logs.
You can get this location by running:

docker inspect --format='{{.LogPath}}' challenge

Here challenge is the name of container.


## Author
Aditya Dubal
