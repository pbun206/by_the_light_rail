from lightrail import LightRailStation
from lat_long import Coord
from slugify import slugify

LIGHTRAIL_STATIONS = []
#     LightRailStation(
#         coord=Coord(
#             long=-122.2977995,
#             lat=47.422585,
#         ),
#         name="Angle Lake",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/angle-lake-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.31134,
#             lat=47.579401,
#         ),
#         name="Beacon Hill",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/beacon-hill-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.165794,
#             lat=47.6244495,
#         ),
#         name="BelRed",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/belred-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.191917,
#             lat=47.615234,
#         ),
#         name="Bellevue Downtown",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/bellevue-downtown-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.3202135,
#             lat=47.6195905,
#         ),
#         name="Capitol Hill",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/capitol-hill-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.2926405,
#             lat=47.5596525,
#         ),
#         name="Columbia City",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/columbia-city-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.118432,
#             lat=47.6716333333333,
#         ),
#         name="Downtown Redmond",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/downtown-redmond-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.1911505,
#             lat=47.608055,
#         ),
#         name="East Main",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/east-main-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.303701666667,
#             lat=47.3161173333333,
#         ),
#         name="Federal Way Downtown",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/federal-way-downtown-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.3280185,
#             lat=47.598049,
#         ),
#         name="Int'l Dist/Chinatown",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/international-district-chinatown-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.304296,
#             lat=47.590296,
#         ),
#         name="Judkins Park",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/judkins-park-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.294398,
#             lat=47.3895445,
#         ),
#         name="Kent Des Moines",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/kent-des-moines-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.294746333333,
#             lat=47.8156386666667,
#         ),
#         name="Lynnwood City Center",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/lynnwood-city-center-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.109772,
#             lat=47.66727,
#         ),
#         name="Marymoor Village",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/marymoor-village-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.2332615,
#             lat=47.588208,
#         ),
#         name="Mercer Island",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/mercer-island-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.297802,
#             lat=47.5767155,
#         ),
#         name="Mount Baker",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/mount-baker-station-transit-center",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.314781,
#             lat=47.784998,
#         ),
#         name="Mountlake Terrace",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/mountlake-terrace-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.328282,
#             lat=47.703038,
#         ),
#         name="Northgate",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/northgate-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.281582,
#             lat=47.5380155,
#         ),
#         name="Othello",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/othello-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.1387985,
#             lat=47.6363865,
#         ),
#         name="Overlake Village",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/overlake-village-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.331318,
#             lat=47.602669,
#         ),
#         name="Pioneer Square",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/pioneer-square-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.279335,
#             lat=47.5226095,
#         ),
#         name="Rainier Beach",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/rainier-beach-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.133619,
#             lat=47.6448216666667,
#         ),
#         name="Redmond Technology",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/redmond-technology-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.3159845,
#             lat=47.676594,
#         ),
#         name="Roosevelt",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/roosevelt-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.3273925,
#             lat=47.5802705,
#         ),
#         name="SODO",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/sodo-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.29686,
#             lat=47.445011,
#         ),
#         name="SeaTac/Airport",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/seatac-airport-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.3228895,
#             lat=47.764088,
#         ),
#         name="Shoreline North/185th",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/shoreline-north-185th-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.325243,
#             lat=47.736126,
#         ),
#         name="Shoreline South/148th",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/shoreline-south-148th-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.190400333333,
#             lat=47.586566,
#         ),
#         name="South Bellevue",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/south-bellevue-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.17857,
#             lat=47.623774,
#         ),
#         name="Spring District",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/spring-district-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.327171,
#             lat=47.5920545,
#         ),
#         name="Stadium",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/stadium-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.2974195,
#             lat=47.359318,
#         ),
#         name="Star Lake",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/star-lake-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.33596,
#             lat=47.607746,
#         ),
#         name="Symphony",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/symphony-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.2882005,
#             lat=47.464098,
#         ),
#         name="Tukwila Int'l Blvd",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/tukwila-international-boulevard-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.3141305,
#             lat=47.660312,
#         ),
#         name="U District",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/u-district-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.3037655,
#             lat=47.6498305,
#         ),
#         name="Univ of Washington",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/university-washington-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.3366585,
#             lat=47.6116045,
#         ),
#         name="Westlake",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/westlake-station",
#     ),
#     LightRailStation(
#         coord=Coord(
#             long=-122.1837465,
#             lat=47.618069,
#         ),
#         name="Wilburton",
#         url="https://www.soundtransit.org/ride-with-us/stops-stations/wilburton-station",
#     ),
LINE_1_STATIONS = [
    LightRailStation(
        coord=Coord(
            long=-122.294746333333,
            lat=47.8156386666667,
        ),
        name="Lynnwood City Center",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/lynnwood-city-center-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.314781,
            lat=47.784998,
        ),
        name="Mountlake Terrace",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/mountlake-terrace-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.3228895,
            lat=47.764088,
        ),
        name="Shoreline North/185th",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/shoreline-north-185th-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.325243,
            lat=47.736126,
        ),
        name="Shoreline South/148th",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/shoreline-south-148th-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.328282,
            lat=47.703038,
        ),
        name="Northgate",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/northgate-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.3159845,
            lat=47.676594,
        ),
        name="Roosevelt",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/roosevelt-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.3141305,
            lat=47.660312,
        ),
        name="U District",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/u-district-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.3037655,
            lat=47.6498305,
        ),
        name="Univ of Washington",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/university-washington-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.3202135,
            lat=47.6195905,
        ),
        name="Capitol Hill",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/capitol-hill-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.3366585,
            lat=47.6116045,
        ),
        name="Westlake",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/westlake-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.33596,
            lat=47.607746,
        ),
        name="Symphony",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/symphony-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.331318,
            lat=47.602669,
        ),
        name="Pioneer Square",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/pioneer-square-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.3280185,
            lat=47.598049,
        ),
        name="Int'l Dist/Chinatown",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/international-district-chinatown-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.327171,
            lat=47.5920545,
        ),
        name="Stadium",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/stadium-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.3273925,
            lat=47.5802705,
        ),
        name="SODO",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/sodo-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.31134,
            lat=47.579401,
        ),
        name="Beacon Hill",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/beacon-hill-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.297802,
            lat=47.5767155,
        ),
        name="Mount Baker",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/mount-baker-station-transit-center",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.2926405,
            lat=47.5596525,
        ),
        name="Columbia City",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/columbia-city-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.281582,
            lat=47.5380155,
        ),
        name="Othello",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/othello-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.279335,
            lat=47.5226095,
        ),
        name="Rainier Beach",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/rainier-beach-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.2882005,
            lat=47.464098,
        ),
        name="Tukwila Int'l Blvd",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/tukwila-international-boulevard-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.29686,
            lat=47.445011,
        ),
        name="SeaTac/Airport",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/seatac-airport-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.2977995,
            lat=47.422585,
        ),
        name="Angle Lake",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/angle-lake-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.294398,
            lat=47.3895445,
        ),
        name="Kent Des Moines",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/kent-des-moines-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.2974195,
            lat=47.359318,
        ),
        name="Star Lake",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/star-lake-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.303701666667,
            lat=47.3161173333333,
        ),
        name="Federal Way Downtown",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/federal-way-downtown-station",
    ),
]

LINE_2_STATIONS = [
    LightRailStation(
        coord=Coord(
            long=-122.118432,
            lat=47.6716333333333,
        ),
        name="Downtown Redmond",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/downtown-redmond-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.109772,
            lat=47.66727,
        ),
        name="Marymoor Village",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/marymoor-village-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.133619,
            lat=47.6448216666667,
        ),
        name="Redmond Technology",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/redmond-technology-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.1387985,
            lat=47.6363865,
        ),
        name="Overlake Village",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/overlake-village-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.165794,
            lat=47.6244495,
        ),
        name="BelRed",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/belred-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.17857,
            lat=47.623774,
        ),
        name="Spring District",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/spring-district-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.1837465,
            lat=47.618069,
        ),
        name="Wilburton",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/wilburton-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.191917,
            lat=47.615234,
        ),
        name="Bellevue Downtown",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/bellevue-downtown-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.1911505,
            lat=47.608055,
        ),
        name="East Main",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/east-main-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.190400333333,
            lat=47.586566,
        ),
        name="South Bellevue",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/south-bellevue-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.2332615,
            lat=47.588208,
        ),
        name="Mercer Island",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/mercer-island-station",
    ),
    LightRailStation(
        coord=Coord(
            long=-122.304296,
            lat=47.590296,
        ),
        name="Judkins Park",
        url="https://www.soundtransit.org/ride-with-us/stops-stations/judkins-park-station",
    ),
]

def stops_to_form(stops):
    res = ""
    # https://stackoverflow.com/questions/5574042/string-slugification-in-python
    for stop in stops:
        # https://stackoverflow.com/questions/24322599/why-cannot-change-checkbox-color-whatever-i-do accent color
        res += "<div class=\"form-check\">"
        res += f"<input style=\"appearance: auto; accent-color: oklch(0.65 0.1 270)\"class=\"form-check-input\" name=\"{slugify(stop.name)}\" type=\"checkbox\" id=\"{slugify(stop.name)}\">"
        res += f"<label class=\"form-check-label\" for=\"{slugify(stop.name)}\">"
        res += stop.name
        res += "</label>"
        res += "<br>"
        res += "</div>"
    return res

            
        
