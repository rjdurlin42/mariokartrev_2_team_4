Team 4 -- Mario Kart & Ride Replay Simulator

Team Members: Ray Durlin, Blake Pickett, Tyler Chittum, Benjamin Reed, and Sage Mooneyham

Detail Design: HDMI Switcher

*Function of the Subsystem:*

The HDMI Switcher is designed to allow users to connect the HDMI ports for their Nintendo Switch and their RRS kit into a single HDMI input to their television or monitor. The switcher that will be used is the BENFEI single-button HDMI switcher (BHS) retrofitted with a Fujitsu NAL-12W-K relay as the switching mechanism. A 1N5818 Diode will protect the This switcher will be installed in the touchscreen compartment and connected to the Raspberry Pi (RPi). If the control bits can be accessed, the Raspberry Pi will interface with a relay to switch between the bits. The button will be replaced by a single pole single throw relay with the switch input originating from a RPi GPIO pin. A 1N5818 diode will protect the RPi from back EMF resulting from the de-energizing of the relay coil [3].

*Constraints:*

*HDMI Compatibility:* The BHS must be rated for 1080p resolutions.

*HDMI Quantity:* The switcher must have at minimum two input HDMI ports and one output HDMI port.

*Relay Voltage/Current Ratings:* The relay coil must be rated for 3.3 V and 11.7 mA, and the relay must operate at 3.3 V or below.

*Relay Power Rating:* The power dissipation at the relay coil cannot exceed 70 mW.

*Back EMF Accommodations:* A diode must be implemented in parallel with the relay coil to protect the RPi from back EMF that results from de-energizing the coil [3].

*Background*

As HDMI is standard in the modern era, the multiplexer needs to be compatible with such an input. The RRS Acquisition is designed to record video at a resolution of 720p. Furthermore, the Nintendo Switch is rated to display data at a resolution of 1080p while in TV mode, which is the mode that the Nintendo Switch will be in while using the bike [1].

The Raspberry Pi supplies 3.3 V [2]. A relay with coil terminals rated for these values are necessary. Additionally, to ensure that the relay functions properly, the "must operate voltage" must be less than 3.3 V. Finally, the RPi is limited to a maximum 16 mA output, so the coil drive current must be less than 16 mA to accommodate
 
*Buildable Schematic:*

![Screenshot (87)](https://user-images.githubusercontent.com/100803313/217079972-4a1b54e3-38e4-4622-be08-7dbfa13a85b0.png)

The schematic shows how the BHS button ports will interact with the relay. As there is no schematic available for the BHS online, a schematic cannot be provided. However, it is not needed to prove the relay retrofit will work. Relay switches act as a button that completes the circuit when an electrical value is applied to its coil and opens the circuit otherwise. This is identical to how a button works, except the button utilizes the physical depression of the button to complete the circuit. Since these two methods are almost identical in how they connect a circuit, it can easily be inferred that replacing the button with a relay will work.

*Analysis:*

The equation for power is P = I^2^R. In this case, the power is calculated as

P = 0.0117A^2 (257 Ω)

P = 35 mW

Therefore, the relay must be rated for 35 mW. The TXS2-L-3V relay is rated for 70 mW and is therefore sufficient [4]. Additionally, for the 3.3V pulse, the equation is

P = V^2/R

P = 3.3V^2/257 Ω

P = 43 mW

 which also shows the relay rating is sufficient.

*BOM*

| Team 4 - Mario Kart & RRS | Bill of Materials (BOM) |               |   |   |   |   |   |   |
| ------------------------- | ----------------------- | ------------- | - | - | - | - | - | - |
| Subsystem Name:           | HDMI Switcher           |                 |  |  |  |
| Requested by:             | Benjamin R              |                 |  |  |  |
| Approve by:               |                         |                 |  |  |  |
| Total Cost:               | $16.69                  |                 |  |  |  |
|                           |                         |                 |  |  |  |  |  |  |
|                           |                         |                 |  |  |  |  |  |  |
| Level                     | Part #                  | Part Name       | Supplier | Supplier Part # | Qty | Units | Unit Cost | Cost |
| 1                         | BHS100                  | HDMI Switcher   | BENFEI | N/A | 1 | Emb. System | $10.99 | $10.99 |
| 2.1                       | RELAY100                | TXS2-L-3V Relay | Digikey | 255-1899-ND | 1 | Piece | $5.30 | $5.30 |
| 2.2                       | DIODE100                | 1N5818 Diode    | Digikey | 497-4548-1-ND | 1 | Piece | $0.40 | $0.40 |
|                           |                         |                 |  |  |  |  | Total | $16.69 |

REFERENCES

[1] Nintendo, "Technical Specs." nintendo.com. https://www.nintendo.com/switch/techspecs/#switch-section (accessed Nov. 21, 2022).

[2] Raspberry Pi Ltd., "Raspberry Pi 4 Model B." raspberrypi.com. https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-datasheet.pdf (accessed Nov. 21, 2022)

[3] Durakool, “A Layman’s Guide to Coil Suppression.” Durakoolrelays.com. https://www.durakoolrelays.com/information/technology/layman-s-guide-to-coil-suppression/#:~:text=If%20the%20coil%20is%20de,Back%20EMF%20(Electromotive%20Force).

[4] Panasonic, “TX-S Relays.” Panasonic.eu. https://mediap.industry.panasonic.eu/assets/download-files/import/mech_eng_txs.pdf
