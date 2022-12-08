# Mario Kart Rev 2 - Signoff - Mario Kart Bike Wireless Sensors Subsystem 
## Team 4 - Blake Pickett ##

_Function of the Subsystem:_

The function of the newly designed feature is to convert the speed and steering sensors and the microcontrollers on the Mario Kart Bike to be wireless. This new feature will mitigate safety risks to the Mario Kart Bike riders by eliminating the long wires running down the bike and around the bike stand. These long wires are a safety hazard for future customers. The wires that are rectifying and stepping down the power for the sensors on the current version of the Mario Kart Bike will be replaced with a three-AA-battery holder, complete with three AA batteries that will produce 4.5 V and 9 A current to the sensors and microcontrollers. 

_Constraints:_ 

The wireless capability provided by the new design requires the removal of the long wires along the bike. Although eliminating the long wires mitigates a safety risk to Mario Kart Bike riders, the equipment must still have power to work properly. Therefore, the long wires will be replaced with batteries. Multiple batteries will supply the DC voltage and current needed to power the equipment. 

**Speed Sensor:** The KY-032 Obstacle Avoidance Sensor must have a DC voltage between 3.3 V and 5 V to operate correctly. Likewise, the KY-032 Obstacle Avoidance Sensor must have a minimum of 20 mA of current to operate correctly. The microcontroller and Bluetooth module will operate correctly with the given voltage between 3.3 V and 5 V.  

**Steering Sensor:** The Potentiometer voltage must be the same as the analog input, so the voltage for the Potentiometer must be the same as the analog to digital converter (ADC), microcontroller, and Bluetooth module. The ADC has a maximum voltage of 5.5 V and a minimum of 0 V. The microcontroller and Bluetooth module will operate correctly with the given voltage between 3.3 V and 5 V. During the fabrication of the new design, analysis will be performed to ensure that safety risks have been mitigated. Although the long wires will be replaced to mitigate the risk resulting from the potential trip hazard, analysis will be performed to ensure that the batteries are not inducing an unacceptable level of voltage or current onto the Mario Kart Bike frame, posing a potential safety risk to the rider. 

_Buildable Schematic:_     

The wiring schematics for the speed and steering sensors are provided in **Figures 1 and 2**.  

![image](https://user-images.githubusercontent.com/113309616/203215793-172644f2-1529-4fd9-980a-8015473bd7fb.png)
**Figure 1.** Wiring Schematic for the Speed Sensor

![image](https://user-images.githubusercontent.com/113309616/203215817-e0fa5485-77cc-4d7a-8503-4ecf4ed32994.png) 
**Figure 2.** Wiring Schematic for the Steering Sensor

_Analysis:_ 

An analysis has been performed to ensure that the existing steering and speed sensors installed on the Mario Kart Bike perform to specification, meeting both the technical requirements and ethical constraints for user safety. The results of the analysis indicate that the sensors are adequate to meet the intended performance, including the enhanced resistance and trail ride features. After verifying the adequacy of the speed and steering sensors, a design was developed to add the convenience of wireless connectivity. To assist in the verification of wireless capability for the speed and steering sensors, schematics were developed to provide illustrations for visual analysis of the design, including a satisfactory, functional means of mounting the batteries needed to achieve the required voltage. Additionally, the use of mathematical calculations enabled the verification of the quantity of batteries needed to provide the required voltage range. Since a single AA battery provides 1.5 V and 3,000 mA, three batteries will provide 4.5 V, which is sufficient voltage within the required range and the required current. The battery holders feature power on/off switches to conserve power / battery life when not in use. The dimensions of the battery holders, measuring 2.681 inches (l) by 1.906 inches (w) by 0.717 inches (h), are small and compact, avoiding the trip hazard posed by the long wires installed on the previous version of the Mario Kart Bike. Additionally, zip ties will be used to neatly and securely mount the battery holder to the Mario Kart bike frame, further promoting the safety of the Mario Kart Bike rider.  

Once the analysis of the design was determined to be satisfactory using the schematic and mathematical calculations, the materials needed to implement the new design of the speed and steering sensors were priced. The most economical purchasing option for the batteries was selected to ensure adequate quantities for the initial testing, standard use, and spares. The price for these materials were reviewed against the proposed budget and determined to be within range. To further promote safety, proper disposal of batteries drained of power will be performed by wrapping electrical tape on both ends of each battery to ensure that an object does not make a connection between the positive and negative ends of the battery, resulting in a fire during disposal.  

_BOM:_ 

The bill of materials (BOM) to accomplish the design illustrated in the schematics is provided in **Table 1**. 

**Table 1.** Bill of Materials
| Brand / Manufacturer       | Part Name            | Supplier | Part / Model # or ASIN # | Qty | Units  | Unit Cost | Cost   |
| -------------------------- | -------------------- | -------- | ------------------------ | --- | ------ | --------- | ------ |
| OLIREXD / Multicolored LED | 3 AA Battery Holders | Amazon   | B07TJZ2KJ5               | 4   | pieces | $1.75     | $6.98  |
| Duracell                   | AA Battery           | Amazon   | AA-CTx24                 | 24  | pieces | $0.87     | $20.78 |
| HMROPE                     | 8 Inch Zip Ties      | Amazon   | TXLAC                    | 1   | pack   | $9.18     | $9.18  |
| Duck                       | Electrical Tape      | Amazon   | 282289                   | 1   | roll   | $1.48     | $1.48  |
