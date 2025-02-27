import numpy as np

x_coord = float(input("Enter the x coordinate: "))
y_coord = float(input("Enter the y coordinate: "))
z_coord = float(input("Enter the z coordinate: "))

convert_ell = int(input("Which conversion do you want? GRS80 = 1, WGS84 = 2, PZ-90.02 = 3: "))

if convert_ell == 1:
    a = 6378137.0 # GRS80
    f = 1/298.257222101

elif convert_ell == 2:
    a = 6378137.0
    f = 1/298.257223563

elif convert_ell == 3:
    a = 6378136.0
    f = 1/298.257839303

b = a * (1 - f)
e = (a**2 - b**2)**0.5 / a

def conversion():
        
    fi_zero = np.arctan(z_coord / (x_coord**2 + y_coord**2)**0.5 * (1 - e**2)) # if h = 0
    N = a / ((1 - e**2 * np.sin(fi_zero)**2)**0.5)
    h_1 = (((x_coord**2 + y_coord**2)**0.5) / np.cos(fi_zero)) - N
    fi = np.arctan(z_coord / (((x_coord**2 + y_coord**2)**0.5) * (1 - e**2 * N / (N + h_1))))

    while True:
        N_1 = a / ((1 - e**2 * np.sin(fi)**2)**0.5)
        h_2 = ((x_coord**2 + y_coord**2)**0.5 / np.cos(fi)) - N_1
        fi_2 = np.arctan(z_coord / (((x_coord**2 + y_coord**2)**0.5) * (1 - e**2 * N_1 / (N_1 + h_2))))
        
        if abs(np.degrees(fi_2) - np.degrees(fi)) < 10**-8:
            break
    
        fi = fi_2

    lambda_rad = np.arctan(y_coord / x_coord)
    lambda_deg = np.degrees(lambda_rad)
    fi_deg = np.degrees(fi_2)
    print(f"The converted coordinates are: latitude = {round(fi_deg)}, longitude = {round(lambda_deg)}, height = {round(h_2)}")
    return   

conversion()