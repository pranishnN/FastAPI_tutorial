
def get_data(data, is_id = True) -> dict:
    rdata = {
        "id": str(data["_id"]),
        "name": data["name"],
        "description": data["description"],
        "is_active": data["is_active"],
    }
    if not is_id:
        del rdata['id']
    return rdata

def get_all_data(datas) -> list:

    return [get_data(data) for data in datas]

def get_address(address) -> dict:
    return {
        "id": str(address["_id"]),
        "street": address["street"],
        "city": address["city"],        
    }

def get_all_address(data) -> list:
    return [get_address(address) for address in data]