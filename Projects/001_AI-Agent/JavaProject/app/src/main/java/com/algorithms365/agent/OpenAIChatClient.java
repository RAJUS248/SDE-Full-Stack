package com.algorithms365.agent;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.ChatModel;
import com.openai.models.chat.completions.ChatCompletion;
import com.openai.models.chat.completions.ChatCompletionCreateParams;

import java.time.Duration;
import java.util.Objects;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * Thin wrapper around the OpenAI Java SDK for chat completions.
 * - Centralizes client creation and configuration (timeouts).
 * - Single method to request a completion and return text.
 */
public class OpenAIChatClient {
    private static final Logger LOG = Logger.getLogger(OpenAIChatClient.class.getName());
    private final OpenAIClient client;
    private final ChatModel defaultModel;

    public OpenAIChatClient(ChatModel defaultModel) {
        this.client = OpenAIOkHttpClient.fromEnv();
        this.defaultModel = Objects.requireNonNull(defaultModel, "defaultModel must not be null");
    }

    /**
     * Send a user prompt and return the first choice text.
     * @param prompt user text
     * @param maxTokens maximum tokens (nullable => default 200)
     * @return trimmed response text
     * @throws RuntimeException on network/auth/model errors
     */
    public String complete(String prompt, Long maxTokens) {
        try {
            ChatCompletionCreateParams params = ChatCompletionCreateParams.builder()
                .addUserMessage(prompt)
                .model(defaultModel)
                .maxTokens(maxTokens != null ? maxTokens : 200L)
                .build();

            ChatCompletion completion = client.chat().completions().create(params);

            if (completion.choices() == null || completion.choices().isEmpty()) {
                throw new RuntimeException("OpenAI response had no choices.");
            }
            String text = completion.choices().get(0).message().content().orElseThrow(() -> new RuntimeException("OpenAI response content was null."));
            if (text == null) {
                throw new RuntimeException("OpenAI response content was null.");
            }
            return text.trim();

        } catch (Exception ex) {
            LOG.log(Level.SEVERE, "OpenAI chat completion failed: " + ex.getMessage(), ex);
            throw new RuntimeException(
                "Failed to get a response from OpenAI. " +
                "Check OPENAI_API_KEY, network, and model access.", ex);
        }
    }
}