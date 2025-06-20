# Project Vision: Party Planner AI Agent

## Overview

This project is an intelligent assistant designed to support the configuration and management of events. It enhances a typical event configuration workflow (like that of `squadup.city`) by introducing context-aware automation and AI-powered suggestions.

The agent does not replace user input—it **augments** it. It should act like a creative, reliable, and responsive co-host that helps the event organizer make better, faster decisions while streamlining communication and logistics.

---

## Core Goals

- Separate **event detail configuration** from all AI-powered functionality in the UI.
- Provide helpful suggestions without overwriting user input.
- Allow the user to approve or reject changes before any are committed.

---

## Functional Modules

### 1. Event Detail Input (Human Authored)
This box includes standard fields, all directly filled by the user:

- Event Title
- Date & Time
- Address (Street, City, State, ZIP, Country)
- Description
- Cover Image (upload)
- Theme Color
- RSVP Enabled (boolean)
- Event Type (Physical / Virtual)
- Visibility (Public / Private)
- Event Slug (optional)

This section is authoritative and forms the basis of all agent context.

---

### 2. Agent Utility Panel (AI Enhanced)

The following tools operate **adjacent to** the event form and use its fields to generate suggestions:

#### a. Description Rewriter
- Rewrites the event description using tone/style guidance from the user.
- Does not overwrite the original—returns a suggested version for review.

#### b. Weather Forecast Integration
- Uses the location and date/time to pull weather data (e.g. temperature, conditions, UV index).
- Suggests updates to the event description and cover image prompt accordingly.

#### c. Cover Image Generator
- Constructs a detailed image prompt based on event title, theme, weather, and location.
- Calls an external image generation API to produce a fitting event cover.
- Option to accept or regenerate.

#### d. RSVP Simulation
- Simulates potential guest responses based on the event's tone, type, and context.
- Can surface common questions (e.g. “Is it dog-friendly?”, “Will there be food?”)

#### e. Guest Communication Agent
- Accepts inbound guest messages.
- Summarizes or tags them for the host.
- Offers quick, editable reply templates for host approval.

#### f. Alternate Location Recommender
- When weather or logistical issues are detected, the agent proposes alternate venues.
- Filters by distance, accessibility, and suitability.

#### g. Shopping List Generator
- Uses event type and guest count to generate a suggested supplies list.
- Adds affiliate links to products where possible (optional monetization path).

---

## UX Requirements

- AI functionality is kept **visually and functionally separate** from user-defined event details.
- Suggestions are **non-destructive**—they require user approval before applying.
- UI must remain clean and minimal, despite advanced capabilities.

---

## Stretch Features

- Real-time conflict checking with nearby events.
- AI tone analysis of event title and description to guide styling.
- Integrated calendar sync options.

---

## Developer Notes

- Current prototype uses `Gradio` for interface and `langchain_ollama` for LLM calls.
- Agent context is built from all user-provided fields and injected via structured prompt.
- Weather and geolocation will require API integration (OpenWeatherMap, Google Maps, etc.).
- Image generation may use DALL·E, SDXL, or equivalent.
- Keep the code modular and manageable.
- Follow best practices.
- Test with black.

---

## End Goal

A modular, extensible, and emotionally intelligent event assistant that feels like an actual collaborator—not a gimmick. The agent should adapt to the user's tone, predict their needs, and always offer suggestions that respect the user’s creative control.