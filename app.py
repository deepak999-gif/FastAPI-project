from typing_extensions import Annotated

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, computed_field, field_validator, model_validator
from typing import Literal
import json
app=FastAPI()
@app.get("/")
def home():
    return{'message':'Hello Welcome To this FastAPI Application'}

def load_data():
    with open ("patients.json","r") as f:
        data=json.load(f)
        return data

@app.get('/patients')
def get_patients(patient_id):
    data=load_data()
    patients=data['patients']
    for patient in patients:
      if patient['patient_id']==patient_id:
        return patient
    else:
        raise HTTPException(status_code=404,detail='Patient not found')
class Patient(BaseModel):
    patient_id:Annotated[str,Field(...,description="Unique identifier for the patient")]
    name:Annotated[str,Field(...,max_length=100,description="Name of the patient")]
    city:Annotated[str,Field(...,max_length=50,description="City of residence")]
    age:Annotated[int,Field(...,ge=0,le=120,description="Age of the patient")]
    gender:Annotated[Literal['Male','Female','Other'],Field(...,description='Gender of Patient')] 
    height:Annotated[float,Field(...,ge=0,description="Height of the patient in centimeters")]
    weight:Annotated[float,Field(...,ge=0,description="Weight of the patient in kilograms")]
    @field_validator('patient_id')
    @classmethod
    def patient_id_validator(cls,value):
      if value.startswith('P') and value[1:].isdigit():
                return value
      else:
          raise ValueError('Invalid patient ID format')
    @field_validator('name')
    @classmethod
    def name_validator(clas,value):
      if value[0].isupper():
        return value
      else:
        raise ValueError('Name must start with a capital letter')
        
    @computed_field
    @property
    def bmi(self)->float:
        height_in_meters=self.height/100
        bmi=self.weight/(height_in_meters**2)
        return round(bmi,2)
    @computed_field
    @property
    def health_risk(self)->str:
        if self.bmi<18.5:
            return 'Underweight'
        elif 18.5<=self.bmi<25:
            return 'Normal weight'
        elif 25<=self.bmi<30:
            return 'Overweight'
        else:
            return 'Obese'
    @model_validator(mode='after')
    def validate_height_weight(self):
        if self.height>180 and self.weight<20:
            raise ValueError('Height and weight values are inconsistent')
        elif self.height<100 and self.weight>200:
            raise ValueError('Height and weight values are inconsistent')
        else:
            return self
            
    @model_validator(mode='before')
    def height_age_validator(cls,data):
        height=data['height']
        age=data['age']
        if height>180 and age<18:
            raise ValueError('Height is unusually high for a patient under 18')
        elif height<100 and age>60:
             raise ValueError('Height is unusually low for a patient over 60')
        else:
            return data
            
@app.post('/create_patient')
def create_patient(patient: Patient):
    data=load_data()
    patients=data['patients']
    for i in patients:
        if i['patient_id']==patient.patient_id:
            raise HTTPException(status_code=400,detail='Patient with this ID already exists')
        
    new_patient=patient.dict()
    patients.append(new_patient)
    with open('patients.json','w') as f:
      json.dump(data,f,indent=4)
    return {
        'message': 'Patient created successfully',
        'patient': new_patient
    }
    
from typing import Optional
from typing_extensions import Annotated

class PatientUpdate(BaseModel):

    name: Annotated[
        Optional[str],
        Field(default=None, max_length=100)
    ]

    city: Annotated[
        Optional[str],
        Field(default=None, max_length=50)
    ]

    age: Annotated[
        Optional[int],
        Field(default=None, ge=0, le=120)
    ]

    gender: Annotated[
        Optional[Literal['Male', 'Female', 'Other']],
        Field(default=None)
    ]

    height: Annotated[
        Optional[float],
        Field(default=None, ge=0)
    ]

    weight: Annotated[
        Optional[float],
        Field(default=None, ge=0)
    ]


@app.put('/update_patient/{patient_id}')
def update_patient(
    patient_id: str,
    updated_data: PatientUpdate
):

    data = load_data()

    patients = data['patients']

    for patient in patients:

        if patient['patient_id'] == patient_id:

            updated_fields = updated_data.model_dump(
                exclude_unset=True
            )

            patient.update(updated_fields)

            with open('patients.json', 'w') as f:
                json.dump(data, f, indent=4)

            return {
                'message': 'Patient updated successfully',
                'updated_patient': patient
            }

    raise HTTPException(
        status_code=404,
        detail='Patient not found'
    )            
@app.delete('/delete_patients/{patient_id}')
def delete_patient(patient_id: str):

    data = load_data()

    patients = data['patients']

    for index, patient in enumerate(patients):

        if patient['patient_id'] == patient_id:

            deleted_patient = patients.pop(index)

            with open('patients.json', 'w') as f:
                json.dump(data, f, indent=4)

            return {
                'message': 'Patient deleted successfully',
                'deleted_patient': deleted_patient
            }

    raise HTTPException(
        status_code=404,
        detail='Patient not found'
    )     
    
      
        
    
        
