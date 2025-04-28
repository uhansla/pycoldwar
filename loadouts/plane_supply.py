import dcs.planes as planes

BLUE = [
    'An-26B'
]

RED = [
    'An-26B'
]

planes_map = {
    'An-26B': [
        {
            'type': planes.An_26B,
            'id': planes.An_26B.id,
            'fuel': planes.An_26B.fuel_max,
            'chaff': planes.An_26B.chaff,
            'flare': planes.An_26B.flare,
            'payload': {
                'pylons': [
                ]
            }
        },
    ],
}
