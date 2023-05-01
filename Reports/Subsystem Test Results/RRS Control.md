# RRS Control Tests

**PWM Duty Cycle:**

In two trials testing both forward and reverse motion at the maximum output level, the PWM duty cycle of the voltage across the linear actuator was seen to be approximately 25 %. The oscilloscope captures below show the observed waveforms.

![DS1Z_QuickPrint4](https://user-images.githubusercontent.com/118228609/235382685-5b1f634b-0f7d-4940-98e0-dd6a8aede44a.png)

![DS1Z_QuickPrint5](https://user-images.githubusercontent.com/118228609/235382686-1c48e18b-8ce7-4554-8cba-b5fce5ed2a9c.png)

![DS1Z_QuickPrint3](https://user-images.githubusercontent.com/118228609/235383375-c700d2c8-720e-4ca8-aaf9-a2d08812267f.png)

![DS1Z_QuickPrint2](https://user-images.githubusercontent.com/118228609/235383445-886a5d9d-f05d-482f-bbb2-acfb2fe8a724.png)

**Voltage ripple:**

Some voltage ripple may be seen on the output. Further testing on the power supply input to the controller, performed twice, reveals that the peak amplitude of the ripple is 8 V pk-pk.
For more detail, see the following oscilloscope captures:

![DS1Z_QuickPrint2](https://user-images.githubusercontent.com/118228609/235383673-8a38f3d5-7248-4cf6-86c5-d8d4837c728c.png)

![DS1Z_QuickPrint1](https://user-images.githubusercontent.com/118228609/235383683-1310bbf9-b9e6-4aab-b286-5878f3ca4dfb.png)

![DS1Z_QuickPrint6](https://user-images.githubusercontent.com/118228609/235383707-199bd0d0-0d5f-4b6c-9a6e-812a3bddc222.png)

**Stability:**

The device was tested across a range of different movement increments, and no instability was observed. See test demonstration video for details.
Test description: test for maximum extension, maximum retraction, middle point, movement by increments of 200 points, 100 points, 50 points, 25 points, 15 points. Ensure absence of undamped oscillation.

**Back-EMF Protection:**

The body diode foreward voltage was measured with an oscilloscope for each MOSFET in the design during operation for both extension and retraction, and the foreward voltage was always measured to be well below 1 V. See video for further detail.

