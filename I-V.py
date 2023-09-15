import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import pyvisa 

rm = pyvisa.ResourceManager()

####################################
smu = rm.open_resource('')
folder_name = "SAMPLE"
RSEN = "OFF"
VOLT = 10e-3
PANEL = "FRONT" #Rear
#MAX_CURR = 0.001
ITERATIONS = 5
####################################

def init():
    smu.write('*RST') 
    smu.write(f"ROUT:TERM {PANEL}")
    smu.write(":SOUR:FUNC VOLT") 
    smu.write(":SENS:FUNC 'CURR'") 
    smu.write(f":SYST:RSEN {RSEN}")
    #smu.write(f':SENS:CURR:PROT {MAX_CURR}')
    smu.write(':SENS:VOLT:RANG:AUTO ON') 
    smu.write(':SOUR:CURR:RANG:AUTO ON') 
    #smu.write(':FORM:ELEM CURR') 

def measurement():
    voltages = np.arange(-VOLT, VOLT + VOLT/11, VOLT/10) 
    smu.write(':OUTP ON') 
    currents = [] 
    for voltage in voltages:
        #smu.write(f':SOUR:VOLT {voltage:.6f}') 
        smu.write(f':SOUR:VOLT {voltage}') 
        time.sleep(0.01) 
        current = float(smu.query(':READ?')) 
        currents.append(current) 
    smu.write(':OUTP OFF')
    return currents,voltages

    
def probe():
    slopes = np.array([])
    writer = pd.ExcelWriter(str(folder_name)+'.xlsx', engine='xlsxwriter')
    for j in range(0,ITERATIONS):
        x,y = measurement()
        plt.plot(x,y,'o')
        df = pd.DataFrame({'I': x, 'V' :y})
        df.to_excel(writer, sheet_name="Measurement-"+str(j))
        slope, _ = np.polyfit(x,y, deg=1)
        slopes = np.append(slopes,slope)
    mean=np.mean(slopes)
    std=np.std(slopes)
    print("Mean resistance:", mean)
    print("Standard deviation of resistances:", std)
    slope_df = pd.DataFrame({'Mean resistance': [mean],'Standard deviation of resistances': [std]})
    slope_df.to_excel(writer, sheet_name='Summary', index=False)
    x=np.array(x,float)
    plt.plot(x,mean*x)
    plt.xlabel('Voltage (V)')
    plt.ylabel('Current (A)')
    writer.close()
    plt.savefig(str(folder_name)+'.png')
    plt.clf() 

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
os.chdir(folder_name)

init()

probe()
