from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn  # 👈 추가

app = FastAPI()

# 자연어 처리 함수 (지금은 키워드 기반)
def predict_intent(text: str) -> str:
    if "여권" in text:
        return "여권_발급"
    elif "쓰레기" in text or "배출" in text:
        return "쓰레기_배출"
    elif "주차" in text:
        return "불법주차"
    else:
        return "기타"

class RequestBody(BaseModel):
    text: str

@app.post("/classify")
def classify_text(body: RequestBody):
    intent = predict_intent(body.text)
    return {"intent": intent}

# 👇 이거 추가 (자동 서버 실행용)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
