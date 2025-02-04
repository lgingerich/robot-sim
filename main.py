import numpy as np
import matplotlib.pyplot as plt

class SingleLinkArm:
    def __init__(self, arm_length, arm_mass, payload_mass):
        """
        Initialize the single-link robot arm
        
        Args:
            arm_length (float): Length of the arm in meters
            arm_mass (float): Mass of the arm in kg
            payload_mass (float): Mass of the payload at the end of the arm in kg
        """
        self.length = arm_length
        self.cog = arm_length / 2  # Center of gravity at half length
        self.arm_mass = arm_mass
        self.payload_mass = payload_mass
        self.g = 9.81  # Gravitational acceleration in m/s²

    def calculate_torque(self, angle_deg):
        """
        Calculate torque for a given angle
        
        Args:
            angle_deg (float): Angle in degrees from vertical (0° is straight up)
            
        Returns:
            float: Total torque in Nm
        """
        # Convert angle to radians
        angle_rad = np.radians(angle_deg)
        
        # Calculate torque from arm weight
        arm_torque = self.arm_mass * self.g * self.cog * np.sin(angle_rad)
        
        # Calculate torque from payload
        payload_torque = self.payload_mass * self.g * self.length * np.sin(angle_rad)
        
        # Total torque
        total_torque = arm_torque + payload_torque
        
        return total_torque

    def plot_torque_curve(self):
        """Plot torque vs angle across the full range of motion"""
        angles = np.linspace(0, 180, 181)
        torques = [self.calculate_torque(angle) for angle in angles]
        
        plt.figure(figsize=(10, 6))
        plt.plot(angles, torques)
        plt.title('Torque vs Angle')
        plt.xlabel('Angle (degrees)')
        plt.ylabel('Torque (Nm)')
        plt.grid(True)
        plt.show()

# Example usage
if __name__ == "__main__":
    
    arm = SingleLinkArm(arm_length=0.85, arm_mass=10.0, payload_mass=5.0)
    
    # Calculate torque at specific angles
    print(f"Torque at 0° (vertical): {arm.calculate_torque(0):.2f} Nm")
    print(f"Torque at 90° (horizontal): {arm.calculate_torque(90):.2f} Nm")
    print(f"Torque at 180° (vertical down): {arm.calculate_torque(180):.2f} Nm")
    
    # Plot torque curve
    arm.plot_torque_curve()
