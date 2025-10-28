package com.algorithms365.agent;

import java.util.Objects;

/**
 * Agent that generates short inspirational quotes in the style of Narendra Modi.
 */
public class AIModiQuoteAgent {

    private final OpenAIChatClient chatClient;

    public AIModiQuoteAgent(OpenAIChatClient chatClient) {
        this.chatClient = Objects.requireNonNull(chatClient);
    }

    /**
     * Generate one or more concise Modi-style quotes around a given theme.
     * @param theme optional theme (e.g., "leadership", "nation-building", "youth", "innovation")
     * @param count number of quotes to produce (1-5 recommended)
     * @return formatted string with each quote on its own line, prefixed by a bullet
     */
    public String generateModiQuotes(String theme, int count) {
        String safeTheme = (theme == null || theme.isBlank()) ? "nation-building and personal responsibility" : theme.trim();
        int safeCount = Math.max(1, Math.min(count, 5));

        String prompt = """
            You are to produce %d concise inspirational quotes in the rhetorical style of an Indian statesman.
            Constraints:
            - Keep each quote one sentence, 8-18 words.
            - Tone: visionary, optimistic, collective progress, self-reliance, duty, unity.
            - Avoid direct references to specific individuals; keep it universal and timeless.
            - Avoid political partisanship; keep it uplifting and apolitical.
            - Theme to weave in: %s.

            Output format:
            • <quote 1>
            • <quote 2>
            • <quote 3>
            (Only include exactly %d bullet lines, no extra text.)
            """.formatted(safeCount, safeTheme, safeCount);

        return chatClient.complete(prompt, 180L);
    }
}



