from pydantic import BaseModel


class PaginatedListField:
    TOTAL_COUNT: str = "total_count"
    COUNT: str = "count"
    LIMIT: str = "limit"
    OFFSET: str = "offset"
    RESULTS: str = "results"


class BasePaginatedList(BaseModel):
    total_count: int
    count: int
    limit: int
    offset: int
