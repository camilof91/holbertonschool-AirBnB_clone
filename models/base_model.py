import uuid
from datetime import datetime

class BaseModel:
    def __init__():
        id = uuid.uuid4()



    def __str__(self):
        """
        Returns the form in which the information should be printed
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"         
    
    def save(self):
        """
        Save the date current
        """
        self.update_at = datetime.now()