def data_serializer(data) -> dict:
    return {
        'id': str(data["_id"]),
        'data': data["data"]
    }
