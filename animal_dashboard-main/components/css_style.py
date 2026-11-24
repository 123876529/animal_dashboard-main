LIGHT_CSS = """
    <style>
    @keyframes fadeIn { from { opacity: 0; transform: translateY(15px); } to { opacity: 1; transform: translateY(0); } }
    .fade-in { animation: fadeIn 0.8s ease-in-out; }
    
    @keyframes blink { 0% { color: #D32F2F; } 50% { color: #FF8A80; } 100% { color: #D32F2F; } }
    .alert-text { animation: blink 1s infinite; font-weight: bold; font-size: 20px; }

    .stApp { background-color: #F4F8F4; transition: background-color 0.5s; }
    h1, h2, h3 { color: #1B5E20; font-weight: 600; }
    
    div[data-testid="stMetric"] {
        background-color: #FFFFFF; padding: 20px; border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04); border-top: 4px solid #2E8B57; margin-bottom: 10px;
    }
    div[data-testid="stPlotlyChart"] {
        background-color: #FFFFFF; border-radius: 12px; padding: 10px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.04);
    }
    .modebar { display: none !important; }
    header[data-testid="stHeader"] { display: none !important; }
    </style>
"""

DARK_CSS = """
    <style>
    @keyframes moveBackground {
        from { background-position: 0 0, 0 0, 0 0; }
        to { background-position: 20px 20px, 40px 40px, 40px 40px; }
    }
    
    .stApp { 
        background-color: #0A0E17 !important; 
        background-image: 
            radial-gradient(#00E5FF 1px, transparent 1px),
            linear-gradient(rgba(0, 229, 255, 0.08) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 229, 255, 0.08) 1px, transparent 1px) !important;
        background-size: 20px 20px, 40px 40px, 40px 40px !important;
        animation: moveBackground 3s linear infinite !important;
    }
    
    h1, h2, h3, p, span, div, label { color: #E2E8F0 !important; }
    
    div[data-testid="stMetric"] { 
        background-color: rgba(15, 23, 42, 0.8) !important; 
        border: 1px solid rgba(0, 229, 255, 0.2) !important;
        border-top: 4px solid #00E5FF !important;
        border-radius: 12px !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4) !important; 
    }
    div[data-testid="stPlotlyChart"] { 
        background-color: rgba(15, 23, 42, 0.8) !important; 
        border: 1px solid rgba(0, 229, 255, 0.2) !important; 
        border-radius: 12px !important;
        padding: 15px !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4) !important;
    }
    
    [data-testid="stSidebar"] { background-color: #0B1120 !important; border-right: 1px solid #1E293B; }
    div[data-baseweb="select"] > div { background-color: #1E293B !important; border-color: #334155 !important; color: #E2E8F0 !important; border-radius: 8px; }
    div[data-baseweb="select"] svg { fill: #00E5FF !important; color: #00E5FF !important; }
    input { background-color: #1E293B !important; color: #E2E8F0 !important; }
    
    .stDownloadButton > button {
        background-color: #1E293B !important; border: 1px solid #00E5FF !important; 
        box-shadow: 0 0 10px rgba(0, 229, 255, 0.3);
    }
    .stDownloadButton > button * { color: #00E5FF !important; font-weight: bold !important; }
    .stDownloadButton > button:hover { background-color: #00E5FF !important; }
    .stDownloadButton > button:hover * { color: #0A0E17 !important; }

    .detail-card {
        background-color: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(0, 229, 255, 0.2);
        border-left: 4px solid #00E5FF;
        border-radius: 12px;
        padding: 20px;
        margin-top: 10px;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    }
    .detail-card p { margin-bottom: 12px !important; font-size: 15px; line-height: 1.5;}
    .detail-card strong { color: #00E5FF !important; }

    div[data-baseweb="popover"],
    div[data-baseweb="popover"] > div,
    div[data-baseweb="popover"] div,
    div[data-baseweb="popover"] ul[role="listbox"] {
        background-color: #0F172A !important;
        border: none !important;
        outline: none !important;
    }
    div[data-baseweb="popover"] ul[role="listbox"] li {
        background-color: transparent !important;
        color: #E2E8F0 !important;
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
        border-radius: 0 !important; 
        margin: 0 !important;
    }
    div[data-baseweb="popover"] ul[role="listbox"] li * {
        color: #E2E8F0 !important;
        background-color: transparent !important;
    }
    div[data-baseweb="popover"] ul[role="listbox"] li:hover {
        background-color: rgba(0, 229, 255, 0.05) !important;
    }
    div[data-baseweb="popover"] ul[role="listbox"] li[aria-selected="true"] {
        background-color: #1E293B !important;
        border-left: 3px solid #00E5FF !important;
    }
    div[data-baseweb="popover"] ul[role="listbox"] li[aria-selected="true"] * {
        color: #00E5FF !important;
        font-weight: bold !important;
    }
    div[data-baseweb="popover"] ul[role="listbox"]::-webkit-scrollbar { width: 6px; }
    div[data-baseweb="popover"] ul[role="listbox"]::-webkit-scrollbar-track { background: transparent; }
    div[data-baseweb="popover"] ul[role="listbox"]::-webkit-scrollbar-thumb {
        background-color: rgba(0, 229, 255, 0.4);
        border-radius: 10px;
    }
    </style>
"""
