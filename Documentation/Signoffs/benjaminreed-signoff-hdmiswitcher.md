Team 4 -- Mario Kart & Ride Replay Simulator

Team Members: Ray Durlin, Blake Pickett, Tyler Chittum, Benjamin Reed, and Sage Mooneyham

Detail Design: HDMI Switcher

*Function of the Subsystem:*

The HDMI Switcher is designed to allow users to connect the HDMI ports for their Nintendo Switch and their RRS kit into a single HDMI input to their television or monitor. The switcher that will be used is the BENFEI single-button HDMI switcher (BHS) retrofitted with a Fujitsu NAL-12W-K relay as the switching mechanism. A 1N5818 Diode will protect the This switcher will be installed in the touchscreen compartment and connected to the Raspberry Pi (RPi). If the control bits can be accessed, the Raspberry Pi will interface with a relay to switch between the bits. The button will be replaced by a single pole single throw relay with the switch input originating from a RPi GPIO pin. A 1N5818 diode will protect the RPi from back EMF resulting from the de-energizing of the relay coil [3].

*Constraints:*

*HDMI Compatibility:* As HDMI is standard in the modern era, the multiplexer needs to be compatible with such an input. The RRS Acquisition is designed to record video at a resolution of 720p. Furthermore, the Nintendo Switch is rated to display data at a resolution of 1080p while in TV mode, which is the mode that the Nintendo Switch will be in while using the bike [1]. The multiplexer must therefore be rated to manage resolutions up to 1080p. It should be commented on that the use of HDMI allows for ease of accessibility for most of the population, especially those who can purchase the MK bike and the RRS kit.

The BHS can display up to 4K resolutions with the caveat that the HDMI cables are no longer than five meters [2]. This is sufficient for the Nintendo Switch and the RRS.

*HDMI Quantity:* As the switcher is expected to manage three ports, the multiplexer must also be capable of doing so. The switcher must have one output port and be capable of switching between two input ports. The BHS meets this criterion [1].

*BHS Switch Ratings: *The BHS's voltage maximums for the switch cannot be determined until the BHS is purchased, as there is no datasheet for the product. An analysis will be conducted to determine the voltage of the signal sent when the button is pressed. Since the product can be purchased off Amazon with two-day shipping, analysis can begin quickly. Once analysis is completed, a follow-up design will be completed.

*Relay Voltage/Current Ratings:* The Raspberry Pi supplies 3.3 V [2]. A relay with coil terminals rated for these values are necessary. Additionally, to ensure that the relay functions properly, the "must operate voltage" must be less than 3.3 V. Finally, the RPi is limited to a maximum 16 mA output, so the coil drive current must be less than 16 mA to accommodate. The relay of choice is the TXS2-L-3V because it has a maximum voltage rating of 4.5 V (150 % of rating), a coil current of 11.7 mA, and a must operate voltage of 2.4 V (80% of rating) [4].

*Relay Power Rating:* The relay is rated for a power dissipation of 70 mW. Therefore, the power dissipation at the relay cannot exceed this value. Analysis to confirm this can be seen below.

*Back EMF Accommodations:* The de-energizing of the relay results in back EMF. If the RPi is left unprotected, this back EMF can damage the RPi. The RPi can be protected by implementing a diode in parallel with the relay coil [3]. The exact EMF cannot be determined as the inductance of the coil cannot be found.

*Video State Reset:* Since the BHS utilizes a single button switch, an error can occur when turning off the Raspberry Pi where the state of the switcher and the expected state according to the Raspberry Pi disagree. It is imperative that the UI has a contingency to ensure that the correct display appears on the user's monitor. This is an issue that will be resolved via a UI program. Specifically, the program will read the switcher's current state so if the MK/RRS system is ever unplugged, the Raspberry Pi knows the current state of the switcher and can determine if switching outputs is necessary. Analysis of the BHS is necessary to ensure that this is possible.

*Buildable Schematic:*

![Screenshot (85)](https://user-images.githubusercontent.com/100803313/216205222-b202e7e0-173a-4004-9dcd-96414c8cbd71.png)

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
