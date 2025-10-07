package com.algorithms365.agent;

import java.util.Objects;

/**
 * Agent that generates a short motivational + preparation snippet
 * for IT students targeting MAANG/FAANG interviews.
 */
public class AIMotivationalQuoteAgent {

    private final OpenAIChatClient chatClient;

    public AIMotivationalQuoteAgent(OpenAIChatClient chatClient) {
        this.chatClient = Objects.requireNonNull(chatClient);
    }

    /**
     * Build a focused prompt with persona and constraints, then call OpenAI.
     * @param studentName optional personalization
     * @param focusArea   e.g., "DSA and System Design"
     */
    public String generateAdvice(String studentName, String focusArea) {
        String name = (studentName == null || studentName.isBlank()) ? "student" : studentName.trim();
        String area = (focusArea == null || focusArea.isBlank()) ? "algorithms, data structures, and system design" : focusArea.trim();

        String prompt = """
            You are the "AI Motivational Quote Agent" for IT students targeting MAANG/FAANG roles.
            Persona:
            - Mentor-like, concise, specific, and encouraging.
            - Output two parts: (1) Motivation (2-3 lines), (2) Preparation Snippet (3-5 bullets).
            - Concrete advice; avoid fluff. Keep under ~120 words.

            Context:
            - Student name: %s
            - Focus area: %s
            - Companies: MAANG/FAANG (Meta, Apple, Amazon, Netflix, Google; plus similar tier orgs).
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
            """.formatted(name, area);

        return chatClient.complete(prompt, 180L);
    }
}