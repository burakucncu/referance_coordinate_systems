import numpy as np

X_P, Y_P, Z_P = int(input("enter the coordinate X: ")), int(input("enter the coordinate Y: ")), int(input("enter the coordinate Z: "))  # First coordinates

lambda_deg = int(input("enter the degree lambda: "))
ccw_or_cw_lambda = input("enter the direction of rotation lambda (ccw or cw): ")
if ccw_or_cw_lambda == "ccw":
    lambda_deg = lambda_deg
elif ccw_or_cw_lambda == "cw":
    lambda_deg = -lambda_deg

delta_deg = int(input("enter the degree delta: "))
ccw_or_cw_delta = input("enter the direction of rotation delta (ccw or cw): ")
if ccw_or_cw_delta == "ccw":
    delta_deg = delta_deg
elif ccw_or_cw_delta == "cw":
    delta_deg = -delta_deg

beta_deg = int(input("enter the degree beta: "))
ccw_or_cw_beta = input("enter the direction of rotation beta (ccw or cw): ")
if ccw_or_cw_beta == "ccw":
    beta_deg = beta_deg
elif ccw_or_cw_beta == "cw":
    beta_deg = -beta_deg

def rotation_x(beta_deg):
    beta_rad = np.radians(beta_deg)
    return np.array([
        [1, 0, 0],
        [0, np.cos(beta_rad), np.sin(beta_rad)],
        [0, -np.sin(beta_rad), np.cos(beta_rad)]
    ])

def rotation_y(delta_deg):
    delta_rad = np.radians(delta_deg)
    return np.array([
        [np.cos(delta_rad), 0, -np.sin(delta_rad)],
        [0, 1, 0],
        [np.sin(delta_rad), 0, np.cos(delta_rad)]
    ])

def rotation_z(lambda_deg):
    lambda_rad = np.radians(lambda_deg)
    return np.array([
        [np.cos(lambda_rad), np.sin(lambda_rad), 0],
        [-np.sin(lambda_rad), np.cos(lambda_rad), 0],
        [0, 0, 1]
    ])

def total_rotation_matrix(lambda_deg, delta_deg, beta_deg):
    Rotation_x = rotation_x(beta_deg)
    Rotation_y = rotation_y(delta_deg)
    Rotation_z = rotation_z(lambda_deg)
    
    Rotation_N = np.dot(np.dot(Rotation_x, Rotation_y), Rotation_z)
    return Rotation_N

def transform_coordinates(Rotation_N, r_point):
    r_point_new = np.dot(Rotation_N, r_point)
    return r_point_new

r_point = np.array([X_P, Y_P, Z_P])
r_point_new = transform_coordinates(total_rotation_matrix(lambda_deg, delta_deg, beta_deg), r_point)

print(f"Yeni koordinatlar (X', Y', Z'): {r_point_new}")