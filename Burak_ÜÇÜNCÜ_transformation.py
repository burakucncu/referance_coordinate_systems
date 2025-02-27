import numpy as np

a = 6378137.0
f = 1 / 298.257222101
e2 = 2 * f - f ** 2

x_coord = float(input("Enter the x coordinate: "))
y_coord = float(input("Enter the y coordinate: "))
z_coord = float(input("Enter the z coordinate: "))

x_coord_north = float(input("Enter the x coordinate of the topocenter: "))
y_coord_east = float(input("Enter the y coordinate of the topocenter: "))
z_coord_up = float(input("Enter the z coordinate of the topocenter: "))

def conversion(x_coord, y_coord, z_coord):
    e = (a**2 - (a * (1 - f))**2)**0.5 / a
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

    lambda_rad = np.arctan2(y_coord, x_coord)
    return fi_2, lambda_rad

def transformation_glbtolcl(x_coord, y_coord, z_coord, x_coord_north, y_coord_east, z_coord_up):
    fi_rad, lambda_rad = conversion(x_coord, y_coord, z_coord)
    
    A = np.array([[-np.sin(fi_rad) * np.cos(lambda_rad), -np.sin(fi_rad) * np.sin(lambda_rad), np.cos(fi_rad)],
                  [-np.sin(lambda_rad), np.cos(lambda_rad), 0],
                  [np.cos(fi_rad) * np.cos(lambda_rad), np.cos(fi_rad) * np.sin(lambda_rad), np.sin(fi_rad)]])
    
    delta_x = x_coord - x_coord_north 
    delta_y = y_coord - y_coord_east
    delta_z = z_coord - z_coord_up
    delta = np.array([delta_x, delta_y, delta_z])
    delta_lcl = np.dot(A, delta)
    
    r = np.linalg.norm(delta_lcl)
    zen = np.arccos(delta_lcl[2] / r)
    azim = np.arctan2(delta_lcl[1], delta_lcl[0])

    azim = np.degrees(azim)
    zen = np.degrees(zen)

    if azim < 0:
        azim += 360
    
    if zen < 0:
        zen += 180

    print(f"Azimuth: {round(azim)} degrees", f"\nZenith: {round(zen)} degrees", f"\nSlant range: {round(r)} meters")
    


transformation_glbtolcl(x_coord, y_coord, z_coord, x_coord_north, y_coord_east, z_coord_up)