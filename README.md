# Rossmann-store-sales
## Project Overview

This project aims to predict the daily sales of Rossmann stores using historical sales data and various features such as promotions, holidays, and store characteristics. The dataset includes sales information across multiple stores, covering a wide range of dates, and the analysis is conducted using time series techniques, feature engineering, and machine learning models.

## Table of Contents
1. [Project Structure](#project-structure)
2. [Features](#features)
3. [Installation](#installation)
4. [Data Preprocessing](#data-preprocessing)
5. [Modeling](#modeling)
6. [Evaluation](#evaluation)
7. [Results](#results)
8. [Contributing](#contributing)

## Project Structure

## Features

The dataset contains the following key features:
- **Store**: Unique identifier for each store.
- **Date**: The date of the sales.
- **Sales**: The total sales for a particular store on a given day.
- **Customers**: Number of customers on that day.
- **Open**: Whether the store was open (1) or closed (0).
- **Promo**: Whether the store was running a promotion on that day.
- **StateHoliday**: Indicator if the day is a state holiday.
- **SchoolHoliday**: Indicator if the store was affected by a school holiday.

### Engineered Features:
- **Year**: Year extracted from the `Date` column.
- **Month**: Month extracted from the `Date` column.
- **Day**: Day extracted from the `Date` column.
- **Weekday**: Day of the week extracted from the `Date` column.

## Installation

To run this project, you need to have Python installed, along with the necessary libraries specified in the `requirements.txt` file. Follow these steps to set up the environment:

1. Clone this repository:
```bash
   git clone https://github.com/olaniSiyum/Rossmann-store-sales.git
   cd rossmann-store-sales
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
3. Set up a virtual environment for isolated package management:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. EDA


