# Packaging Java Software for Standalone Apps — A Beginner-Friendly, Industry-Style Guide

**Audience:** CS/CE students who can write small Java programs and want to learn how *real* projects are built, packaged, and shipped — using the Java **standard library** + **open‑source libraries**, and modern **build systems**.

> **Goal:** Understand how source code becomes **binaries** (JARs, fat/uber JARs, native installers), how build tools pull in dependencies, and how a **multi‑module** project is structured and shipped — just like in industry.

---

## 1) Why Packaging & Build Systems Matter

In professional software, your customer (or server) usually receives **binaries**, not your source code. The build process must:
- **Compile** Java sources into `.class` files.
- **Resolve dependencies** (standard + open‑source libraries from Maven Central).
- **Assemble** a runnable artifact (JAR, fat JAR, runtime image, installer).
- **Stamp metadata** (version, group, artifact, main class), maybe sign it, and ensure **reproducibility**.
- **Automate** all of the above for local dev, CI, and release pipelines.

**Common packaging formats:**
- **JAR** (Java ARchive): contains compiled classes + metadata.
- **Uber/fat JAR**: a single JAR bundling *your code + all dependencies* (handy for “double‑click to run” or `java -jar`).
- **Custom runtime image** via `jlink`: includes your app + minimal JRE modules.
- **Native installers** via `jpackage`: platform‑native EXE/MSI (Windows), PKG/DMG (macOS), DEB/RPM (Linux).

> We’ll stick to **Java 17 (LTS)** in examples, and show both **Maven** and **Gradle** — the two most popular build systems. (Ant is legacy; still used in places, but less common for new projects.)

---

## 2) Popular Java Build Systems (Quick Overview)

| Build System | Why People Use It | Typical Use Today |
|---|---|---|
| **Maven** | Convention over configuration, XML, massive plugin ecosystem, deterministic dependency resolution | Enterprise apps, libraries, very common |
| **Gradle** | Flexible, fast incremental builds, Groovy/Kotlin DSL, top‑notch IDE integration | Microservices, Android, modern server apps |
| **Ant** | Script‑like, explicit steps | Legacy or custom pipelines |

> Both Maven and Gradle pull dependencies from **Maven Central**, cache them locally, and support multi‑module builds, tests, packaging, and publishing.

---

## 3) What We’ll Build (Hands‑On)

A **multi‑module** project with two modules:

- `core` — library module with 2 classes:
  - `ConfigLoader` — reads a text file using **Apache Commons IO** (open‑source library).
  - `Greeter` — formats a greeting.
- `app` — application module with 1 class:
  - `Main` — uses `core` to print a greeting + file content.

We’ll show **both Maven and Gradle** setups. You can copy either.

### 3.1 Project layout (generic)
```
java-packaging-demo/
├─ README.md
├─ pom.xml                   (Maven parent)         # or build.gradle/settings.gradle for Gradle
├─ core/
│  ├─ pom.xml               (Maven child)          # or core/build.gradle
│  └─ src/
│     └─ main/java/com/example/core/
│        ├─ ConfigLoader.java
│        └─ Greeter.java
├─ app/
│  ├─ pom.xml               (Maven child)          # or app/build.gradle
│  └─ src/
│     └─ main/java/com/example/app/
│        └─ Main.java
└─ data/
   └─ message.txt           (runtime file for the demo)
```

> Create a `data/message.txt` with:  
> `Hello from Algorithms365 build demo!`

---

## 4) The Code (2 modules, 3 classes)

### 4.1 `core/src/main/java/com/example/core/ConfigLoader.java`
```java
package com.example.core;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;

// Open-source library: Apache Commons IO
import org.apache.commons.io.FileUtils;

/**
 * Loads text content from a file path.
 * Demonstrates using an open-source library (Commons IO).
 */
public final class ConfigLoader {

    private ConfigLoader() { /* static utility */ }

    public static String readText(Path path) throws IOException {
        // Using Commons IO for clarity (works with File/Path)
        return FileUtils.readFileToString(path.toFile(), StandardCharsets.UTF_8);
        // Equivalent with JDK only: return Files.readString(path, StandardCharsets.UTF_8);
    }

    public static boolean exists(Path path) {
        return Files.exists(path);
    }
}
```

### 4.2 `core/src/main/java/com/example/core/Greeter.java`
```java
package com.example.core;

/** Simple greeter to keep the example realistic but small. */
public final class Greeter {

    private Greeter() { }

    public static String greet(String name) {
        return "Hello, " + name + "!";
    }
}
```

### 4.3 `app/src/main/java/com/example/app/Main.java`
```java
package com.example.app;

import com.example.core.ConfigLoader;
import com.example.core.Greeter;

import java.io.IOException;
import java.nio.file.Path;

/** Entry point of the application. */
public final class Main {

    public static void main(String[] args) throws IOException {
        System.out.println(Greeter.greet("Algorithms365"));

        Path messagePath = Path.of("data/message.txt");
        String content = ConfigLoader.readText(messagePath);
        System.out.println("File content:");
        System.out.println(content);
    }
}
```

---

## 5) Maven Setup (Multi‑Module + Fat JAR)

### 5.1 Parent `pom.xml` (aggregator + shared config)
```xml
<!-- java-packaging-demo/pom.xml -->
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.example</groupId>
  <artifactId>java-packaging-demo</artifactId>
  <version>1.0.0</version>
  <packaging>pom</packaging>

  <properties>
    <maven.compiler.release>17</maven.compiler.release>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <commons-io.version>2.16.1</commons-io.version> <!-- use latest stable in real projects -->
  </properties>

  <modules>
    <module>core</module>
    <module>app</module>
  </modules>
</project>
```

### 5.2 `core/pom.xml`
```xml
<!-- java-packaging-demo/core/pom.xml -->
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <parent>
    <groupId>com.example</groupId>
    <artifactId>java-packaging-demo</artifactId>
    <version>1.0.0</version>
  </parent>

  <artifactId>core</artifactId>
  <packaging>jar</packaging>

  <dependencies>
    <dependency>
      <groupId>commons-io</groupId>
      <artifactId>commons-io</artifactId>
      <version>${commons-io.version}</version>
    </dependency>
  </dependencies>
</project>
```

### 5.3 `app/pom.xml` (depends on `core`, builds **fat JAR**)
```xml
<!-- java-packaging-demo/app/pom.xml -->
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <parent>
    <groupId>com.example</groupId>
    <artifactId>java-packaging-demo</artifactId>
    <version>1.0.0</version>
  </parent>

  <artifactId>app</artifactId>
  <packaging>jar</packaging>

  <dependencies>
    <dependency>
      <groupId>com.example</groupId>
      <artifactId>core</artifactId>
      <version>${project.version}</version>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <!-- Add Main-Class to MANIFEST.MF -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-jar-plugin</artifactId>
        <version>3.4.1</version>
        <configuration>
          <archive>
            <manifest>
              <mainClass>com.example.app.Main</mainClass>
            </manifest>
          </archive>
        </configuration>
      </plugin>

      <!-- Create a fat/uber JAR with all dependencies bundled -->
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-shade-plugin</artifactId>
        <version>3.5.0</version>
        <executions>
          <execution>
            <phase>package</phase>
            <goals>
              <goal>shade</goal>
            </goals>
            <configuration>
              <createDependencyReducedPom>true</createDependencyReducedPom>
              <shadedArtifactAttached>true</shadedArtifactAttached>
              <transformers>
                <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                  <mainClass>com.example.app.Main</mainClass>
                </transformer>
              </transformers>
            </configuration>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
</project>
```

### 5.4 Build & run with Maven
```bash
# at the repository root
mvn -v                 # check Maven
mvn -q -DskipTests package

# Run the fat jar (name may include classifier like -shaded)
java -jar app/target/app-1.0.0-shaded.jar
```

Expected output:
```
Hello, Algorithms365!
File content:
Hello from Algorithms365 build demo!
```

---

## 6) Gradle Setup (Multi‑Project + Distribution / Shadow JAR)

If you prefer **Gradle**, use this layout and files instead of the Maven ones.

### 6.1 `settings.gradle`
```gradle
rootProject.name = 'java-packaging-demo'
include('core', 'app')
```

### 6.2 Root `build.gradle` (shared config)
```gradle
plugins {
    id 'java'
}

allprojects {
    group = 'com.example'
    version = '1.0.0'

    repositories {
        mavenCentral()
    }
}

subprojects {
    apply plugin: 'java'

    java {
        toolchain {
            languageVersion = JavaLanguageVersion.of(17)
        }
    }

    tasks.withType(JavaCompile).configureEach {
        options.encoding = 'UTF-8'
    }
}
```

### 6.3 `core/build.gradle`
```gradle
dependencies {
    implementation 'commons-io:commons-io:2.16.1' // use latest stable in real projects
}
```

### 6.4 `app/build.gradle` (depends on `core`)

**Option A: Run via `application` plugin (no fat JAR yet):**
```gradle
plugins {
    id 'application'
}

dependencies {
    implementation project(':core')
}

application {
    mainClass = 'com.example.app.Main'
}
```

Run:
```bash
./gradlew :app:run
```

**Option B: Create a fat JAR with Shadow plugin:**
```gradle
plugins {
    id 'application'
    id 'com.github.johnrengelman.shadow' version '8.1.1'
}

dependencies {
    implementation project(':core')
}

application {
    mainClass = 'com.example.app.Main'
}

tasks.named('shadowJar') {
    archiveClassifier = 'all' // app-1.0.0-all.jar
}
```

Build & run the fat JAR:
```bash
./gradlew :app:shadowJar
java -jar app/build/libs/app-1.0.0-all.jar
```

---

## 7) Beyond JARs: Custom Runtime & Native Installers

For desktop apps or locked‑down servers, shipping a **self‑contained runtime** helps avoid “works on my machine”:

- **`jlink`** (Java 9+): build a custom, minimized JRE containing only the modules your app needs.
- **`jpackage`** (Java 14+): build native installers (`.msi`, `.pkg/.dmg`, `.deb/.rpm`).

**Example (conceptual):**
```bash
# Create a runtime image (requires modularized app or add-modules list)
jlink --add-modules java.base,java.desktop \
      --output build/runtime-image

# Package native installer (when configured)
jpackage --name MyApp \
         --input app/target \
         --main-jar app-1.0.0-shaded.jar \
         --type dmg   # or msi, pkg, deb, rpm
```

Gradle has the **org.beryx.jlink** plugin, and Maven has jlink/jpackage plugins as well.

---

## 8) Key Concepts You’ll See in Industry

- **Coordinates**: Each artifact has `groupId:artifactId:version` (e.g., `commons-io:commons-io:2.16.1`).
- **Dependency scopes/configurations**: `implementation`, `testImplementation` (Gradle) or `compile`, `test` (Maven Classic) — define where deps apply.
- **Semantic versioning**: `MAJOR.MINOR.PATCH`. Lock versions to avoid surprises; update intentionally.
- **Reproducible builds**: pin versions, prefer deterministic plugins, use CI to build/tag/sign artifacts.
- **Main‑Class** manifest**:** enables `java -jar myapp.jar`.
- **Multi‑module**: shared code (`core`) vs runnable app (`app`). Keeps responsibilities clean.
- **Only binaries shipped**: servers/clients get JARs/containers/installers, not your `.java` files.

---

## 9) Common Pitfalls (and How to Avoid Them)

1. **Forgetting the Main‑Class** → your JAR isn’t runnable.  
2. **Classpath conflicts** → use fat JAR plugins that merge manifests correctly; avoid duplicate classes.  
3. **Missing runtime files** → include external resources in a known path (`data/`) or bundle them as classpath resources.  
4. **Unpinned dependency versions** → builds break later; pin versions explicitly.  
5. **Different Java versions** → set toolchains (Maven/Gradle) to Java 17 for consistency.  
6. **Shadow/Shade collisions** → if two dependencies have same resources, configure relocations/merge strategies.  

---

## 10) Quick Start Checklist

- [ ] Install **JDK 17** and **Maven** or **Gradle**  
- [ ] Create the project structure and Java classes  
- [ ] Add **Commons IO** dependency in `core`  
- [ ] Wire `app` → `core` dependency  
- [ ] Configure **Main‑Class** & **fat JAR** (Shade or Shadow)  
- [ ] `mvn package` or `./gradlew :app:shadowJar`  
- [ ] Run: `java -jar app/target/app-1.0.0-shaded.jar` or `app/build/libs/app-1.0.0-all.jar`  

---

## 11) What You’ve Learned

- How modern Java projects pull **open‑source libraries** and combine them with the **standard library**.
- How **Maven** and **Gradle** structure **multi‑module** builds (library module + application module).
- How to **package binaries** you can ship to servers/clients (JARs, fat JARs), and where to go next (jlink/jpackage).

> Next steps: add unit tests (JUnit 5), enable CI (GitHub Actions), and practice publishing artifacts to a private or public repository.
