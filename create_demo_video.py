#!/usr/bin/env python3
"""
Demo Video Generator for Multi-Agent Workflow
Creates an animated visualization of the agent coordination
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Create frames directory
os.makedirs("demo_frames", exist_ok=True)

# Colors
BG_COLOR = (26, 26, 46)  # Dark blue
AGENT_COLORS = {
    "researcher": (0, 212, 255),  # Cyan
    "writer": (123, 47, 247),     # Purple
    "publisher": (0, 255, 136),   # Green
}
TEXT_COLOR = (238, 238, 238)
ACCENT_COLOR = (255, 170, 0)

def create_frame(frame_num, title, content, active_agent=None, progress=0):
    """Create a single frame of the demo"""
    width, height = 1200, 800
    img = Image.new('RGB', (width, height), BG_COLOR)
    draw = ImageDraw.Draw(img)
    
    # Try to load font, fallback to default
    try:
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Title
    draw.text((width//2 - 250, 30), title, fill=ACCENT_COLOR, font=font_large)
    
    # Draw agent boxes
    agent_y = 120
    agent_width = 300
    agent_height = 80
    agent_spacing = 50
    start_x = (width - (3 * agent_width + 2 * agent_spacing)) // 2
    
    agents = [
        ("Researcher", "researcher"),
        ("Writer", "writer"),
        ("Publisher", "publisher")
    ]
    
    for i, (name, key) in enumerate(agents):
        x = start_x + i * (agent_width + agent_spacing)
        color = AGENT_COLORS[key]
        
        # Highlight active agent
        if active_agent == key:
            # Glow effect
            for glow in range(3, 0, -1):
                glow_color = tuple(min(255, c + 30*glow) for c in color)
                draw.rounded_rectangle([x-glow*5, agent_y-glow*5, 
                                       x+agent_width+glow*5, agent_y+agent_height+glow*5],
                                      radius=15, outline=glow_color, width=3)
        
        # Agent box
        draw.rounded_rectangle([x, agent_y, x+agent_width, agent_y+agent_height],
                              radius=10, fill=color, outline=color)
        
        # Agent name
        text_bbox = draw.textbbox((0, 0), name, font=font_medium)
        text_width = text_bbox[2] - text_bbox[0]
        text_x = x + (agent_width - text_width) // 2
        draw.text((text_x, agent_y + 25), name, fill=BG_COLOR, font=font_medium)
    
    # Draw connections
    line_y = agent_y + agent_height + 20
    for i in range(2):
        x1 = start_x + i * (agent_width + agent_spacing) + agent_width
        x2 = start_x + (i + 1) * (agent_width + agent_spacing)
        
        # Draw arrow
        if progress > i + 1:
            draw.line([(x1, line_y), (x2, line_y)], fill=(0, 255, 136), width=3)
            # Arrow head
            draw.polygon([(x2-10, line_y-5), (x2, line_y), (x2-10, line_y+5)], 
                        fill=(0, 255, 136))
        else:
            draw.line([(x1, line_y), (x2, line_y)], fill=(100, 100, 100), width=2)
    
    # Content area
    content_y = 280
    content_box = [50, content_y, width-50, height-50]
    draw.rounded_rectangle(content_box, radius=10, outline=(100, 100, 100), width=2)
    
    # Content text
    y_offset = content_y + 20
    for line in content.split('\n'):
        if line.strip():
            draw.text((70, y_offset), line, fill=TEXT_COLOR, font=font_small)
            y_offset += 30
    
    # Progress bar
    bar_y = height - 30
    bar_width = width - 100
    draw.rectangle([50, bar_y, 50+bar_width, bar_y+10], outline=(100, 100, 100), width=1)
    progress_width = int(bar_width * (progress / 3))
    draw.rectangle([50, bar_y, 50+progress_width, bar_y+10], fill=ACCENT_COLOR)
    
    # Frame number
    draw.text((width-100, height-25), f"Frame {frame_num}", fill=(100, 100, 100), font=font_small)
    
    return img

def create_demo_video():
    """Create all frames for the demo video"""
    frames = []
    
    # Frame 1: Introduction
    content1 = """
🚀 Multi-Agent Task Coordination Demo

📌 Topic: AI agents in blockchain
👥 Target Audience: web3 developers

Starting workflow with 3 specialized agents:
  • Researcher - Gathers information and insights
  • Writer - Creates structured content  
  • Publisher - Finalizes and records onchain

Initializing agent coordination...
"""
    frames.append(create_frame(1, "Multi-Agent Demo", content1, None, 0))
    
    # Frame 2: Researcher working
    content2 = """
🔍 RESEARCHER AGENT

Status: WORKING

Researching: AI agents in blockchain

Key findings:
  ✓ Identified main use cases
  ✓ Analyzed current landscape
  ✓ Compiled technical insights
  ✓ Gathered industry data

Output: Comprehensive research report
"""
    frames.extend([create_frame(2, "Step 1: Research", content2, "researcher", 0.5) for _ in range(3)])
    
    # Frame 3: Research complete, Writer starts
    content3 = """
✅ RESEARCH COMPLETE

Research report delivered to Writer agent

📊 Findings Summary:
  • Emerging technology area
  • Rapid adoption in web3
  • Strong developer interest
  • Significant growth potential

Passing research to Writer...
"""
    frames.extend([create_frame(3, "Research → Writer", content3, "writer", 1) for _ in range(3)])
    
    # Frame 4: Writer working
    content4 = """
✍️ WRITER AGENT

Status: WRITING

Creating article for: web3 developers

Structure:
  ✓ Executive Summary
  ✓ Detailed Analysis  
  ✓ Key Takeaways
  ✓ Conclusion

Transforming research into readable content...
"""
    frames.extend([create_frame(4, "Step 2: Writing", content4, "writer", 1.5) for _ in range(3)])
    
    # Frame 5: Writing complete, Publisher starts
    content5 = """
✅ ARTICLE COMPLETE

Draft article ready for publication

📄 Content Stats:
  • Word count: ~200 words
  • Sections: 4
  • Reading time: 2 minutes
  • Audience: web3 developers

Sending to Publisher for finalization...
"""
    frames.extend([create_frame(5, "Writer → Publisher", content5, "publisher", 2) for _ in range(3)])
    
    # Frame 6: Publisher working
    content6 = """
📤 PUBLISHER AGENT

Status: PUBLISHING

Finalizing article and recording onchain...

Actions:
  ✓ Formatting final output
  ✓ Adding metadata
  ✓ Recording proof on Base Sepolia
  ✓ Generating transaction hash

Creating immutable record...
"""
    frames.extend([create_frame(6, "Step 3: Publishing", content6, "publisher", 2.5) for _ in range(3)])
    
    # Frame 7: Complete
    content7 = """
✅ WORKFLOW COMPLETE!

🎉 All agents finished successfully

Results:
  • Research: Complete ✓
  • Article: Published ✓
  • Onchain Proof: Recorded ✓

📋 Task ID: 32a8bc1a3a652821
🔗 Network: Base Sepolia

Multi-agent coordination demonstrated!
"""
    frames.extend([create_frame(7, "Demo Complete!", content7, None, 3) for _ in range(5)])
    
    # Save frames
    for i, frame in enumerate(frames):
        frame.save(f"demo_frames/frame_{i:03d}.png")
    
    print(f"✅ Created {len(frames)} frames in demo_frames/")
    print("📁 Files saved as frame_000.png through frame_{:03d}.png".format(len(frames)-1))
    
    return len(frames)

if __name__ == "__main__":
    num_frames = create_demo_video()
    print(f"\n🎬 Demo video frames ready!")
    print(f"   Total frames: {num_frames}")
    print(f"\nTo create GIF: convert -delay 30 demo_frames/*.png demo.gif")
    print(f"Or use: ffmpeg -i demo_frames/frame_%03d.png -vf fps=10 demo.mp4")