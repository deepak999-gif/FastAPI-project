import requests

new_patient = {
    "patient_id": "P001",
    "name": "Deepak",
    "city": "Kanpur",
    "age": 20,
    "gender": "Male",
    "height": 175,
    "weight": 70
}

response = requests.post(
    "http://127.0.0.1:8000/create_patient",
    json=new_patient
)

print(response.status_code)
print(response.json())