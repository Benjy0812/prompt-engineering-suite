# Product Guidelines - Prompt Engineering Suite

## 1. Tone and Voice
- **Technical & Precise**: Instructions must be clear, unambiguous, and use formal engineering terminology.
- **Direct**: Avoid conversational filler; focus on the "instruction-response" efficiency.

## 2. Prompt Structure Standards
To ensure consistency across the suite, every prompt file MUST follow this structure:
- **Role**: Define the specific persona the AI should adopt.
- **Task**: A clear statement of the objective.
- **Constraints**: Explicit rules the AI must follow (e.g., "No conversational filler").
- **Output Format**: Detailed requirements for how the response should be formatted.

## 3. Implementation Patterns
- **Unified Placeholders**: Use a consistent syntax for user input variables (e.g., `{{USER_INPUT}}`).
- **Multi-Model Optimization**: Include specific instructions or blocks optimized for the Gemini family (Flash, Flash Lite, Pro) and other major models to ensure consistent behavior.

## 4. Quality & Performance Standards
- **Performance Benchmarking**: Every prompt must be tested and verified against Gemini Flash, Gemini Flash Lite, and Gemini Pro.
- **Reliability**: Prompts must achieve a 95% success rate in producing valid, parseable outputs during testing.
- **Documentation**: Every prompt MUST be accompanied by a `[prompt-name].README.md` that defines its intent, version, and usage examples.
