from pydoc import text
from pydantic import BaseModel, Field

class SimpleMecabResultModel(BaseModel):
    text  : str = Field(..., title="一文", example="もうかなりお世話に成っています、これからもよろしくお願いします。")