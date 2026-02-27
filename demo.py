#!/usr/bin/env python3
"""
CLI Demo for Multi-Agent Task Coordination
Bounty #239 - Run via command line
"""

import argparse
from multi_agent_workflow import run_demo

def main():
    parser = argparse.ArgumentParser(
        description="Multi-Agent Task Coordination Demo"
    )
    parser.add_argument(
        "--topic", 
        type=str, 
        default="The future of AI agents in software development",
        help="Topic for the research team to work on"
    )
    parser.add_argument(
        "--audience",
        type=str,
        default="software developers",
        help="Target audience for the content"
    )
    
    args = parser.parse_args()
    
    result = run_demo(args.topic, args.audience)
    
    print("\n" + "=" * 60)
    print("✅ Demo Complete!")
    print("=" * 60)
    
    # Save output to file
    output_file = "outputs/article.md"
    with open(output_file, "w") as f:
        f.write(result.get("published_article", ""))
    print(f"📄 Article saved to: {output_file}")

if __name__ == "__main__":
    main()