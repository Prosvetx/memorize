
def add_remove_m2m_functional(validated_data: dict, instance_m2m_field, add_key: str, remove_key: str):
    """add, remove objects from m2m field"""
    if validated_data.get(add_key):
        objects = validated_data.get(add_key)
        for obj in objects:
            instance_m2m_field.add(obj)

    if validated_data.get(remove_key):
        objects = validated_data.get(remove_key)
        for obj in objects:
            instance_m2m_field.remove(obj)