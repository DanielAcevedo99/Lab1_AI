import uuid

def generate_uuid():
    uuid_str = str(uuid.uuid4())
    return uuid_str

print(generate_uuid())

with open("results_JavaScript.txt", "w") as f:
    f.write(f"UUID: {generate_uuid()}")