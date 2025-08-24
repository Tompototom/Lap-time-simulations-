# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 10:33:58 2025

@author: TOM
"""


import pandas as pd
import io
import os
from pathlib import Path
import matplotlib.pyplot as plt
from pathlib import Path


# File path
file_path = r"D:\VUB\5MAIW\Thesis\Apps\OpenLap\OpenLAP-Lap-Time-Simulator-master\OpenLAP Sims\OpenLAP_Aion var_Endurance Germany 2012.csv"

# Read all lines
#################################################################################################################

def csvReader(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find header: first line that repeats immediately
    header_line = None
    for i in range(len(lines)-1):
        if lines[i].strip() and lines[i] == lines[i+1]:
            header_line = i
            break
    if header_line is None:
        raise ValueError("Header lines not found")
    
    # Build CSV text: real header + data lines (skip duplicate header, units row, empty rows)
    header = lines[header_line].strip()
    data_start = header_line + 4  # skip the duplicate header, unit line, and one empty line
    csv_text = header + '\n' + ''.join(lines[data_start:])
    
    # Load into DataFrame
    df = pd.read_csv(io.StringIO(csv_text))
    
    summary = {
        'distance':          round(df['distance'].max() - df['distance'].min(), 2),
        'max_speed':         round(df['speed'].max() * 3.6, 2),
        'average_speed':     round(df['speed'].mean() * 3.6, 2),
        'lap_time':          round(df['time'].max(), 2),
        'energy_spent':      round(df['energy_spent_fuel'].max(), 2),
        
        'ax_max':            round(df['long_acc'].max(), 2),
        'ax_mean':           round(df['long_acc'].mean(), 2),
        'ay_max':            round(df['lat_acc'].max(), 2),
        'ay_mean':           round(df['lat_acc'].mean(), 2),
        
        'wheel_torque_max':  round(df['wheel_torque'].max(), 2),
        'wheel_torque_mean': round(df['wheel_torque'].mean(), 2),
        
        'engine_torque_max':  round(df['engine_torque'].max(), 2),
        'engine_torque_mean': round(df['engine_torque'].mean(), 2),
        'engine_power_max':   round(df['engine_power'].max(), 2),
        'engine_power_mean':  round(df['engine_power'].mean(), 2),
        
        'throttle_mean':     round(df['throttle'].mean(), 2),
        'brake_max':         round(df['brake_force'].max(), 2),
        'brake_mean':        round(df['brake_force'].mean(), 2),
        
        'Fz_aero_max':       round(df['Fz_aero'].max(), 2),
        'Fz_aero_mean':      round(df['Fz_aero'].mean(), 2),
        'Fx_aero_max':       round(df['Fx_aero'].max(), 2),
        'Fx_aero_mean':      round(df['Fx_aero'].mean(), 2),
        'Fz_total_max':      round(df['Fz_total'].max(), 2),
        'Fz_total_mean':     round(df['Fz_total'].mean(), 2),
    }
    vert = (
        pd.DataFrame.from_dict(summary, orient='index', columns=['Value'])
          .reset_index()
          .rename(columns={'index':'Metric'})
    )
    print(vert)

    return df




def variable(df, variable):
    variable = variable.lower()  # make comparison case-insensitive

    if variable == 'lap_time':
        return df['time'].max()

    elif variable == 'distance':
        return df['distance']

    elif variable == 'speed':
        return df['speed'] * 3.6  # km/h

    elif variable == 'energy_spent':
        return df['energy_spent_fuel']

    elif variable == 'long_acc':
        return df['long_acc']

    elif variable == 'lat_acc':
        return df['lat_acc']

    elif variable == 'wheel_torque':
        return df['wheel_torque']

    elif variable == 'engine_torque':
        return df['engine_torque']

    elif variable == 'engine_power':
        return df['engine_power']

    elif variable == 'engine_speed':
        return df['engine_speed']

    elif variable == 'throttle':
        return df['throttle']

    elif variable == 'brake':
        return df['brake_force']

    elif variable == 'fz_aero':
        return -df['Fz_aero']

    elif variable == 'fx_aero':
        return -df['Fx_aero']

    elif variable == 'fx_eng':
        return df['Fx_eng']

    elif variable == 'fx_roll':
        return -df['Fx_roll']

    elif variable == 'fz_mass':
        return -df['Fz_mass']

    elif variable == 'fz_total':
        return -df['Fz_total']

    elif variable == 'yaw_rate':
        return df['yaw_rate']

    elif variable == 'brake_pres':
        return df['brake_pres']

    elif variable == 'steering':
        return df['steering']

    else:
        return None

    


def plot_all(files, x_var='distance', y_var='speed', title=None):
    plt.figure(figsize=(10, 6))

    for label, filepath in files.items():
        df = csvReader(filepath)
        x = variable(df, x_var)
        y = variable(df, y_var)
        plt.plot(x, y, label=label)

    plt.xlabel(x_var.replace('_', ' ').title())
    plt.ylabel(y_var.replace('_', ' ').title())
    plt.ylim(bottom=0)
    if title:
        plt.title(title)
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend()
    #plt.tight_layout()
    plt.show()
    
# Example usage 'Name file': r"path tho CSV"
#Set this to the paths you want.
files = {
    'OP peak': r"D:\VUB\OP Peak.csv",
    'OP continuous': r"D:\VUB\OP continuous.csv",
    'Actual setup': r"D:\VUB\actual setup.csv",

    
    
    #Change x_var and y_var to what you want, the title can also be changed
plot_all(Tyre_size_comp, x_var='distance', y_var='wheel_torque', title='Force at wheel vs Distance')

