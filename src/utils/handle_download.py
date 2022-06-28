from open_mastr import Mastr
from datetime import datetime

def start_download():
    db = Mastr()
    date = datetime(2022,6,8) 
    limit = 2
    chunksize = 1000
    technology = ["solar","biomass",'combustion','gsgk','hydro','nuclear','storage','wind']
    data_types = ["unit_data", "eeg_data", "kwk_data", "permit_data"]  #
    location_types = [
        "location_elec_generation",
        "location_elec_consumption",
        "location_gas_generation",
        "location_gas_consumption",
    ]
    
    # call download functionality
    db.download(
        method="API",
        api_limit=limit,
        api_chunksize=chunksize,
        technology=technology,
        api_date=date,
        api_processes=None,
        api_data_types=data_types,
    )