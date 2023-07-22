from fastapi import FastAPI
from domain.separate import separate_router
from domain.image import image_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(separate_router.router)
app.include_router(image_router.router)
