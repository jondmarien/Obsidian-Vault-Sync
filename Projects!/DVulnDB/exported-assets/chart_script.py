import plotly.graph_objects as go
import numpy as np

# Create system architecture diagram
fig = go.Figure()

# Define layers with better positioning
layers = [
    {"name": "Frontend Layer", "y": 4.5, "color": "#10b981", 
     "components": ["Next.js 14", "Dashboard", "Forms", "Analytics", "Wallet"]},
    {"name": "Web3 Infrastructure", "y": 3.0, "color": "#3b82f6", 
     "components": ["Wagmi", "Viem", "Web3Modal", "IPFS Client", "ETH RPC"]},
    {"name": "Blockchain Layer", "y": 1.5, "color": "#6366f1", 
     "components": ["VulnRegistry", "BountyEscrow", "ReputNFT", "Ethereum", "IPFS Store"]},
    {"name": "External Tools", "y": 0, "color": "#f59e0b", 
     "components": ["Nmap", "Nikto", "Burp Suite", "PowerShell", "APIs"]}
]

# Add components as rectangles with proper spacing
for layer in layers:
    y_pos = layer["y"]
    
    # Add layer title on the left
    fig.add_annotation(
        x=-1.2, y=y_pos,
        text=f"<b>{layer['name']}</b>",
        showarrow=False,
        font=dict(size=14, color=layer["color"]),
        xanchor="center",
        textangle=-90
    )
    
    # Add components
    for i, component in enumerate(layer["components"]):
        x_pos = i * 1.2
        
        # Component rectangle
        fig.add_shape(
            type="rect",
            x0=x_pos-0.5, x1=x_pos+0.5,
            y0=y_pos-0.3, y1=y_pos+0.3,
            fillcolor=layer["color"],
            opacity=0.7,
            line=dict(color="white", width=2)
        )
        
        # Component text
        fig.add_annotation(
            x=x_pos, y=y_pos,
            text=f"<b>{component}</b>",
            showarrow=False,
            font=dict(size=12, color="white"),
            xanchor="center"
        )

# Add comprehensive connection arrows
connections = [
    # Frontend to Web3
    {"from": (0, 4.5), "to": (0, 3.3), "label": "React Hooks", "color": "#10b981"},
    {"from": (1.2, 4.5), "to": (1.2, 3.3), "label": "Web3 Calls", "color": "#10b981"},
    
    # Web3 to Blockchain
    {"from": (0, 2.7), "to": (0, 1.8), "label": "Smart Contracts", "color": "#3b82f6"},
    {"from": (3.6, 2.7), "to": (4.8, 1.8), "label": "IPFS Upload", "color": "#3b82f6"},
    
    # External Tools to Frontend
    {"from": (0, 0.3), "to": (2.4, 4.2), "label": "Data Feed", "color": "#f59e0b"},
    {"from": (4.8, 0.3), "to": (3.6, 4.2), "label": "API Data", "color": "#f59e0b"}
]

for conn in connections:
    from_x, from_y = conn["from"]
    to_x, to_y = conn["to"]
    
    # Add curved arrow
    fig.add_annotation(
        x=to_x, y=to_y,
        ax=from_x, ay=from_y,
        arrowhead=2,
        arrowsize=1.5,
        arrowwidth=3,
        arrowcolor=conn["color"],
        showarrow=True,
        text="",
        opacity=0.8
    )
    
    # Add connection label
    mid_x = (from_x + to_x) / 2
    mid_y = (from_y + to_y) / 2
    
    fig.add_annotation(
        x=mid_x, y=mid_y,
        text=f"<b>{conn['label']}</b>",
        showarrow=False,
        font=dict(size=11, color=conn["color"]),
        bgcolor="rgba(255,255,255,0.9)",
        bordercolor=conn["color"],
        borderwidth=1,
        borderpad=3
    )

# Update layout for better visibility
fig.update_layout(
    title="<b>DVulnDB System Architecture</b>",
    title_font_size=18,
    xaxis=dict(
        range=[-2, 6],
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        visible=False
    ),
    yaxis=dict(
        range=[-0.8, 5.3],
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        visible=False
    ),
    plot_bgcolor="white",
    paper_bgcolor="white",
    showlegend=False,
    height=700,
    margin=dict(l=50, r=50, t=80, b=50)
)

# Save the chart
fig.write_image("dvulndb_architecture.png", width=1200, height=700)