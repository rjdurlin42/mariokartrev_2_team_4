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

