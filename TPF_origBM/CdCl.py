import numpy as np
from numpy.fft import rfft, rfftfreq
import matplotlib.pyplot as plt
import os

def readPostProcess(filename: str) -> (np.array, np.array, np.array):
    with open(filename) as fin:
        data = fin.readlines()[20:]
        time, Cd, Cl = [], [], []
        for row in data:
            row = row.split('\t')
            time.append(float(row[0]))
            Cd.append(float(row[1]))
            Cl.append(float(row[3]))
    return np.array(time), np.array(Cd), np.array(Cl)

if not os.path.exists('pics/'):
    os.mkdir('pics')

fout = open('CdCl.log', 'w')

#print("Default local path to post processing file is ./postProcessing/forceCoeffs1/0/coefficient.dat. If no path entered, default value is used.")
#path = input("Enter path: ")
#if path == '':
#    path = "./postProcessing/forceCoeffs1/0/coefficient.dat"
#    fout.write("Default path value is used.\n")
#else:
#    fout.write(f"Using path = {path}.\n")
path = "./postProcessing/forceCoeffs1/160/coefficient.dat"

time, Cd, Cl = readPostProcess(path)

plt.subplot(2, 1, 1)
plt.plot(time, Cd)
plt.xlabel('time')
plt.ylabel('Cd')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time, Cl)
plt.xlabel('time')
plt.ylabel('Cl')
plt.grid(True)
plt.tight_layout()
plt.savefig('pics/CdCl.png')
plt.clf()

#print("Default start time from which the flow is considered to be established is 100 sec. If no start time entered, default value is used.")
#startTime = input('Enter start time (in seconds): ')
#if startTime == '':
#    startTime = 100
#    fout.write("Default starttime value is used.\n")
#else:
#    startTime = float(startTime)
#    fout.write(f"Using starttime = {startTime}.\n")
startTime = 100

time = time[time > startTime]
Cd, Cl = Cd[-len(time):], Cl[-len(time):]

#if len(time) < 100:
#    fout.close()
#    raise Exception("Not enough data (len of resulting arrays less then 100).")

endIndCd, endIndCl = len(time)-1, len(time)-1
signOfCdDerivative, signOfClDerivative = 1 if Cd[1]-Cd[0] >= 0 else -1, 1 if Cl[1]-Cl[0] >= 0 else -1

for i in range(endIndCd, 0, -1):
    if signOfCdDerivative == 1:
        if Cd[i]-Cd[i-1] >= 0 and Cd[i] > Cd[0] and Cd[i-1] <= Cd[0]:
            endIndCd = i
            break
    else:
        if Cd[i]-Cd[i-1] < 0 and Cd[i] < Cd[0] and Cd[i-1] >= Cd[0]:
            endIndCd = i
            break

for i in range(endIndCl, 0, -1):
    if signOfClDerivative == 1:
        if Cl[i]-Cl[i-1] >= 0 and Cl[i] > Cl[0] and Cl[i-1] <= Cl[0]:
            endIndCl = i
            break
    else:
        if Cl[i]-Cl[i-1] < 0 and Cl[i] < Cl[0] and Cl[i-1] >= Cl[0]:
            endIndCl = i
            break

timeCd = time[:endIndCd+1]
timeCl = time[:endIndCl+1]
Cd = Cd[:endIndCd+1]
Cl = Cl[:endIndCl+1]

plt.subplot(2, 1, 1)
plt.plot(timeCd, Cd)
plt.xlabel('time')
plt.ylabel('Cd')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(timeCl, Cl)
plt.xlabel('time')
plt.ylabel('Cl')
plt.grid(True)
plt.tight_layout()
plt.savefig('pics/CdCl_prepeared.png')
plt.clf()

#if len(timeCd) < 100 or len(timeCl) < 100:
#    fout.close()
#    raise Exception("Not enough data (len of resulting arrays less then 100).")

#fout.write("\n----------------calculating statistics----------------\n\n")

Cd_pulse = Cd - Cd.mean()
Cl_pulse = Cl - Cl.mean()
Cl_std = np.std(Cl)

fout.write(f"Mean Cd = {round(np.mean(Cd), 5)}\nMean Cl = {round(np.mean(Cl), 5)}.\n")
fout.write(f"Standart deviation of Cd = {round(np.std(Cd), 5)}\nStandart deviation of Cl = {round(np.std(Cl), 5)}.\n")

#fout.write("\n----------------calculating Cl fft----------------\n\n")


sp = rfft(Cl_pulse)
sp = np.abs(sp.real)/len(sp.real)
freq = rfftfreq(len(timeCl), d=timeCl[1]-timeCl[0])
max_amplitude_freq_index = np.argmax(np.abs(sp.real))

plt.bar(freq[:5*max_amplitude_freq_index], sp[:5*max_amplitude_freq_index], width=0.01)
plt.xlabel('frequency')
plt.ylabel('Cl_pulse_amplitude')
plt.savefig("pics/Cl_amplitude-frequency-characteristics.png")
plt.clf()

fout.write(f'max amplitude == {round(max(sp), 5)}\nFrequency of max amplitude == {round(freq[max_amplitude_freq_index], 5)}\n')
fout.close()

err = (round(Cd.mean(), 2) - 1.02) * 100000 + (round(Cl_std, 2) - 0.12)*100
f = open("err", "w")
f.write(str(err))
f.close()
