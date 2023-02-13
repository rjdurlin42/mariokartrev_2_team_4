%INITIALIZATION
r = 0.0254; % radius in meters
D = 0.0508; % mag diameter in m
l = 0.00635; % thickness in meters
minD = 0.002; %min magnet dist
maxD = 0.025; %max mag dist
effectiveR = 0.305;
t = 0.0127; %flywheel thickness
u0 = 4*pi*(10.^-7); % permeability in a vacuum
Br = 1.48; % max residual flux density in Tesla (14800 in Gauss)
d = (minD:0.000001:maxD); % Range of distances from 2 mm to 25 mm away from the flywheel
V = pi*(r^2)*l; % Volume of magnet
m = (Br*V)/u0; % Magnetic dipole moment
By = (u0.*m)./(4.*pi.*d.^3);
p = 3.77e7; %Conductivity
D2 = 0.1016; %diameter of magnets (simulating 4" diameter bracket)
R = 0.1016-(D2/2); %radius of flyhweel - 4" radius

for(RPM = [2501.6 6192.2]) %This loop has an iteration for the upper and lower speed bounds
    w = (2*pi/60)*RPM; %Conversion of flywheel speed into rad/s
    Td = ((pi*p*(D2.^2)*t*((By/10000).^2).*(R.^2).*w)/4)*2.44*21.5; %Calculation of torque vector
    i = 1; %Increment counter
    while(Td(i) > 49.23) %Counts up to the first usable torque value
        i = i+1;
    end
    first_usable = i; %Index counter for array element corresponding to first usable torque value
    while(Td(i) >= 0.004) %Counts the the last usable torque value
        i = i+1;
    end
    last_usable = i-1; %Index counter for array element corresponding to last usable torque value
    figure, plot(d(first_usable:last_usable), Td(first_usable:last_usable)); %Plots the usable torque range over distance
    xlabel("Distance (m)")
    ylabel("Developed Torque (N*m)")
end
