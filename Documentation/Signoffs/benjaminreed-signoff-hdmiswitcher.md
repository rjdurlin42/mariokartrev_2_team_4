Team 4 -- Mario Kart & Ride Replay Simulator

Team Members: Ray Durlin, Blake Pickett, Tyler Chittum, Benjamin Reed, and Sage Mooneyham

Detail Design: HDMI Switcher

*Function of the Subsystem:*

The HDMI Switcher is designed to allow users to connect the HDMI ports for their Nintendo Switch and their RRS kit into a single HDMI input to their television or monitor. The switcher that will be used is the BENFEI single-button HDMI switcher (BHS) retrofitted with a relay as the switching mechanism. These components cannot be determined until a proper analysis of the BHS is completed. This switcher will be installed in the touchscreen compartment and connected to the Raspberry Pi (RPi). The Raspberry Pi will interface with a relay to switch between the bits. The button will be replaced by a single pole single throw relay with the switch input originating from RPi GPIO21 from pin 40 [2].

*Constraints:*

*HDMI Compatibility:* As HDMI is standard in the modern era, the multiplexer needs to be compatible with such an input. The RRS Acquisition is designed to record video at a resolution of 720p. Furthermore, the Nintendo Switch is rated to display data at a resolution of 1080p while in TV mode, which is the mode that the Nintendo Switch will be in while using the bike [1]. The multiplexer must therefore be rated to manage resolutions up to 1080p. It should be commented on that the use of HDMI allows for ease of accessibility for most of the population, especially those who can purchase the MK bike and the RRS kit.

The BHS can display up to 4K resolutions with the caveat that the HDMI cables are no longer than five meters [2]. This is sufficient for the Nintendo Switch and the RRS.

*HDMI Quantity:* As the switcher is expected to manage three ports, the multiplexer must also be capable of doing so. The switcher must have one output port and be capable of switching between two input ports. The BHS meets this criterion [1].

*BHS Switch Ratings: *The BHS's voltage maximums for the switch cannot be determined until the BHS is purchased, as there is no datasheet for the product. An analysis will be conducted to determine the voltage of the signal sent when the button is pressed. Since the product can be purchased off Amazon with two-day shipping, analysis can begin quickly. Once analysis is completed, a follow-up design will be completed.

*Relay Ratings:* As the Raspberry Pi only supplies 3.3 V and a range of -2 mA to 2 mA outputs, a relay with sufficient ratings for those attributes. Additionally, the ratings for the switch pins of the relay must be able to withstand the voltage and current values that the switcher's button is presently located. A proper relay cannot be fully determined until the BHS is analyzed.

*Video State Reset:* Since the BHS utilizes a single button switch, an error can occur when turning off the Raspberry Pi where the state of the switcher and the expected state according to the Raspberry Pi disagree. It is imperative that the UI has a contingency to ensure that the correct display appears on the user's monitor. This is an issue that will be resolved via a UI program. Specifically, the program will read the switcher's current state so if the MK/RRS system is ever unplugged, the Raspberry Pi knows the current state of the switcher and can determine if switching outputs is necessary. Analysis of the BHS is necessary to ensure that this is possible.

*Buildable Schematic:*

![Screenshot (79)](https://user-images.githubusercontent.com/100803313/215166588-85a58984-fabb-4a24-aa6c-24de54f56c09.png)

*Analysis:*

The analysis will occur post-purchase of the BHS, in which a follow-up design will be completed. The analysis will consist of the following actions:

- Determine the schematic for the BHS,

- Determine how the switching mechanism works to determine the use of a MOSFET or a relay,

- Determine current and voltage values at certain components, particularly,

o The button/switching mechanism,

o The selector bits/system

- Calculate power dissipation at key locations,

- Design a schematic for the BHS with the new switch implemented.


*BOM*

| Team 4 - Mario Kart & RRS | Bill of Materials (BOM) |               |   |   |   |   |   |   |
| ------------------------- | ----------------------- | ------------- | - | - | - | - | - | - |
|                           |                         |               |          |  |  |  |  |  |
| Subsystem Name:           | HDMI Switcher           |               |          |  |  |
| Requested by:             | Benjamin R              |               |          |  |  |
| Approve by:               |                         |               |          |  |  |
| Total Cost:               | $10.99                  |               |          |  |  |
|                           |                         |               |          |  |  |  |  |  |
| Level                     | Part #                  | Part Name     | Supplier | Supplier Part # | Qty | Units       | Unit Cost | Cost   |
| 1.1                       | BHS100                  | HDMI Switcher | BENFEI   | N/A             | 1   | Emb. System | $10.99    | $10.99 |
|                           |                         |               |  |  |  |  | Total | $10.99 |

REFERENCES

[1] Nintendo, "Technical Specs." nintendo.com. https://www.nintendo.com/switch/techspecs/#switch-section (accessed Nov. 21, 2022).

[2] Raspberry Pi Ltd., "Raspberry Pi 4 Model B." raspberrypi.com. https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-datasheet.pdf (accessed Nov. 21, 2022)
