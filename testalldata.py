import numpy as np
from matplotlib import pyplot as plt

data = np.random.randint(0,2,25)
time = np.arange(len(data))



# Unipolar
plt.subplot(2,3,1)
plt.step(time, data,where='post')
plt.title('Unipolar')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.text(0,2,data)
plt.grid(True)
plt.yticks([-2,-1,0,1,2,3])
plt.xticks(time)
# NRZ-L
signal = np.where(data==1, 1, -1)
plt.subplot(2,3,2)
plt.step(time, signal,where='post')
plt.title('NRZ-L')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.text(0,2,data)
plt.grid(True)
plt.yticks([-2,-1,0,1,2,3])
plt.xticks(time)

# NRZ-I
signal = np.zeros(len(data), dtype = int)
flg = True
for i in range(len(data)):
    if data[i] == 1:
        flg = not flg
    if flg:
        signal[i] = 1
    else:
        signal[i] = -1
plt.subplot(2,3,3)
plt.step(time, signal,where='post')
plt.title('NRZ-I')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.text(0,2,data)
plt.grid(True)
plt.yticks([-2,-1,0,1,2,3])
plt.xticks(time)

# RZ
signal = np.zeros(2*len(data), dtype = int)
for i in range(0,2*len(data),2):
    if data[i//2] == 1:
       signal[i] = 1
    else:
        signal[i] = -1
    signal[i+1] = 0
plt.subplot(2,3,4)
plt.step(np.arange(len(signal)), signal,where='post')
plt.title('RZ')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.text(0,2,data)
plt.grid(True)
plt.yticks([-2,-1,0,1,2,3])
plt.xticks(np.arange(len(signal)))

# Manchester
signal = np.zeros(len(data)*2, dtype = int)
for i in range(0,len(data)*2,2):
    if data[i//2] == 0:
        signal[i] = 1
        signal[i+1] = -1
    else:
        signal[i] = -1
        signal[i+1] = 1
plt.subplot(2,3,5)
plt.step(np.arange(len(signal)), signal,where='post')
plt.title('Manchester')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.text(0,2,data)
plt.grid(True)
plt.yticks([-2,-1,0,1,2,3])
plt.xticks(np.arange(len(signal)))

# Differential Manchester
signal = np.zeros(len(data)*2, dtype = int)
start = False
for i in range(0,len(data)*2,2):
    if start:
        if data[i//2] == 0:
            signal[i] =  -1*signal[i-1]
            signal[i+1] = signal[i-1]
        else:
            signal[i] = signal[i-1]
            signal[i+1] = -1* signal[i-1]
    else:
        start = True
        if data[i//2] == 0:
            signal[i] = -1
            signal[i+1] = 1
        else:
            signal[i] = 1
            signal[i+1] = -1
plt.subplot(2,3,6)
plt.step(np.arange(len(signal)), signal,where='post')
plt.title('Differential Manchester')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.text(0,2,data)
plt.grid(True)
plt.yticks([-2,-1,0,1,2,3])
plt.xticks(np.arange(len(signal)))


plt.show()
