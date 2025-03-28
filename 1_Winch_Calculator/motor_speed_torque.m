% DC motor datasheet parameters
R = 7.4
tau_c = 0.001  % friction [Nm]
K=0.025        % Torque constant [Nm/A]
V =12          % supply voltage [V]
i_s = V/R      % Stall current [A]
i_n = 0.0187     % no load current
i=[ i_n: 0.01: i_s] 
eta = (-R*K*i.^2 + (tau_c*R+V*K)*i -tau_c*V)./(V*K*i) %efficiency []


RAD2RPM = 180/2*pi
speedRPM = RAD2RPM*(V-R*i)/K
no_load_speedRPM = speedRPM(1) % no load speed corresponds to current to overcome coulomb friction torques




% compute point of max efficiency analytically
i_max = sqrt(tau_c*V/(R*K))
eta_max = (-R*K*i_max.^2 + (tau_c*R+V*K)*i_max -tau_c*V)./(V*K*i_max)


% verify it matches with the computed curve
subplot(2,1,1)
plot(i, eta)
grid on
hold on
plot(i_max, eta_max,'ro')
xlabel('Current i [A]')
ylabel('Efficiency eta')


subplot(2,1,2)
% plot speed current characteristic
plot(i, speedRPM,'b')    
grid on
hold on 
plot(i_n, no_load_speedRPM,'ro')
xlabel('Current i [A]')
ylabel('Speed [RPM]')