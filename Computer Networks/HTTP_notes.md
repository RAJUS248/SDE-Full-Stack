
<a id="top"></a>

# HTTP Notes — Versions & Error Codes (with TOC)

> A compact, classroom‑friendly reference that combines **HTTP versions** (what changed & why) and **HTTP error codes** (4xx/5xx).  
> **Standards note:** HTTP is standardized by the **IETF** Internet Engineering Task Force

---

## 📑 Index

1. [HTTP Versions — What Changed & Why](#http-versions)
2. [HTTP Error Codes — Quick Reference (4xx & 5xx)](#http-error-codes)

---

<a id="http-versions"></a>
## HTTP Versions — What Changed & Why

> **Note:** HTTP is defined by the IETF. Key specs: **RFC 9110** (HTTP semantics), **RFC 9111** (caching), **RFC 9112** (HTTP/1.1), **RFC 9113** (HTTP/2), **RFC 9114** (HTTP/3).

| Version | Year (primary spec) | Standards body / Spec | Transport | Key features / changes | What it tried to fix vs. earlier | Status / notes |
|---|---|---|---|---|---|---|
| **HTTP/0.9** | ~1991 (informal) | Early CERN-era docs (no official RFC) | TCP | One-line protocol: `GET /path`, raw HTML only, **no headers/status codes**. | Provide a minimal way to retrieve hypertext. | Historical; not used today. |
| **HTTP/1.0** | 1996 | **IETF RFC 1945** | TCP | Versioned protocol, request/response **headers**, **status codes**, `Content-Type`, basic caching/proxies. Connections usually **close per request**. | Introduced metadata & media types; basic interoperability. | Superseded; many servers still accept 1.0-style requests. |
| **HTTP/1.1** | 1997 (**RFC 2068**), 1999 (**RFC 2616**), 2014 (**RFC 7230–7235**), 2022 (**RFC 9110/9111/9112**) | **IETF** | TCP | **Persistent connections** (keep‑alive) by default, **chunked transfer**, **Host** header (virtual hosting), **range requests**, **100‑continue**, stronger caching & semantics. | Reduce connection overhead; enable virtual hosting; stream bodies without known size. | Current definitions split across RFC **9110/9111/9112**. |
| **HTTP/2** | 2015 (**RFC 7540**), 2022 (**RFC 9113**) | **IETF** | TCP | **Binary framing**, **multiplexing** many streams on one TCP connection, **HPACK** header compression (RFC 7541), stream prioritization, optional **server push**. | Fix **application‑layer HOL** of 1.1 and cut latency without many TCP connections. | Widely deployed; still subject to **TCP HOL** at transport; server push usage reduced. |
| **HTTP/3** | 2022 (**RFC 9114**) | **IETF** | **QUIC over UDP** | Streams map to QUIC (independent loss recovery), **no TCP HOL**, **TLS 1.3 built‑in**, **connection migration** (mobile/NAT), **0‑RTT**, **QPACK** header compression. | Eliminate transport HOL, faster handshakes, better mobility/reliability on lossy paths. | Rapidly adopted by browsers/CDNs; requires QUIC-capable stacks/middleboxes. |

**ECMA context (FYI):** **ECMA‑262** defines ECMAScript (JS). It complements HTTP (browser runtime) but does **not** define the HTTP protocol.

[⬆ Back to top](#top)

---

<a id="http-error-codes"></a>
## HTTP Error Codes — Quick Reference (4xx & 5xx)

| Code | Name | What it means (plain English) | Typical causes | Client action | Server fix / When to return |
|-----:|------|--------------------------------|----------------|---------------|-----------------------------|
| 400 | Bad Request | The server can’t understand the request as sent. | Malformed JSON, invalid query string, wrong field types, bad headers. | Validate & fix request format; check API docs and payload schema. | Validate input early, return precise error body; include field errors. |
| 401 | Unauthorized | No valid authentication credentials provided. | Missing/expired token, wrong auth scheme. | Obtain/refresh token; send `Authorization` header correctly. | Challenge with `WWW-Authenticate`; keep error body minimal to avoid leaking info. |
| 402 | Payment Required | Reserved for future use / payments. Rare in the wild. | Paywall/billing gateways (non-standard). | Follow provider’s billing flow if defined. | Avoid unless your API explicitly documents a payment workflow. |
| 403 | Forbidden | Authenticated but not allowed to perform this action. | Lacking role/permission; IP blocked. | Request appropriate access; try a different account/role. | Enforce authorization; log attempts; don’t reveal sensitive policy details. |
| 404 | Not Found | The resource doesn’t exist at this path. | Wrong URL/ID; removed item. | Check endpoint/ID; handle gracefully in UI. | Use for unknown IDs/paths; avoid revealing what exists vs. not (security). |
| 405 | Method Not Allowed | The resource doesn’t allow this HTTP method. | Using `POST` on a `GET`-only endpoint, etc. | Retry with allowed method. | Include `Allow: GET, POST` header listing supported methods. |
| 406 | Not Acceptable | Server can’t return a representation matching `Accept`. | Client demanded an unsupported content type. | Relax `Accept` header; accept JSON/HTML default. | Offer common formats; implement content negotiation or simplify. |
| 407 | Proxy Authentication Required | A proxy requires authentication. | Corporate proxy, gateway auth. | Provide proxy credentials as required by network. | Return `Proxy-Authenticate` challenge; rarely used by app servers. |
| 408 | Request Timeout | Client took too long to send the request. | Very slow upload, stalled connection. | Retry; ensure reasonable timeouts and payload size. | Tune server/read timeouts; consider 100-continue for large bodies. |
| 409 | Conflict | Request conflicts with current server state. | Duplicate key, version mismatch in optimistic locking. | Refresh state, resolve conflict, retry with updated version. | Use for edit conflicts; include conflict details (current version/fields). |
| 410 | Gone | Resource used to exist but is permanently removed. | Deleted page/API, retired shortlink. | Don’t retry; update links/bookmarks. | Prefer over 404 when removal is permanent and intentional. |
| 411 | Length Required | Missing `Content-Length` where required. | Streaming without length to a server that mandates it. | Include `Content-Length` or switch to chunked if supported. | Accept chunked coding or document the requirement clearly. |
| 412 | Precondition Failed | A precondition header wasn’t met. | `If-Match` ETag doesn’t match current resource. | Re-fetch resource, update ETag, retry if appropriate. | Implement ETag/conditional requests; return current validators. |
| 413 | Content Too Large *(Payload Too Large)* | Request body is bigger than the server is willing to accept. | Oversized file upload/body. | Compress/resize file; split upload; respect limits. | Enforce limits; include max size; consider resumable uploads. |
| 414 | URI Too Long | The URL is too long for the server to process. | Massive query strings, encoded data in URL. | Switch to `POST` with body; shorten params. | Increase limits carefully; guide clients to use body. |
| 415 | Unsupported Media Type | Server doesn’t support the request payload’s format. | Sending XML where only JSON is supported; wrong `Content-Type`. | Send supported content type; fix header & encoding. | Validate `Content-Type`; list supported types in docs. |
| 416 | Range Not Satisfiable | Requested byte range can’t be served. | Start/end out of bounds. | Recalculate range or fetch whole file. | Return valid `Content-Range`; ensure static file metadata is correct. |
| 417 | Expectation Failed | The `Expect` header’s requirements can’t be met. | `Expect: 100-continue` not supported. | Remove `Expect` or adapt to server behavior. | Either support 100-continue or reject early with guidance. |
| 418 | I’m a teapot | Joke status from RFC 2324; sometimes used playfully. | Easter eggs. | N/A. | Don’t use in production APIs. |
| 421 | Misdirected Request | Request was routed to a server unable to produce a response. | HTTP/2 connection reuse to wrong origin. | Retry on a new connection; disable connection reuse if needed. | Ensure correct routing/ALB config; SNI/authority checks. |
| 422 | Unprocessable Content / Entity | Well-formed but semantically invalid. | Fails business rules or schema validation. | Fix payload per error details; validate client-side first. | Return precise field errors; keep 422 for validation failures. |
| 423 | Locked | Resource is locked (WebDAV). | Write to locked resource. | Wait/retry per lock policy. | Use for WebDAV or similar lock semantics. |
| 424 | Failed Dependency | Dependent request failed (WebDAV). | Prior action in a batch failed. | Fix prior failure first. | Use in multi-action/transactional APIs with dependencies. |
| 425 | Too Early | Server is unwilling to risk processing an early replay. | Early data (TLS 0-RTT) replay risk. | Retry without early data. | Gate non-idempotent operations until handshake completes. |
| 426 | Upgrade Required | Client must switch to a different protocol. | Need TLS/HTTP/2/WebSocket. | Reissue request with upgraded protocol. | Send `Upgrade` and `Connection` headers indicating options. |
| 428 | Precondition Required | Missing required precondition headers. | Unsafe updates without `If-Match`. | Supply `If-Match` / validators. | Enforce conditional updates to prevent lost writes. |
| 429 | Too Many Requests | Rate limit exceeded. | Bursty traffic, abuse prevention. | **Back off and retry** after `Retry-After`; implement client-side rate limiting. | Return `Retry-After`; document quotas; provide headers for limits/remaining. |
| 431 | Request Header Fields Too Large | Header fields are too large. | Huge cookies/headers. | Trim cookies/headers; use body. | Enforce sane header size limits; guide clients. |
| 451 | Unavailable For Legal Reasons | Blocked due to legal demands. | Geo/IP block, court order. | Do not retry; follow legal guidance. | Return minimal details; log and comply with regulations. |
| 500 | Internal Server Error | Server hit an unexpected exception. | Uncaught errors, null refs, unhandled edge cases. | Retry if idempotent; report with correlation ID if provided. | Log with trace ID; fix bug; avoid leaking stack traces. |
| 501 | Not Implemented | Server doesn’t recognize/implement the method. | Using unsupported verb or feature. | Don’t retry; check API docs. | Use for truly unimplemented features; prefer 405 if resource disallows method. |
| 502 | Bad Gateway | Upstream server returned invalid response. | Broken dependency, upstream crash. | Retry with backoff. | Monitor upstreams; add circuit breaker; handle timeouts. |
| 503 | Service Unavailable | Service is overloaded or down for maintenance. | Traffic spikes, deploys. | Retry after delay; respect `Retry-After`. | Use for overload & maintenance windows; shed load gracefully. |
| 504 | Gateway Timeout | Upstream didn’t respond in time. | Slow DB/service; network issues. | Retry with backoff; consider smaller requests. | Tune timeouts; optimize upstream; add caching/queuing. |
| 505 | HTTP Version Not Supported | Server doesn’t support the HTTP version used. | Legacy client using unsupported version. | Upgrade client. | Support modern versions; document supported versions. |
| 506 | Variant Also Negotiates | Content negotiation configuration error. | `Transparent Content Negotiation` misconfig. | N/A (server-side issue). | Fix negotiation setup; avoid circular references. |
| 507 | Insufficient Storage | Not enough space to complete the operation. | Disk quota full (often WebDAV). | Retry later or reduce payload. | Provision storage; return accurate quota info if possible. |
| 508 | Loop Detected | Infinite loop detected while processing request. | Recursive graph traversal (WebDAV, PROPFIND). | Stop / adjust request. | Detect & break cycles; cap depth. |
| 510 | Not Extended | Further extensions to the request are required. | Deprecated/rare extension negotiation. | Follow API spec if used. | Avoid; design explicit negotiation mechanisms. |
| 511 | Network Authentication Required | Client must authenticate to gain network access. | Captive portals (Wi‑Fi login). | Open portal, authenticate, then retry. | Use in gateways; redirect to login portal. |

> **Tips**
> - Return a structured error body (e.g., `{ "code": 422, "message": "Validation failed", "errors": [{ "field": "email", "reason": "invalid" }] }`) and include a **correlation ID** for debugging.
> - For **429** and **503**, include `Retry-After`. For **409/412/428**, include **ETag/version** hints.

[⬆ Back to top](#top)
