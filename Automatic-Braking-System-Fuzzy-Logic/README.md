# Fuzzy Logic-Based Automatic Braking System

A Python-based educational simulation of an **Automatic Braking System (ABS)** using a **9-rule Mamdani Fuzzy Inference System (FIS)**.

> **Important:** This is an academic proof-of-concept simulation. It is **not** a certified automotive controller and must not be used to control a real vehicle.

## Project Overview

This project demonstrates how fuzzy logic can map two vehicle-situation inputs:

- **Obstacle distance, D:** 0–100 m
- **Closing speed, Vc:** 0–30 m/s

to one output:

- **Braking command, B:** 0–100%

The model uses triangular membership functions, Mamdani inference, `min` for AND/implication, `max` for aggregation, and centroid defuzzification.

## Repository Contents

```text
fuzzy-logic-automatic-braking-system/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   └── abs_fuzzy_skfuzzy.py
├── data/
│   └── test_results.csv
├── tests/
│   └── test_model.py
├── docs/
│   ├── Automatic_Braking_System_Final_Presentation.pdf
│   └── Automatic_Braking_System_Final_Presentation.pptx
└── .github/
    └── workflows/
        └── python-tests.yml
```

## Fuzzy Variables

| Variable | Type | Range | Membership functions |
|---|---|---:|---|
| Distance `D` | Input | 0–100 m | Near, Medium, Far |
| Closing speed `Vc` | Input | 0–30 m/s | Slow, Moderate, Fast |
| Braking `B` | Output | 0–100 % | Light, Moderate, Hard |

### Membership functions

**Distance**

- Near: `[0, 0, 30]`
- Medium: `[10, 40, 70]`
- Far: `[50, 100, 100]`

**Closing speed**

- Slow: `[0, 0, 10]`
- Moderate: `[5, 15, 25]`
- Fast: `[20, 30, 30]`

**Braking command**

- Light: `[0, 0, 40]`
- Moderate: `[20, 50, 80]`
- Hard: `[60, 100, 100]`

## Rule Base

| Distance \ Closing speed | Slow | Moderate | Fast |
|---|---|---|---|
| Near | Moderate | Hard | Hard |
| Medium | Light | Moderate | Hard |
| Far | Light | Light | Moderate |

The design follows the project logic that a nearer obstacle and/or higher closing speed should generally produce stronger braking.

## Mamdani Inference Process

```text
Distance + Closing Speed
          ↓
      Fuzzification
          ↓
      Rule Evaluation
          ↓
       Aggregation
          ↓
  Centroid Defuzzification
          ↓
    Braking Command (%)
```

## Example

For:

```text
Distance D = 20 m
Closing speed Vc = 15 m/s
```

the model produces approximately:

```text
Braking command = 62.4 %
```

This is a blend between the Moderate and Hard braking output sets.

## Test Results

The repository includes the 10 project test cases in `data/test_results.csv`.

| Test | D (m) | Vc (m/s) | Expected | Output |
|---:|---:|---:|---|---:|
| T01 | 5 | 25 | Hard | 84.4% |
| T02 | 10 | 10 | Hard | 84.4% |
| T03 | 15 | 5 | Moderate | 44.5% |
| T04 | 20 | 15 | Moderate–Hard | 62.4% |
| T05 | 40 | 5 | Light | 15.6% |
| T06 | 40 | 15 | Moderate | 50.0% |
| T07 | 40 | 25 | Hard | 84.4% |
| T08 | 70 | 5 | Light | 16.3% |
| T09 | 70 | 15 | Light | 16.3% |
| T10 | 90 | 28 | Moderate | 50.0% |

## Installation

Recommended Python version: **3.9+**

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Simulation

From the repository root:

```bash
python src/abs_fuzzy_skfuzzy.py
```

Expected output includes values close to:

```text
T01  D=  5 m  Vc=25 m/s  ->  84.4 %
T04  D= 20 m  Vc=15 m/s  ->  62.4 %
T10  D= 90 m  Vc=28 m/s  ->  50.0 %
```

Exact floating-point formatting can vary slightly between environments/package versions.

## Run Tests

Install pytest if it is not already included:

```bash
pip install pytest
```

Then:

```bash
pytest
```

The tests verify the project's published test cases against the current `scikit-fuzzy` implementation.

## Limitations

This model does not simulate:

- Vehicle dynamics
- Stopping distance
- Road friction
- Tyre grip
- Vehicle mass
- Brake actuator delay
- Brake dynamics
- Driver intent
- Weather or road conditions
- Real sensors or an ECU

The project presentation also notes that the simplified rule base and membership functions require engineering validation before any real-world application.

## Future Improvements

Potential future work identified by the project includes:

- Add time-to-collision and acceleration inputs
- Validate the controller against a physics-based vehicle model
- Compare with PID control
- Tune membership functions using a genetic algorithm
- Add sensor-noise filtering
- Develop a real simulator interface

## Academic Project

**Course:** Fuzzy Logic and Genetic Programming (BE05000461)  
**Department:** Automobile Engineering  
**Institute:** L.D. College of Engineering (LDCE), Ahmedabad  
**University:** Gujarat Technological University (GTU)  
**Academic project:** Problem-Based Learning (PBL)

### Team

- Darshan Kantibhai Prajapati
- Parth Sanjaybhai Parmar

See the presentation in `docs/` for the complete project material.

## References

1. L.D. College of Engineering, PBL course brief, BE05000461.
2. scikit-fuzzy documentation: https://scikit-fuzzy.github.io/scikit-fuzzy/
3. L. A. Zadeh, “Fuzzy sets,” *Information and Control*, vol. 8, no. 3, pp. 338–353, 1965.
4. E. H. Mamdani and S. Assilian, “An experiment in linguistic synthesis with a fuzzy logic controller,” *International Journal of Man-Machine Studies*, vol. 7, no. 1, pp. 1–13, 1975.
5. T. J. Ross, *Fuzzy Logic with Engineering Applications*, 4th ed., Wiley, 2016.
