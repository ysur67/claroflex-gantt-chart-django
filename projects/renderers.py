from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer


class CommentHtmlRenderer(TemplateHTMLRenderer):
    def get_template_context(self, data, renderer_context):
        context = {'object': data}
        response = renderer_context['response']
        if response.exception:
            data['status_code'] = response.status_code
        return context
