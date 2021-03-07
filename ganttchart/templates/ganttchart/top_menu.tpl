<div class="task_top_panel project_top_menu">
{% include 'ganttchart/top_menu_admin.tpl' %}
<a class="item {ACTIVE_1}" href="/projects">Mis proyectos <span id="new_count_for_worker">{NEW_COUNT_IN_USER_PROJECT}</span></a>
<a class="item {ACTIVE_3}" href="/projects?part=2&closed=1">Mis proyectos cerrados </a>
<a class="item {ACTIVE_2}" href="/projects?part=1">Ïðîåêòû, en el que participo <span id="new_count_in_part_projects">{NEW_COUNT_IN_PART_PROJECT}</span></a>
<a class="item {ACTIVE_4}" href="/projects?part=4&closed=1">Cerrado, en el que participo</a>
<div class="clear"></div>
</div>

