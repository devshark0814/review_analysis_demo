from typing import Optional
from pydantic import BaseModel, Field

class ScrapingSettingRakuten(BaseModel):
    shohin_id  : str = Field(..., title="商品ID", example="212142_10126692")
    repeat     : int = Field(..., title="繰り返し回数", example=1)

class ScrapingResult(BaseModel):
    page_url   : str = Field(..., title="ベースURL", example="212142_10126692")