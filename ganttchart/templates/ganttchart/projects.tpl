<script type="text/javascript" src="/js/tinymce/tinymce.min.js"></script>

<div class="content_block_padn">
{% url add_form %}
</div>

{% url top_menu %}

{% url user_part_project_gant %}

<br>
<div id="projects_list_content ">
{% url project_list_content %}
</div>

<script>
show_closed = '{% closed %}';
</script>