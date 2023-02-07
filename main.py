from mapapi_PG import show_map

coordinates = '151.21529330927066,-33.85653004033911'
z = 17

show_map(coordinates, map_type='sat', add_params={'z': z})