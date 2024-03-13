import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


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
    
    def _to_dict(self):
        """Convert the instance to a dictionary.

    Returns:
        dict: A dictionary containing all attributes of the instance.
    """
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()  
        
        self.__dict__["__class__"] = self.__class__.__name__
        
        return self.__dict__

