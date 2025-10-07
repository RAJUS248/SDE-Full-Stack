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
        String studentName = (args.length >= 1 && !args[0].isBlank()) ? args[0] : "student";
        String focusArea   = (args.length >= 2 && !args[1].isBlank()) ? args[1] : "DSA and System Design";

        // Guard: API key must exist
        if (System.getenv("OPENAI_API_KEY") == null) {
            LOG.severe("OPENAI_API_KEY is not set.");
            System.err.println("ERROR: Set OPENAI_API_KEY in your environment before running.");
            System.exit(1);
        }

        OpenAIChatClient client = new OpenAIChatClient(ChatModel.GPT_4_1);
        AIMotivationalQuoteAgent agent = new AIMotivationalQuoteAgent(client);

        try {
            String advice = agent.generateAdvice(studentName, focusArea);
            Path out = Paths.get("gpt_output.txt");
            writeUtf8(out, advice);
            LOG.info(() -> "Advice generated and written to: " + out.toAbsolutePath());
            System.out.println("SUCCESS: Wrote advice to " + out.toAbsolutePath());

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
}