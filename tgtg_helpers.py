from tgtg import TgtgClient


def log_in(credentials: dict) -> TgtgClient:
    return TgtgClient(access_token=credentials["access_token"],
                      refresh_token=credentials["refresh_token"],
                      user_id=credentials["user_id"])


def get_items(client: TgtgClient) -> list:
    result = client.get_items()
    l = []
    for entry in result:
        item = entry["item"]
        d = {
            "item": {
                "price": item["price_including_taxes"],
                "value": item["value_including_taxes"],
                "logo_picture": item["logo_picture"],
                "collection_info": item["collection_info"]
            },
            "display_name": entry["display_name"],
            "address": entry["pickup_location"]["address"],
            "items_available": entry["items_available"],
            "new_item": entry["new_item"]
        }
        l.append(d)
    return l


