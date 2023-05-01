# RRSA Testing

**Sync Test:**

For the initial test, recording was started, and the device was raised into the air 23 s after beginning recording. The collected video verifies that this is the timestamp at which the device was raised, and the collected data show a decrease in barometric pressure beginning at this time. The last data index corresponds to the ending timestamp of the video for both pressure and speed data.

![Screenshot_2023-04-30_14-12-02](https://user-images.githubusercontent.com/118228609/235369381-c9255f22-0c29-41a8-96b0-1cd3e2a7038b.png)

![Psync](https://user-images.githubusercontent.com/118228609/235369389-d4f8aab9-0c57-46c9-89c4-1d8c1fd2094b.png)

A following test was used to further test syncing of the video footage to an external clock: start clock simultaneously to video recording, record clock.

![Screenshot_2023-04-30_14-28-40](https://user-images.githubusercontent.com/118228609/235370257-59c691d2-2b40-4cb5-a45b-869c195852ac.png)

This test produced the expected result.

In testing of the pressure sensor, similar correspondance of the change in elevation seen in the video and the change in pressure values was observed indicating successful syncing.
The sync was proven to be inadequite; however via 3 hour testing. In a 3 hour trial, the end result showed a final timestamp of 3:02:48 while the final data index was 110778 ds, indicating a desync of 110 s (where the data length is longer than the video). Reviewing the footage reveals that the video footage occasionally skips during recording, resulting in a shorter video relative to the collected data.

**Battery and Storage Test:**

The device was tested continuously recording for 3 hours. The device met specification in two trials, the results of which are below.

Trial 1:

    Vfinal (pi on) = 3.797 V
    On-board Charge Indication: 3/5
    Storage used: 8770091459 bytes (8.2 GiB)

Trial 2:

    Vfinal (pi on) = 3.729 V
		On-board Charge Indication: 3/5
		Storage used: 8913880643 bytes (8.3 GiB)

Based on the above storage usage, combined with the current storage usage, the device can store 42 hours worth of ride recordings.

Storage usage:

    Boot partition: 255 MiB
	  System files: 3586464503 bytes
	  Free Space (with no recordings): 115.5 GiB

**Durability Test:**

The device was sprayed down with water in a sink. The first trial was 5 min, the second 10 min. All functions were tested by recording during and after this, and no loss of functionality or damage was noted. To test the durability of the mounting bracket, the bike was ridden over gravel three times, then off the edge of the sidewalk. Following riding off the edge of the sidewalk, the mounting bracket broke, resulting in a failed test and preventing further durability testing.

**Altitude Sensing Precision Test:**

The device was raised 30 mm in three trials with the temperature controlled at 60 degrees F.

Trial 1:

![alt](https://user-images.githubusercontent.com/118228609/235381631-e489ff23-afac-4446-96b9-75747d6babff.png)

    Start value: 975.489 hPa
    End value: 975.439 hPa
    Measured change in pressure: 0.050 hPa
    Ideal change in pressure: 0.034 hPa
    Corresponding change in altitude: 44.16 cm
    Error: 14.16 cm (rated error: 4.76 cm)

Trial 2:

![alt2](https://user-images.githubusercontent.com/118228609/235381642-211cc4f2-2c9f-48ba-a185-1e1e8f5f7e5f.png)

    Start value: 974.970 hPa
    End value: 974.930 hPa
    Measured change in pressure: 0.040 hPa
    Ideal change in pressure: 0.034 hPa
    Corresponding change in altitude: 35.37 cm
    Error: 5.37 cm (rated error: 4.76 cm)

Trial 3:

![Alt3](https://user-images.githubusercontent.com/118228609/235381655-6fe2132d-4189-4d7a-997e-91bc9811fc27.png)

    Start value: 975.237 hPa
    End value: 975.205 hPa
    Measured change in pressure: 0.032 hPa
    Ideal change in pressure: 0.034 hPa
    Corresponding change in altitude: 28.25 cm
    Error: 1.75 cm (rated error: 4.76 cm)

*Approximating elevation to be 970 hPa (literature value for Cookeville), T = 70 F, P0 = 1013.25 hPa*

In the first and second trials, significant error is observed relative to the specification. Analysis of the plots gives the impression that the measured pressure tends to drift with time, as the measured pressure changes significantly even at times when the device was not in motion.

**Pressure Accuracy Test:**

The accuracy of the pressure sensor was consistantly within 5 % of the literature value for Cookeville (all trials shown above count for this test, including the entirety of both 3 hour trials).

    Atmospheric pressure in Cookeville, TN: 97 kPa = 970 hPa [Source: https://elevation.maplogs.com/poi/cookeville_tn_usa.34896.html]
    Upper limit: 1018.5
    Lower limit: 921.5

