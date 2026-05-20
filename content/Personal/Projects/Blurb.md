---
class: project
tags:
source:
related:
author:
date: 2026-05-18
updated: 2026-05-18 13:46:17
aliases:
---
Blurb is an idea I came up with a while back but could never fully flesh out. I was inspired by a feeling I was experiencing that the main social media platforms I'm on are way too cluttered, with an overwhelming amount of content I'm facing every time I log in, when I really just want to see a select few people's activity. Hence, the idea is essentially that Blurb will be a social media platform solely for my partner and I (and also for select groups of people who are invited by each other in a fuller version of this project) - think Twitter but for just you and your friends. 

I do want to rebuild this project from scratch again, and get a strong MVP up and running for testing with my partner. 

## Ideas: 
- ~~Bun~~
- React frontend
- Swift for Mobile
- ~~Firebase Auth~~ 
	- Or a postgres/mysql DB?
- ~~Redis Caching~~
- ~~Microservice architecture~~
- ~~Vercel first, AWS S3, Terraform if scaling~~ 
- ~~Not sure if needed: Apache Kafka, Docker, Kubernetes~~

## Finalised Stack

| Layer                  | Choice                                   | Why                                                                           |
| ---------------------- | ---------------------------------------- | ----------------------------------------------------------------------------- |
| Backend                | [[Go]]                                   | Compiled, statically typed, purpose-built for high-throughput APIs            |
| Router                 | Chi                                      | Lightweight and idiomatic; used in production at my company                   |
| Frontend               | React + TypeScript (Vite)                |                                                                               |
| Database               | Postgres + sqlc                          | sqlc generates type-safe Go from raw SQL with no ORM overhead                 |
| Migrations             | golang-migrate                           |                                                                               |
| Architecture           | Clean Architecture (monolith)            | Monolith first; clean layer boundaries make future extraction straightforward |
| Logging                | slog (stdlib)                            | Structured logging with zero external dependencies (Go 1.21+)                 |
| Config                 | caarlos0/env                             | Typed, validated env vars at startup; fails fast if config is missing         |
| Testing                | testify + real Postgres                  | Real DB ensures tests reflect actual production behaviour                     |
| Auth                   | In-house (bcrypt + JWT + refresh tokens) | Invite-only app; no vendor lock-in, full ownership                            |
| Real-time              | SSE                                      | One-way server push; simpler than WebSockets for feed updates                 |
| Containerisation       | Docker (multi-stage)                     |                                                                               |
| CI/CD                  | GitHub Actions                           |                                                                               |
| Dev tooling            | Makefile                                 |                                                                               |
| Hosting (Frontend)     | Vercel                                   |                                                                               |
| Hosting (Backend + DB) | Railway                                  | Persistent server required for SSE; managed Postgres included                 |
| Mobile                 | Swift (deferred)                         | Web MVP first                                                                 |

## Old Draft of Blurb:
![[Screenshot 2026-05-18 at 2.06.00 PM.png | 500]]
- i was using vue for this 
- i tried lifting from twitter's ui 
- i would much prefer a more minimalist, monochromic colour scheme to begin with, then customise from there 
- i would like to deprecate the mood section for now, and just focus on the blurbs (tweets) and feed


## MVP Features
I believe that the MVP should have a few components that can confidently function for my girlfriend and I as the only users at least for now:
### Phase 1 
- Login / Auth - and storing this user data in our db
- Home Page
	- Feed (similar to twitter, we will see blurbs in our timeline here)
	- Blurb Button + composer (text only)
- Profile Page - to configure user info
	- profile pic (just emojis for now)
	- username
	- display name
- PostgreSQL DB
	- user data
	- blurbs - content only
- Styling:
	- minimalist, monochromic
	- berkeley mono / jetbrains mono for font
### Phase 2 
- Interaction data on blurbs (likes, comments)
- Settings Page
	- dark / light mode toggle
- Media in blurbs (images, etc.)
### Future
- Custom CSS config
- Invite system for other users
