from fastapi import APIRouter

router = APIRouter()


@router.get("/test")
def test():
    return {"bang": "seungjae"}