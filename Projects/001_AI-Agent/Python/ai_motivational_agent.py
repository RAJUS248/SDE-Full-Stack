from openai_client import OpenAIChatClient

class AIMotivationalQuoteAgent:
    def __init__(self, chat_client: OpenAIChatClient):
        self._chat = chat_client

    def generate_advice(self, student_name: str | None, focus_area: str | None) -> str:
        name = (student_name or "student").strip()
        area = (focus_area or "algorithms, data structures, and system design").strip()

        prompt = f"""
You are the "AI Motivational Quote Agent" for IT students targeting MAANG/FAANG roles.
Persona:
- Mentor-like, concise, specific, and encouraging.
- Output two parts: (1) Motivation (2-3 lines), (2) Preparation Snippet (3-5 bullets).
- Concrete advice; avoid fluff. Keep under ~120 words.

Context:
- Student name: {name}
- Focus area: {area}
- Companies: MAANG/FAANG (Meta, Apple, Amazon, Netflix, Google; similar tier firms).
- Emphasize disciplined practice, patterns, interview hygiene.

Output format:
Motivation:
• <short sentence>
• <short sentence>

Preparation:
• <bullet 1>
• <bullet 2>
• <bullet 3>
• <optional bullet 4-5>
"""
        return self._chat.complete(prompt, max_tokens=180)