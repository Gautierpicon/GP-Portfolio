# DuckAI - Portfolio

A fun and quirky AI model. The model is powered by Gemma 3 1B and customized through a Modelfile.

## Prerequisites

- **Ollama** installed on your system. Download it from [ollama.ai](https://ollama.ai)

## Setup Instructions

### 1. Install Ollama

Download and install [Ollama.ai](https://ollama.ai) from the official website appropriate for your operating system (macOS, Windows, or Linux).

### 2. Create the Duck Model

Navigate to the `ollama` directory containing the `Modelfile`

```bash
cd ollama
```

And run:

```bash
ollama create DuckAI -f Modelfile
```

This command creates a new model called `DuckAI` using the specifications in your Modelfile.

### 3. Run the Model

Start a chat session with your duck:

```bash
ollama run DuckAI
```

## Model Features

- **Character**: Plays a white duck with an orange beak
- **Personality**: Fun, friendly, and slightly clumsy
- **Signature**: Ends every sentence with "koik" and uses 🦆 emoji
- **Base Model**: Gemma 3 1B
- **Temperature**: 1.3 (creative responses)

## Customizing the Model

To modify the duck's behavior, edit the `Modelfile`:

- Change the `PARAMETER temperature` value (lower = more focused, higher = more creative)
- Modify the `SYSTEM` prompt to change personality, rules, or language behavior

After making changes, recreate the model:

```bash
ollama create DuckAI -f Modelfile
```

## Contributing

Feel free to open an [issue](https://github.com/Gautierpicon/GP-Portfolio/issues), submit a [pull request](https://github.com/Gautierpicon/GP-Portfolio/pulls) with improvements or variations of the duck model! You can:

- Modify the system prompt for different personalities
- Test with different base models
- Suggest parameter tweaks for better performance
- Add new language-specific behaviors

---

Enjoy your quirky duck! 🦆 koik koik!
