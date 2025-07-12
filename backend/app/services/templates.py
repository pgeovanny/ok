def gerar_html_template(conteudo):
    html = """
    <html>
    <head>
        <meta charset="utf-8">
        <title>Resumo Organizado</title>
    </head>
    <body>
        <h1>Resumo Organizado</h1>
        <pre style="font-size:14px; white-space: pre-wrap;">{}</pre>
    </body>
    </html>
    """.format(conteudo)
    return html
