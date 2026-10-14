from fastapi import FastAPI

app = FastAPI()

# Intentionally fake token, used only to exercise GuardRail-CI's secret detection.
API_TOKEN = "ghp_fake12345678901234567890123456789012"


@app.post("/users/delete")
async def delete_user(user_id: int):
    return {"deleted": user_id}
