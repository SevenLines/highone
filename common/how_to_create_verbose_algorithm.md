---
layout: page
permalink: how-to-create-verbose-algorithm
title: Как описать алгоритм своими словами
comments: true
---

Описываем своими словами, как будто ребенку объясняем.  Так, чтобы даже себе было понятно. Ни каких псведокодов.

{% for example in site.data.examples %}

<h2> Пример №{{ forloop.index }} </h2>

<div class="task-description" markdown="0">
<span class="task-title">Постановка задачи: </span><span class="task-text" markdown="1">{{example.object}}</span>
</div>

<h4 class="algorithm-verbose-header">вариант описания:</h4>

<div class="algorithm-steps" markdown="0">
{% for i in example.steps %}
    <div class="algorithm-step">
        <div class="algorithm-step-index">
            <div class="inner">{{forloop.index}}</div>
        </div>
        <span class="algorithm-step-description" markdown="1">{{i.step}}</span>
    </div>
     {% if i.steps %}
        {% assign outer_forloop = forloop %}
        {% for j in i.steps %}
        <div class="algorithm-step algorithm-step-level2">
            <div class="algorithm-step-index">
                <div class="inner">{{outer_forloop.index}}.{{forloop.index}}</div>
            </div>
            <span markdown="1" class="algorithm-step-description">{{j.step}}</span>
        </div>
        {% endfor %}
    {% endif %}
{% endfor %}
</div>

<h4 class="algorithm-verbose-code-header">код соответствующий описанию</h4>

{% highlight csharp %}
{{example.code}}
{% endhighlight %}

{% endfor %}


