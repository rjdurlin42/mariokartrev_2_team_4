Team 4 – Mario Kart & Ride Replay Simulator
Team Members: Ray Durlin, Blake Pickett, Tyler Chittum, Benjamin Reed, and Sage Mooneyham
Detail Design: Resistance System


Function of the Subsystem: 
The function of the resistance system is to wirelessly receive an input value from the RRS processing subsystem. The input value is to be received by the H-Bridge controller. The H-Bridge controller will send a power signal to the linear actuator in the form of a pulse width modulated value to adjust the position of the magnets across the flywheel resulting in the creation of eddy currents in the flywheel. These eddy currents create a magnetic field that opposes the source magnetic field. This causes power dissipation in the flywheel, as well as opposing torque, which creates a change of resistance felt by the user. 

Constraints:
Cost: The main constraint for the resistance system is the cost of materials for both the flywheel, linear motor, and magnets. The total budgeted cost of the resistance system is 50% of the project budget, equaling $600. 
-	Flywheel: A traditional spin bike flywheel used commercially ranges from $270 to $475 used. To mitigate the cost of the flywheel, team 4 will construct a flywheel using the existing bike tire and aluminum sheet material.
-	Linear Motor: An ideal linear motor would have specifications of 100% duty cycle and 23.6 inches per sec speed but would cost over $1,000. To mitigate the cost, the team will suffice with a lower duty cycle linear motor while maintaining a speed of 3.3 inches per sec. The cost is approx. $184. The controller will need to manage the power supplied to the linear actuator to ensure the duty cycle rating is not exceeded.
-	Magnets: A N52 neodymium magnet with a surface field rating of 4000 Gauss or greater ranges from $35 to $50 depending on thickness. Based on the calculations made in the analytical section, the number of magnets required for a rectangular magnet with the dimensions of 2 inches in length by 1 inch in width, with a thickness of 0.5 inch that is 8. The magnet dimensions that are chosen in the resistance system based on cost.

Material:
- Flywheel Material: The material for the constructed flywheel is a constraint, as a ferromagnetic flywheel will experience magnetic pull when in the magnetic field created by the magnets. Because of this, Team 4’s constructed flywheel will be made of aluminum sheets, a non-ferromagnetic material.

Buildable schematic:

![image](https://user-images.githubusercontent.com/114370750/201011044-d22a8e48-4f29-43f6-9733-91bda5719795.png)

![image](https://user-images.githubusercontent.com/114370750/201011097-6f954d7b-ff05-4396-bd05-49222ed99d69.png)




Analysis:
The resistance system is centered around the electromagnetic topic of eddy currents, as well as Lenz’s Law. Electromagnetic braking can be modeled mathematically using D. Schieber’s equation [1]:
τ=1/2 σδωπr^2 m^2 B_Z^2 [1-(r/a)^2/(1-(m/a)^2 )^2 ]
where,
σ = electrical conductivity of the rotating disc
δ = sheet thickness of the rotating disc
ω = angular velocity of the rotating disc
π = constant coefficient
r = radius of the electromagnet 
m = distance of disc axis from pole-face center
a = disc radius
Bz = z component of magnetic flux density, z axis being the direction of the center of the electromagnetic pole
τ = Torque

One thing to note is that Schieber’s equation only works in low-speed applications.
Schieber’s equation was utilized to determine the attributes of the resistance system components. Specifically, the magnetic force necessary and the dimensions of the flywheel were derived from this equation. The following explanation will be referencing Flywheel_Analysis.xlsx.
Each value in the equation was entered into the spreadsheet to allow for analysis. The torque threshold that needed to be met was approximately 30 Nm. This was determined by using the maximum power output for the system, 300 W, divided by a quarter of the maximum angular velocity for the system (described below), resulting in a velocity of 10.15 rad/s. The purpose of this analysis was to determine the attributes that would reach that 30 Nm threshold. 
The following values were able to be determined from the onset.
-	The bicycle’s wheel radius is a known constant of 0.33 m. 
-	The flywheel’s radius was also determined to be 0.33 m because Schieber’s equation produces more torque as flywheel radius increases. For this reason, the radius was determined to be the maximum value possible.
-	The material for the flywheel was determined to be aluminum. This is because aluminum has the highest conductivity for the cost, allowing the resistance system to reach the necessary torque values. This value is therefore 3.77*107 (Ωm)-1.
-	The maximum linear velocity for the average cyclist is approximately 30 mph. Converted to angular velocity, the value was determined to be 40.6 rad/s. This value was determined to be the maximum value to produce the most torque and was used for the duration of the analysis.
-	The axis-to-pole value was set to be approximately 0.305 m. This distance was determined by the flywheel’s radius minus the maximum radius of the magnet options available. It should also be noted that torque is maximized when the magnets are at the edge of the flywheel.
-	The magnetic flux at the end of the radius is given by the equation ∫_ ^  B ⃗⋅n ̂ dA = BA = Bπa^2. This equation was implemented for magnetic flux.
The attributes left to be determined were flywheel thickness, the magnetic field, and the area of the magnet. The magnetic field and magnet area were dependent on the type of magnet used. These had to be determined analytically. It should also be noted that the column labeled “Torque” is the torque through one flywheel, while the column labeled “New Torque” is the sum of the torque in both flywheels.
The first thing to determine was the magnet to be used, this was done by implementing the three magnet models determined to be viable and testing each one for which produces the greatest amount of torque. The magnet models in question were the DX88-N52, the DY04-N52, and the BY0X08-N52. The flywheel’s thickness was set to be 1 mm for analytical purposes. Note that the BY0X08-N52 magnet is rectangular. For the case of this magnet, the expression πr^2 in Schieber’s equation was replaced with the area of a rectangle, and the radius was recorded as 25.4 mm as the orientation of the magnet on the H-Bracket would cause the magnet to act as though that was its radius. Through this way, it was determined that the strongest magnet was the BY0X08-N52. This magnet’s area and magnetic field were used for the rest of the analysis.
The next thing to determine was the number of magnets needed to produce enough magnetic flux to produce 30 Nm of torque. The flywheel’s thickness was set to 2.5 mm for this analysis as it proved to be a more realistic value. The magnetic field and the magnet area were modified to increase with the addition of magnets, and an analysis for one to twelve magnets for one flywheel was completed. Torque values that were within ±100% of the threshold were chosen for further analysis. This large variance was chosen because the thickness of the flywheel proved to have a significant impact on the torque, so a larger sample size was deemed necessary. The magnet quantities chosen were two, three, and four per flywheel.
The flywheel thickness analysis took all possible thickness sizes from the Cut2Size custom cut functionality versus the quantity of magnets selected (Cut2Size.com citation). The values of interest, being those within 15% of the torque threshold, were highlighted in red and taken to price analysis.
The final analysis was the price analysis. This was executed to determine which of the three combinations of flywheel thickness and magnet quantity was the least expensive. It was determined that the least expensive option was the 1.6 mm thick flywheel with four magnets on each side.


![image](https://user-images.githubusercontent.com/114370750/201012188-e285c507-e496-41f7-a01a-832c86b08c23.png)



BOM:

![image](https://user-images.githubusercontent.com/114370750/201011295-cf13f8bb-1d30-43b7-a0ac-1640ab845f02.png)




REFERENCES
[1]	Alexandre José Rosa Nunes and Francisco Miguel Ribeiro Proença Brojo, (2020), “Designing an Eddy Current Brake for Engine Testing” in International Congress on Engineering — Engineering for Evolution, KnE Engineering, pages 743–756. DOI 10.18502/keg.v5i6.7094



