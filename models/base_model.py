import uuid

class BaseModel:
    def __init__():
        id = uuid.uuid4()

    def __str__():
        return 
    
    def save(self):
        return
    
    def _to_dict(self):
        """Convert the instance to a dictionary.

    Returns:
        dict: A dictionary containing all attributes of the instance.
    """
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()  
        
        self.__dict__["__class__"] = self.__class__.__name__
        
        return self.__dict__
