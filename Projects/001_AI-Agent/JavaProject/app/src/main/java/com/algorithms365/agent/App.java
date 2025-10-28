package com.algorithms365.agent;

import com.openai.models.ChatModel;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.time.LocalDateTime;
import java.util.Optional;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * CLI entry point:
 * - Optional args: studentName, focusArea
 * - Invokes agent and writes output to gpt_output.txt (UTF-8)
 * - Robust try/catch and logging
 */
public class App {
    private static final Logger LOG = Logger.getLogger(App.class.getName());

    public static void main(String[] args) {
        // Guard: API key must exist
        if (System.getenv("OPENAI_API_KEY") == null) {
            LOG.severe("OPENAI_API_KEY is not set.");
            System.err.println("ERROR: Set OPENAI_API_KEY in your environment before running.");
            System.exit(1);
        }

        OpenAIChatClient client = new OpenAIChatClient(ChatModel.GPT_4_1);

        // Modes:
        // - "motivational" [studentName] [focusArea]
        // - "modi" [theme] [count]
        // Backward compatibility: if first arg isn't a known mode, treat as motivational studentName/focusArea.
        String mode = (args.length >= 1 && !args[0].isBlank()) ? args[0].toLowerCase() : "motivational";
        boolean legacyMotivational = !("motivational".equals(mode) || "modi".equals(mode));

        try {
            Path out = Paths.get("gpt_output.txt");

            if (legacyMotivational || "motivational".equals(mode)) {
                String studentName;
                String focusArea;
                if (legacyMotivational) {
                    studentName = (args.length >= 1 && !args[0].isBlank()) ? args[0] : "student";
                    focusArea   = (args.length >= 2 && !args[1].isBlank()) ? args[1] : "DSA and System Design";
                } else {
                    studentName = (args.length >= 2 && !args[1].isBlank()) ? args[1] : "student";
                    focusArea   = (args.length >= 3 && !args[2].isBlank()) ? args[2] : "DSA and System Design";
                }

                AIMotivationalQuoteAgent agent = new AIMotivationalQuoteAgent(client);
                String advice = agent.generateAdvice(studentName, focusArea);
                writeUtf8(out, advice);
                LOG.info(() -> "Motivational advice written to: " + out.toAbsolutePath());
                System.out.println("SUCCESS: Wrote advice to " + out.toAbsolutePath());

            } else if ("modi".equals(mode)) {
                String theme = (args.length >= 2 && !args[1].isBlank()) ? args[1] : "nation-building and personal responsibility";
                int count = 3;
                if (args.length >= 3 && !args[2].isBlank()) {
                    try {
                        count = Integer.parseInt(args[2]);
                    } catch (NumberFormatException ignored) {
                        count = 3;
                    }
                }
                count = Math.max(1, Math.min(count, 5));

                AIModiQuoteAgent modiAgent = new AIModiQuoteAgent(client);
                String quotes = modiAgent.generateModiQuotes(theme, count);
                writeUtf8(out, "AI Modi Quotes", quotes);
                LOG.info(() -> "Modi quotes written to: " + out.toAbsolutePath());
                System.out.println("SUCCESS: Wrote Modi quotes to " + out.toAbsolutePath());
            }

        } catch (RuntimeException ex) { // OpenAI / runtime errors
            LOG.log(Level.SEVERE, "AI generation failed: " + ex.getMessage(), ex);
            System.err.println("ERROR: " + ex.getMessage());
            System.exit(2);

        } catch (Exception ex) { // last-resort
            LOG.log(Level.SEVERE, "Unexpected error: " + ex.getMessage(), ex);
            System.err.println("FATAL: " + ex.getMessage());
            System.exit(3);
        }
    }

    private static void writeUtf8(Path path, String content) throws IOException {
        String header = """
                =========================
                AI Motivational Quote Agent
                Timestamp: %s
                =========================

                """.formatted(LocalDateTime.now());

        try {
            Files.writeString(path, header + content + System.lineSeparator(), StandardCharsets.UTF_8,
                    StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING, StandardOpenOption.WRITE);
        } catch (NoSuchFileException nsf) {
            if (path.getParent() != null) {
                Files.createDirectories(path.getParent());
                Files.writeString(path, header + content + System.lineSeparator(), StandardCharsets.UTF_8,
                        StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING, StandardOpenOption.WRITE);
            } else {
                throw nsf;
            }
        }
    }

    private static void writeUtf8(Path path, String title, String content) throws IOException {
        String header = """
                =========================
                %s
                Timestamp: %s
                =========================

                """.formatted(title, LocalDateTime.now());

        try {
            Files.writeString(path, header + content + System.lineSeparator(), StandardCharsets.UTF_8,
                    StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING, StandardOpenOption.WRITE);
        } catch (NoSuchFileException nsf) {
            if (path.getParent() != null) {
                Files.createDirectories(path.getParent());
                Files.writeString(path, header + content + System.lineSeparator(), StandardCharsets.UTF_8,
                        StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING, StandardOpenOption.WRITE);
            } else {
                throw nsf;
            }
        }
    }
}