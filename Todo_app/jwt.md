# JSON Web Token (JWT) — Full Explanation

## 1. Introduction to JWT

JWT (JSON Web Token) is an open standard (RFC 7519) used to securely transmit information between two parties as a JSON object. It is compact, URL-safe, and digitally signed, making it ideal for modern web applications and APIs.

JWT is most commonly used for:

- **Authentication** (who the user is)
- **Authorization** (what the user can access)

A key characteristic of JWT is **stateless authentication**, where the server does not store session data.

---

## 2. Why JWT Exists

Traditional session-based authentication requires:

- Server-side session storage
- Session lookup on every request
- Difficulty scaling across multiple servers

JWT solves these problems by:

- Storing user identity inside the token
- Eliminating server-side session storage
- Enabling easy horizontal scaling

---

## 3. Key Properties of JWT

- Stateless  
- Compact and fast  
- Self-contained  
- Signed (and optionally encrypted)  
- Platform and language independent  

---

## 4. JWT Structure

A JWT consists of **three Base64URL-encoded parts**, separated by dots (`.`):

header.payload.signature

makefile
Copy code

Example:

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.
eyJzdWIiOiIxMjMiLCJleHAiOjE3MTAwMDAwMDB9
.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

yaml
Copy code

---

## 5. JWT Header

The header describes how the token is signed.

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
Common Header Fields:

alg → Signing algorithm

typ → Token type (JWT)

kid → Key ID (optional, used in key rotation)

6. JWT Payload (Claims)
The payload contains claims, which are statements about the user and metadata about the token.

json
Copy code
{
  "sub": "user_123",
  "email": "user@gmail.com",
  "role": "admin",
  "iat": 1700000000,
  "exp": 1710000000
}
Types of Claims
6.1 Registered Claims
Standard claims defined by the JWT specification:

iss → Issuer

sub → Subject (user identifier)

aud → Audience

exp → Expiration time

nbf → Not valid before

iat → Issued at

jti → JWT ID

6.2 Public Claims
Custom claims agreed upon publicly:

email

username

profile

6.3 Private Claims
Application-specific claims:

role

permissions

tenant_id

⚠️ Important: JWT payload is not encrypted — only encoded. Anyone with the token can decode it.

7. JWT Signature
The signature ensures token integrity.

scss
Copy code
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  secret_key
)
Purpose of Signature:

Verifies the token was issued by a trusted server

Prevents modification of payload data

Ensures authenticity

8. JWT Encoding vs Encryption
Feature	Signed JWT (JWS)	Encrypted JWT (JWE)
Readable payload	Yes	No
Tamper-proof	Yes	Yes
Confidential	No	Yes
Common usage	Very common	Rare

Most APIs use signed JWT (JWS).

9. JWT Authentication Flow
Typical authentication process:

User submits login credentials

Server validates credentials

Server generates JWT

JWT is sent to client

Client stores JWT

Client includes JWT in every request

Server verifies JWT signature and claims

HTTP Authorization Header:

makefile
Copy code
Authorization: Bearer <JWT_TOKEN>
10. Stateless Authentication Explained
With JWT:

Server does not store session data

Token itself contains user identity

Each request is self-verifying

This is why JWT is popular in:

FastAPI

Microservices

Cloud-native applications

11. Access Tokens vs Refresh Tokens
Access Token
Short-lived (minutes)

Used to access protected routes

Sent with every request

Refresh Token
Long-lived (days/weeks)

Used to obtain a new access token

Stored securely (HttpOnly cookie)

Token Type	Lifetime	Usage
Access Token	Short	API access
Refresh Token	Long	Token renewal

12. Token Storage Strategies
Recommended:

HttpOnly cookies

Secure cookies

SameSite policies

Not Recommended:

localStorage (XSS risk)

sessionStorage (limited protection)

13. Token Expiration and Revocation
JWT cannot be revoked easily because it is stateless.

Common Solutions:

Short expiration times

Refresh token rotation

Token blacklisting (DB/Redis)

Versioned user tokens

14. JWT Security Best Practices
Always use HTTPS

Keep exp short

Validate iss, aud, and exp

Use strong secret keys

Rotate signing keys

Avoid storing sensitive data

Protect refresh tokens carefully

15. Common JWT Errors
Token expired

Invalid signature

Wrong algorithm

Missing Bearer prefix

Clock skew issues

16. JWT in FastAPI (Conceptual)
FastAPI typically uses:

OAuth2PasswordBearer

python-jose

Dependency injection for authentication

Middleware or dependencies for validation

JWT usually contains:

sub → user ID

exp → expiration time

17. When NOT to Use JWT
Applications needing instant logout

Extremely sensitive environments

Simple monolithic applications

18. JWT vs Session-Based Authentication
Aspect	JWT	Session
Server storage	No	Yes
Scalability	High	Medium
Revocation	Hard	Easy
Cloud-ready	Yes	Less
Mobile-friendly	Yes	No

19. Advantages of JWT
Stateless and scalable

Fast authentication

Language-agnostic

Works well with APIs

Ideal for microservices

20. Disadvantages of JWT
Hard to revoke

Token theft risk

Payload visibility

Larger request size

21. One-Line Summary
JWT is a stateless, signed token mechanism that securely authenticates users and authorizes access in modern distributed systems.

