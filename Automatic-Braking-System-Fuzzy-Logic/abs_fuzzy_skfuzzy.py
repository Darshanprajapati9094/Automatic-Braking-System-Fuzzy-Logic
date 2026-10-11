"""Fuzzy Logic-Based Automatic Braking System (Mamdani FIS) - scikit-fuzzy
GTU BE05000461 | Automobile Engineering | LDCE, Ahmedabad
Educational simulation only - not a certified automotive controller."""
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

dist  = ctrl.Antecedent(np.arange(0, 101, 1), 'distance')       # m
speed = ctrl.Antecedent(np.arange(0, 31, 1),  'closing_speed')  # m/s
brake = ctrl.Consequent(np.arange(0, 101, 1), 'brake')          # %  (centroid default)

dist['Near']   = fuzz.trimf(dist.universe,  [0, 0, 30])
dist['Medium'] = fuzz.trimf(dist.universe,  [10, 40, 70])
dist['Far']    = fuzz.trimf(dist.universe,  [50, 100, 100])
speed['Slow']     = fuzz.trimf(speed.universe, [0, 0, 10])
speed['Moderate'] = fuzz.trimf(speed.universe, [5, 15, 25])
speed['Fast']     = fuzz.trimf(speed.universe, [20, 30, 30])
brake['Light']    = fuzz.trimf(brake.universe, [0, 0, 40])
brake['Moderate'] = fuzz.trimf(brake.universe, [20, 50, 80])
brake['Hard']     = fuzz.trimf(brake.universe, [60, 100, 100])

rules = [
 ctrl.Rule(dist['Near']   & speed['Slow'],     brake['Moderate']),  # R1
 ctrl.Rule(dist['Near']   & speed['Moderate'], brake['Hard']),      # R2
 ctrl.Rule(dist['Near']   & speed['Fast'],     brake['Hard']),      # R3
 ctrl.Rule(dist['Medium'] & speed['Slow'],     brake['Light']),     # R4
 ctrl.Rule(dist['Medium'] & speed['Moderate'], brake['Moderate']), # R5
 ctrl.Rule(dist['Medium'] & speed['Fast'],     brake['Hard']),      # R6
 ctrl.Rule(dist['Far']    & speed['Slow'],     brake['Light']),     # R7
 ctrl.Rule(dist['Far']    & speed['Moderate'], brake['Light']),     # R8
 ctrl.Rule(dist['Far']    & speed['Fast'],     brake['Moderate']),  # R9
]
system = ctrl.ControlSystem(rules)

def braking(d, v):
    sim = ctrl.ControlSystemSimulation(system)
    sim.input['distance'] = d
    sim.input['closing_speed'] = v
    sim.compute()
    return sim.output['brake']

if __name__ == '__main__':
    tests = [(5,25),(10,10),(15,5),(20,15),(40,5),(40,15),(40,25),(70,5),(70,15),(90,28)]
    for i,(d,v) in enumerate(tests,1):
        print(f'T{i:02d}  D={d:>3} m  Vc={v:>2} m/s  ->  {braking(d,v):5.1f} %')
