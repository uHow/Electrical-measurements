import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import pyvisa 

rm = pyvisa.ResourceManager()

#####################################
smu = rm.open_resource('')
folder_name = "SAMPLE"
RSEN = "OFF"
CURRENT = 100e-6
MAX_VOLT = 5
ITERATIONS = 5
#####################################

def init():
    smu.write('*RST') 
    smu.write(':SOUR:FUNC CURR') 
    smu.write(':SENS:FUNC "VOLT"') 
    smu.write(f":SYST:RSEN {RSEN}")
    #smu.write(f':SENS:VOLT:PROT {MAX_VOLT}') 
    smu.write(':SENS:VOLT:RANG:AUTO ON') 
    smu.write(':SOUR:CURR:RANG:AUTO ON') 
    #smu.write(':FORM:ELEM VOLT') 

def measurement():
    currents = np.arange(-CURRENT, CURRENT + CURRENT/11, CURRENT/10) 
    smu.write(':OUTP ON') 
    voltages = [] 
    for current in currents:
        smu.write(f':SOUR:CURR {current}') 
        time.sleep(0.01) 
        voltage = float(smu.query(':READ?')) 
        voltages.append(voltage) 
    smu.write(':OUTP OFF')
    
    return currents,voltages

    
def probe():
    slopes = np.array([])
    writer = pd.ExcelWriter(str(folder_name)+'.xlsx', engine='xlsxwriter')
    for j in range(0,ITERATIONS):
        y,x = measurement()
        plt.plot(x,y,'o')
        df = pd.DataFrame({'U': x, 'I' :y})
        df.to_excel(writer, sheet_name="Measurement-"+str(j))
        slope, _ = np.polyfit(y,x, deg=1)
        slopes = np.append(slopes,slope)
    mean=np.mean(slopes)
    std=np.std(slopes)
    print("Mean resistance:", mean)
    print("Standard deviation of resistances:", std)
    slope_df = pd.DataFrame({'Mean resistance': [mean],'Standard deviation of resistances': [std]})
    slope_df.to_excel(writer, sheet_name='Summary', index=False)
    x=np.array(x,float)
    plt.plot(x,mean*x)
    plt.ylabel('Voltage (V)')
    plt.xlabel('Current (A)')
    writer.close()
    plt.savefig(str(folder_name)+'.png')
    plt.clf() 

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
os.chdir(folder_name)

init()

probe()
            
