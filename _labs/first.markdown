--- 
layout: lab 
lab_id: first 
---

{% assign lab = site.data.labs[page.lab_id] %} {% assign tasks = lab.tasks | sort:"difficult"%}
{% capture recommends %}{% include_relative recommendations/first_recommends.md %}{% endcapture %}

<nav>
    <div class="nav nav-tabs">
        <a class="nav-item nav-link" data-toggle="tab" href="#nav-home" role="tab">Рекомендации</a>
        {% for category in lab.categories %}
            <a class="nav-item nav-link {%if forloop.index == 1 %} active{% endif %}" data-toggle="tab" href="#nav-tasks-{{category}}" role="tab">
            Группа задач {{category}}</a>
        {% endfor %}
    </div>
</nav>

<div class="tab-content" id="nav-tabContent">
    <div class="tab-pane" id="nav-home" role="tabpanel">
        {{ recommends | markdownify }} 
    </div>
{% for category in lab.categories %}
    <div class="tab-pane {%if forloop.index == 1 %}show active{% endif %}" id="nav-tasks-{{category}}" role="tabpanel">
        <div class="tasks-list">
            {% assign tasks_category = tasks | where: "category", category %}
            {% for task in tasks_category %}
            <div class="tasks-item tasks-item-difficulty-{{task.difficult}}">
                <div class="tasks-item-index"><div>{{forloop.index}}</div></div>
                <div class="tasks-item-description">{{task.description | markdownify}}</div>
            </div>
            {% endfor %}
        </div>
    </div>
{% endfor %}
</div>
