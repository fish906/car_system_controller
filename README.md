This project is aimed to offer a full software suite for controlling the Faller Car System.

The logic (eg. traffic rules and routing) is controlled by a central server. A Raspberry Pi has more than enough power
for this kind of workload.

The physical components of the car system (eg. traffic lights, magnets etc.) are controlled by (cheap) ESP32 
microcontrollers. 

As for the communication protocol, I'm planning on using MQTT for now.
