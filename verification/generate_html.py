import markdown
import os

with open('README.md', 'r') as f:
    text = f.read()

html = markdown.markdown(text, extensions=['extra', 'toc', 'tables'])

# Add some basic styling to mimic GitHub's dark mode
full_html = f"""
<html>
<head>
<style>
    body {{
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji";
        padding: 50px;
        line-height: 1.5;
    }}
    a {{ color: #58a6ff; text-decoration: none; }}
    table {{ border-collapse: collapse; width: 100%; margin: 16px 0; }}
    table, th, td {{ border: 1px solid #30363d; padding: 8px; }}
    tr:nth-child(even) {{ background-color: #161b22; }}
    img {{ max-width: 100%; }}
    hr {{ height: .25em; background-color: #30363d; border: 0; margin: 24px 0; }}
    blockquote {{ padding: 0 1em; color: #8b949e; border-left: .25em solid #30363d; }}
    code {{ background-color: rgba(110,118,129,0.4); padding: .2em .4em; border-radius: 6px; }}
    details {{ border: 1px solid #30363d; border-radius: 6px; padding: 10px; }}
    summary {{ cursor: pointer; font-weight: bold; }}
</style>
</head>
<body>
{html}
</body>
</html>
"""

with open('verification/readme_preview.html', 'w') as f:
    f.write(full_html)
