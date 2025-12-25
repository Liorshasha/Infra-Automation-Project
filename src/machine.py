from pydantic import BaseModel ,ValidationError, field_validator
import logging

logging.basicConfig(level=logging.INFO,filename="./logs/machine.log",
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Machine(BaseModel):
    name: str
    os: str="Windows"
    cores: int=4
    ram: int=16
    disk_space: int=256

#chacking info

    @field_validator ('name')
    def validate_name(cls, value):  
        if not value:
            raise ValueError("Name cannot be empty.")
        if len(value) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        special_characters = set('!@#$%^&*()+=[]{}|\\;:\'",<>/?`~')
        if not special_characters.isdisjoint(value):
            raise ValueError("Name cannot contain special characters.")
        return value
    @field_validator('os')
    def validate_os(cls, value):
        valid_os = ['Windows', 'Linux', 'macOS']
        if value not in valid_os:
            raise ValueError(f"Invalid OS. Choose from {valid_os}.")
        return value
    @field_validator('cores')
    def validate_cores(cls, value):
        if value < 1 or value > 64:
            raise ValueError("Cores must be between 1 and 64.")
        return value
    @field_validator('ram')
    def validate_ram(cls, value):
        if value < 8 or value > 256:
           raise ValueError("RAM must be between 8 and 256 GB.")
        if value % 2 != 0:
           raise ValueError("RAM must be an even number (divisible by 2).")   
        return value    
    @field_validator('disk_space')
    def validate_disk_space(cls, value):
        if value < 100 or value > 1024:
            raise ValueError("Disk space must be between 100 and 1024 GB.")
        return value
      