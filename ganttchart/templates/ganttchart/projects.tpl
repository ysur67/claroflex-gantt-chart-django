{% load static%}
{% extends "projects/base.html" %}
{% load i18n %}
{% block title %}
{% trans "Projects" %} - {% trans "Home" %}
{% endblock title %}
{% block content %}
<script type="text/javascript" src="{% static 'static/bootstrap/js/tinymce/tinymce.min.js' %}"></script>

<div class="content_block_padn">
{% add_form %}
</div>

{% top_menu %}

{% user_part_project_gant %}

<br>
<div id="projects_list_content ">
{% project_list_content %}
</div>
{% endblock %}

<script>
show_closed = '{% closed %}';
</script>