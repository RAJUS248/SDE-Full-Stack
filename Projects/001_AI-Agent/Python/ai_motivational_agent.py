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

    def generate_modi_quote(self, topic: str | None = None) -> str:
        """
        Generate a short, original inspirational quote inspired by public themes often associated
        with Narendra Modi (leadership, national development, discipline, vision). This should
        NOT attempt to impersonate or reproduce exact historical quotes. Instead, produce an
        original, concise quote (1-2 sentences) and append a short attribution line like
        "— Inspired by Narendra Modi" so the origin is clear.

        `topic` may be used to steer the topic of the quote (e.g., "service", "discipline").
        """

        steer = f" about {topic}" if topic else ""
        prompt = f"""
Write a single, original, inspirational quote{steer} that is concise (1-2 sentences). The quote
should be uplifting, leadership-focused, and practical. Do NOT impersonate or claim to be an
actual quote from any real person. After the quote, add a short attribution line exactly like
this (without additional text):

— Inspired by Narendra Modi

Keep the whole output to no more than 40 words total.
"""

        return self._chat.complete(prompt, max_tokens=80)