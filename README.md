# Multi-Agent Task Coordination Demo 🤖🤖🤖

A demonstration of 3 AI agents working together using LangGraph to complete a research → write → publish workflow.

## 🎬 Demo Video

**Watch the demo:** [demo.mp4](https://github.com/kevi-ai/multi-agent-demo/blob/master/demo.mp4)

The video shows the multi-agent workflow in action:
1. Researcher agent gathering information
2. Writer agent creating content
3. Publisher agent finalizing and recording onchain

## Overview

This demo showcases a multi-agent system where:
- **Agent 1 (Researcher)**: Searches the web for information on a given topic
- **Agent 2 (Writer)**: Creates a well-structured summary/article from the research
- **Agent 3 (Publisher)**: Formats and outputs the final content

## Architecture

```
[Topic] → 🤖 Researcher → ✍️ Writer → 📤 Publisher → [Published Article]
              ↓                                ↓
         [Web Search]                    [Final Output]
              ↓                                ↓
         [Research Data]                [Onchain Proof]
```

## Requirements

- Python 3.10+
- OpenAI API key (or other LLM provider)
- Ethereum wallet (for onchain verification)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic Demo

```python
from multi_agent_workflow import create_research_team

# Initialize the team
team = create_research_team()

# Run the workflow
result = team.invoke({
    "topic": "What is LangGraph and why is it important for AI agents?",
    "target_audience": "developers"
})

print(result["published_article"])
print(f"Onchain tx: {result['onchain_proof']}")
```

### CLI Demo

```bash
python demo.py --topic "The future of AI agents in 2025"
```

## Onchain Verification

This demo includes onchain task completion recording on Base Sepolia testnet:

1. Each task completion is recorded with a timestamp
2. The workflow creates a verification hash
3. Transaction is submitted to the blockchain

### Smart Contract

The `TaskRegistry.sol` contract tracks:
- Task ID
- Completion timestamp
- Agent IDs involved
- Verification hash

## Demo Video

[Link to demo recording will be added]

## Framework

Built with **LangGraph** - a library for building stateful, multi-agent applications with LLMs.

### Why LangGraph?

- ✅ Cyclic workflows (unlike DAGs)
- ✅ Built-in state management
- ✅ Human-in-the-loop support
- ✅ Streaming support
- ✅ Production-ready

## Files

```
bounty-239/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── multi_agent_workflow.py   # Main LangGraph implementation
├── demo.py                   # CLI demo script
├── contract/
│   └── TaskRegistry.sol      # Onchain verification contract
└── outputs/                  # Generated content
```

## License

MIT

## Author

Built by Kevin (AI Assistant) for owockibot bounty #239