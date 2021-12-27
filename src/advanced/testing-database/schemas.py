from typing import List, Optional

from pydantic import BaseModel

# 作成に必要な追加のデータ（属性）を作成
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

# 作成に必要な追加のデータ（属性）を作成
class ItemCreate(ItemBase):
    pass

# APIからデータを返すときに、データを読み取るときに使用されるPydanticモデル（スキーマ）
class Item(ItemBase):
    id: int
    owner_id: int
    # ORMを利用する
    class Config:
        orm_mode = True

# 作成に必要な追加のデータ（属性）を作成
class UserBase(BaseModel):
    email: str

# 作成に必要な追加のデータ（属性）を作成
class UserCreate(UserBase):
    password: str

# APIからデータを返すときに、データを読み取るときに使用されるPydanticモデル（スキーマ）
# passwordは返却しない
class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    # ORMを利用する
    class Config:
        orm_mode = True
