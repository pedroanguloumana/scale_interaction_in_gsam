SECTOR_WIDTH_ANGLE     = 10
SECTOR_WIDTH_RADIUS    = 1

# SECTOR_CLASSES_RADIUS_MIN = {
#     'weak':   1,
#     'strong': 2.5, 
# }

# SECTOR_NAME_AND_CENTER_THETAS = {
#     # '4.0': -45,
#     # '4.5': -22.5,
#     '5.0': 0
# }

SECTORS = {
    'sector23': {
        'theta_min': -112.5 - SECTOR_WIDTH_ANGLE / 2,
        'theta_max': -112.5 + SECTOR_WIDTH_ANGLE / 2,
        'radius_min': 1,
        'radius_max': 2
    },
    'sector34': {
        'theta_min': -67.5 - SECTOR_WIDTH_ANGLE / 2,
        'theta_max': -67.5 + SECTOR_WIDTH_ANGLE / 2,
        'radius_min': 1,
        'radius_max': 2
    },
    'sector45': {
        'theta_min': -22.5 - SECTOR_WIDTH_ANGLE / 2,
        'theta_max': -22.5 + SECTOR_WIDTH_ANGLE / 2,
        'radius_min': 1,
        'radius_max': 2
    },
}