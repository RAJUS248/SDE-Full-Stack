# Java Libraries for File & Network I/O — An Intro with Two Practical Examples

**Audience:** Beginner Computer Science students learning Java and curious about how to use libraries to accomplish common real-world tasks.

---

## Why Libraries? (And Why This Matters)
- Early Java (and older languages like C) required verbose, manual code for reading files or network sockets.  
- Today, **libraries** (standard and open-source) provide:
  - Cleaner APIs.
  - Cross-platform consistency.
  - Faster development.  

**Two types of libraries:**
- **Standard library (JDK)**: Built into Java (e.g., `java.nio.file` for files, `java.net.http` or older `java.net` for networking).
- **Open-source libraries**: Published by the community on Maven Central (e.g., `OkHttp` for HTTP, Apache Commons for utilities).  

> Key skill: Learn how to **use** libraries and **find documentation** (not memorize every method).

---

## Example 1 — Read a Text File and Print It (Standard Library: `java.nio.file`)

```java
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.io.IOException;

public class FileReadExample {

    // Utility method to read file content into a String
    public static String readTextFile(Path path) throws IOException {
        return Files.readString(path); // UTF-8 by default
    }

    public static void main(String[] args) throws IOException {
        Path dataDir = Paths.get("data");
        Path filePath = dataDir.resolve("notes.txt");

        // Create directory and starter file if not present
        if (!Files.exists(dataDir)) {
            Files.createDirectories(dataDir);
        }
        if (!Files.exists(filePath)) {
            Files.writeString(filePath, "Hello from Algorithms365!\n");
        }

        String content = readTextFile(filePath);
        System.out.println(content);
    }
}
```

**What to notice:**
- `Path` and `Files` (from `java.nio.file`) are the modern way to work with files.  
- The code is short and clear, compared to older `FileReader`/`BufferedReader` APIs.  
- We deliberately **don’t add try/catch yet** — this is just to understand the library usage.

---

## Example 2 — Make an HTTP GET Request and Print the Response (Open-Source: OkHttp)

To use **OkHttp** (a popular HTTP client):  
- Add it to your project via **Maven** or **Gradle**.  
  - Maven:
    ```xml
    <dependency>
      <groupId>com.squareup.okhttp3</groupId>
      <artifactId>okhttp</artifactId>
      <version>4.12.0</version>
    </dependency>
    ```
  - Gradle:
    ```gradle
    implementation("com.squareup.okhttp3:okhttp:4.12.0")
    ```

```java
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import java.io.IOException;

public class NetworkRequestExample {

    // Utility method to fetch URL content as a String
    public static String fetchText(String url) throws IOException {
        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder()
                .url(url)
                .build();

        // Try-with-resources auto-closes the Response
        try (Response response = client.newCall(request).execute()) {
            return response.body().string();
        }
    }

    public static void main(String[] args) throws IOException {
        String url = "https://httpbin.org/get";
        String body = fetchText(url);
        System.out.println(body);
    }
}
```

**What to notice:**
- `OkHttp` is much simpler and more ergonomic than the low-level `HttpURLConnection`.  
- The client manages connections and makes the call in just a few lines.  
- Again, no exception handling yet — focus on **basic API usage**.

---

## How to Learn (Don’t Memorize — Search Smart)
- **Standard library docs**: https://docs.oracle.com/en/java/javase/ (look up `java.nio.file.Files` or `Path`).  
- **Open-source libraries**: Search on https://mvnrepository.com/ (e.g., “okhttp”).  
- Skim official GitHub README or docs for usage snippets.

---

## Mini-Checklist for Professional Style
- Use **clear class/method names** (`FileReadExample`, `readTextFile`, `fetchText`).  
- Keep each method focused on one task.  
- Use **JavaDoc comments** for reusable methods.  
- Stick to modern APIs (`java.nio.file`, `OkHttp`) instead of legacy ones.  

---

## Practice Ideas
1. Change the file name and starter text, then re-run.  
2. Fetch a different URL (e.g., a public JSON API like `https://api.github.com`) and print only the first 200 characters.  
3. Try using the JDK’s built-in `HttpClient` instead of OkHttp to compare.  

---

✅ With these two examples, you’ve seen how **Java libraries** (standard and open-source) make it easy to handle files and networks in a clean, modern way.  
