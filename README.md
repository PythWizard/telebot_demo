# Telegram AI Assistant

A **showcase version** of a Python application integrating Large Language Models (LLMs) with Telegram automation, intelligent conversations, speech recognition, and configurable messaging workflows.

> **Portfolio Showcase**
>
> This repository contains a simplified version of the original application and is intended to demonstrate the project's architecture, implementation approach, and AI integration.
>
> The complete production version is maintained in a **private repository** because it contains proprietary automation workflows, prompt engineering, and additional implementation details.

---

## Overview

Telegram AI Assistant is a desktop application that combines Telegram automation with modern AI technologies to create an intelligent conversational assistant.

The application integrates the Telegram API, OpenAI language models, and speech recognition to support context-aware conversations, voice message transcription, configurable assistant behavior, and automated follow-up workflows.

The project demonstrates practical implementation of asynchronous programming, AI API integration, desktop application development, and conversational workflow automation.

---

## Key Features

- 🤖 AI-powered conversations using OpenAI language models
- 💬 Context-aware dialogue management
- 🎤 Voice message transcription using Whisper
- ⏳ Automated follow-up communication
- ⌨️ Human-like typing simulation
- ⚙️ Configurable prompts and assistant behavior
- 📋 Conversation history management
- 📝 Application logging and monitoring
- 🖥️ Desktop configuration interface

---

## AI & Automation Workflow

The application combines multiple components into a single automation pipeline:

- Telegram message processing
- Context management
- AI response generation
- Voice transcription
- Follow-up scheduling
- User activity tracking
- Automated response delivery

---

## Desktop Application

Built with Tkinter, the application provides:

- Runtime configuration management
- AI model parameter configuration
- Prompt customization
- Application monitoring
- Live logging
- Background asynchronous processing

---

## System Architecture

```text
                 Telegram API
                       │
                       ▼
             Message Processing
                       │
                       ▼
             Conversation Manager
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
   OpenAI API     Whisper Engine   Activity Tracker
          │            │            │
          └────────────┼────────────┘
                       ▼
             Automation Engine
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
   Automated Replies        Follow-up Scheduler
                       │
                       ▼
               Desktop Interface
```

---

## Technologies

- Python
- AsyncIO
- Telethon
- OpenAI API
- faster-whisper
- Tkinter
- JSON data storage

---

## Repository Scope

This repository contains only the core functionality required to demonstrate the project's architecture and implementation.

The complete private version additionally includes:

- advanced conversation management
- production prompt engineering
- configurable automation workflows
- extended activity tracking
- additional AI processing modules
- project-specific optimization and utilities

---

## Example Applications

- AI-powered Telegram assistants
- Customer communication automation
- Personal productivity assistants
- Voice-enabled messaging workflows
- Intelligent chatbot development

---

## Screenshot

<p align="center">
  <img src="https://github.com/user-attachments/assets/437e79c5-2b5b-4bc5-b9d4-1960dd48018c"
       width="700"
       alt="Telegram AI Assistant">
</p>

---

## Disclaimer

This repository is provided as part of my software development portfolio.

Some implementation details have been intentionally simplified or omitted, while the complete production version remains private.
