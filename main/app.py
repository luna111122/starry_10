from dotenv import load_dotenv
import os
from openai import OpenAI
from flask import Flask

# .env 파일에서 API 키 로드
load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def stream_chatgpt_response(diary_content):
    """사용자의 일기 내용에 대해 스트리밍 응답을 제공하는 함수"""
    try:


        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an empathetic mentor and a scientific advisor. "
            "When responding to the user's diary entry, provide emotional support and understanding. "
            "Additionally, include scientifically-backed advice or facts to help the user improve their well-being. "
            "Your tone should be kind, thoughtful, and balanced between empathy and practical guidance."},
                {"role": "user", "content": diary_content}
            ],
            model="gpt-3.5-turbo",
        )

        print("\n=== 피드백 시작 ===\n")

        print(response.choices[0].message.content)


    except Exception as e:
        print(f"오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    # 사용자로부터 일기 입력 받기
    diary_entry = input("오늘의 일기를 입력하세요: ")
    # 스트리밍 응답 실행
    stream_chatgpt_response(diary_entry)