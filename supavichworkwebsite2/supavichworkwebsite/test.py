from misaka import Markdown, HtmlRenderer

rndr = HtmlRenderer()
md = Markdown(rndr)

print(md('some text'))