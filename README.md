# Design and Development of a Fuzzy Logic-Based Automatic Braking System

## Project Overview

This project explores an educational automatic braking simulation using a Mamdani Fuzzy Inference System (FIS). The controller estimates a braking command from obstacle distance and relative closing speed.

**Academic details**
- Institute: L.D. College of Engineering, Ahmedabad
- University: Gujarat Technological University (GTU)
- Department: Automobile Engineering
- Subject: Fuzzy Logic and Genetic Programming
- Subject Code: BE05000461
- Project type: Problem-Based Learning (PBL)

## Team

- Darshan Kantibhai Prajapati
- Parth Sanjaybhai Parmar

## Objectives

- Define fuzzy input and output variables.
- Design membership functions and a fuzzy rule base.
- Implement a Mamdani FIS using Python and `scikit-fuzzy`.
- Evaluate the controller using multiple input combinations.
- Discuss the model's limitations and potential improvements.

## Inputs and Output

| Variable | Range | Unit |
|---|---:|---|
| Obstacle distance | 0–100 | m |
| Relative closing speed | 0–30 | m/s |
| Braking command | 0–100 | % |

## Technology Stack

- Python
- NumPy
- scikit-fuzzy
- Matplotlib (if used for plots)

## Project Structure

- `abs_fuzzy_skfuzzy.py` — Fuzzy controller source code
- `test_results.csv` — Test-result data
- `docs/` — Project report and presentation
- `screenshots/` — Genuine simulation screenshots
- `requirements.txt` — Python dependencies

## Setup and Execution

1. Install Python 3.
2. Install the dependencies listed in `requirements.txt`.
3. Run the controller using the command specified in the project instructions.
4. Compare the output with the documented test cases.

## Current Status

Educational simulation project. Numerical outputs, execution status, and screenshots should be treated as verified only after testing the submitted implementation.

## Limitations

This is a simplified software simulation. It is not a certified automotive braking controller and must not be used to control a real vehicle.

## Academic Use

Developed for academic learning and demonstration as part of the GTU PBL subject.
