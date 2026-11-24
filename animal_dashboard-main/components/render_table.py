def render_html_table(df, is_dark=False):
    if is_dark:
        table_style = "width:100%; border-collapse: collapse; color: #E2E8F0; font-size: 14px;"
        th_style = "padding: 12px; text-align: left; border-bottom: 2px solid #00E5FF; color: #00E5FF; background-color: rgba(0, 229, 255, 0.05);"
        td_style = "padding: 10px 12px; border-bottom: 1px solid #1E293B;"
    else:
        table_style = "width:100%; border-collapse: collapse; color: #2C3E2D; font-size: 14px;"
        th_style = "padding: 12px; text-align: left; border-bottom: 2px solid #2E8B57; color: #1B5E20; background-color: #F1F8E9;"
        td_style = "padding: 10px 12px; border-bottom: 1px solid #E0E0E0;"

    html = f'<table style="{table_style}"><thead><tr>'
    for col in df.columns:
        html += f'<th style="{th_style}">{col}</th>'
    html += '</tr></thead><tbody>'
    for _, row in df.iterrows():
        html += '<tr>'
        for val in row:
            html += f'<td style="{td_style}">{val}</td>'
        html += '</tr>'
    html += '</tbody></table>'
    return html
