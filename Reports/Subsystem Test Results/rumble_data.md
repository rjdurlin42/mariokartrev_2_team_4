This document is meant to help quickly gain an understanding of how Joycontrol reports input and output data. In addition, this document will include where this data is located and how to utilize it.

**Getting Started**

Firstly, when connecting the bike to the switch using the sudo python3 run_controller_cli.py command, it is necessary to include the -l flag followed by a file name for the information to go to. This looks like the following:

sudo python3 run_controller_cli.py PRO_CONTROLLER -l myreport

It is also better to not use .txt files or anything similar. Stick with either .hex, .bin, or extensionless files.

To view the hex code that is exported, a dedicated hex editor is necessary. Installed onto the Raspberry Pi OS that is with the MK/RRS bike is the Bless hex editor, although any hex editor will do. Bless can be opened by simply typing "bless" into the terminal. When working on Windows devices, Notepad++ with the Hex Editor plugin works well. This can be obtained through the plugin tab via plugin à plugin admin.

**Report Basics**

The communications between the Nintendo Switch and the controller can be seen via the report, as referenced above. The report presents an input and an output report, distinguished by a leading byte 0xA1 and 0xA2, respectively. For rumble data purposes, the output report is the only one to be considered. For output reports, there are several different output reports, all of which can be found at <https://github.com/dekuNukem/Nintendo_Switch_Reverse_Engineering/blob/master/bluetooth_hid_notes.md>. However, the two most common output reports are subcommand reports and rumble data reports, marked by a second byte of 0x01 and 0x10, respectively.

**Rumble Data Formatting**

            The output reports for rumble data are 23-byte values. The values of interest, however, can be obtained from the first eleven bytes. A simple description of the format will be performed using an example value in hexadecimal:

A2       10        03        62        18        63        40        62        18        63        40

Where:

- A2: Report type. This describes whether it is an output or input report. In this case, it is an output report.

- 10: Output type. This shows what kind of output data is being shown. This is rumble data in this case.

- 03: Counter. This value increments from 0x00 to 0x0F, resetting once it surpasses 0x0F. This is seemingly to ensure the proper rumble data output occurs in sequence.

- 62 18 63 40: Rumble data. This is the primary value that describes the rumble data characteristics. The first four values is for the left joycon, and the second four is for the right joycon. In the case of a pro controller, this is for the left and right rumble packs, respectively. In all cases, the first four bytes repeat for the second four.

For a more thorough description of rumble data in an output report, visit <https://github.com/dekuNukem/Nintendo_Switch_Reverse_Engineering/blob/master/bluetooth_hid_notes.md>. For a description of rumble data in general, visit <https://github.com/dekuNukem/Nintendo_Switch_Reverse_Engineering/blob/master/rumble_data_table.md>. For the purposes of Revision 2 of this project, the in-depth information found in those web pages are not necessary.

**What's Going On?**

            The first thing to note is that there is a persistent rumble data value of 00 01 40 40. This is effectively the rumble's resting state. This value means no rumble is present. This is useful as it presents a method of informing the resistance system when it does not need to be in use. Conversely, any instance that does not present this value needs to be addressed.

            Next, it is important to note that the rumble data does not present a constant value or a constant order. Rather, it sends a group of rumble patterns in a randomized order. These values are recognizable and can be used to determine what in-game instance is occurring. For the purposes of the prototype, there is a focus on the off-road rumble data. Some distinct rumble patterns from Moo Moo Meadows are as follows:

67        37        B7       58

00        01        40        40

CA       8D       61        40

DC       00        3D       40

00        01        40        40

62        18        63        40

B0       00        38        40

This is beneficial because, in the case of driving off-road, a distinct pattern or value can be found, then the resistance can be applied until the user is back on the track. Since the resting value is part of the rumble patterns for being off-road, it can be determined that the user is on the track again after two or more instances of 00 01 40 40 are detected.

            An issue that needs to be addressed is that different stages have variations in rumble data. For example, Dry Dry Desert has the following off-road rumble data:

CA       8A       49        40

CA       8A       61        40

DC       00        BD       4B

DC       00        BD       49

67        29        AF       58

It can also be seen that some rumble states are identical to those found in Moo Moo Meadows. There are also several repeated first bytes, such as 62, 63, 6F, CA, DC, 80, and 67.

            Finally, testing was performed in the Mario Circuit track, the results being many of the same rumble states as are found in Moo Moo Meadows. There are some unique states, but the CA 8D 61 40, DC 00 3D 40, 00 01 40 40 pattern and the 67 37 B7 58, 00 01 40 40 pattern both appear. This indicates that grass, sand, and other types of offroad terrain have their own rumble state lists that, though very similar, are not the same. However, both sand and grass offroad terrains have a commonality in that the fourth bytes of 40, 80, and 58 occur very frequently. Offroad instances can therefore be determined primarily by finding the first byte pattern CA followed by DC, the first byte 67 paired with the fourth byte 58, or an instance of a triad of a combination of 40, 80, or 58. Other values occur, but they occur too rarely to cause concern.

            For being hit by a shell, a unique rumble state of

80        6A       60        80

appeared at or near the beginning of the set of rumble data sent for all three recorded instances of being hit by a shell. This implies that shell collisions always results in this rumble data string being sent to the output report. Additionally, being hit by a shell, when compared to offroad and boost instances, presents the widest variation of fourth byte values. Particularly, the last four bits are the most random out of the three rumble state instances considered here. Finally, the null state does not occur at any point in the patterns. It appears that a shell collision can be detected via the rumble state above. As a fallback, three rumble states where the last four bits do not repeat without either the null state or a fourth byte of 40, 80, 71, or 72 occurring. The purpose of including 71 and 72 can be found below.

            For boosting with a mushroom, the rumble states are the most inconsistent. Between two sets of boost data, only one value was repeated, that value being

78        00        2X       72

where the X represents the numbers 6, 8, or 9, as those are the only ones that occurred. This value was also only found in the first boost's set of rumble data, meaning that it is unreliable and, therefore, unusable. However, there are attributes that makes these states easy to identify. The first byte has the most values between 90 and 9F. More interestingly, the fourth byte only exceeded 7F twice across two boost values, with values 71 and 72 occurring frequently.
