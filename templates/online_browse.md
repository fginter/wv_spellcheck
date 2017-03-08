---
layout: default
---

# About

This is a list of {{words|length}} spelling errors automatically extracted from the Turku Internet Parsebank. The underlying data is on the project's GitHub page.

# Browse online

In the table below, you can type in any word and you will be shown all the spelling errors that were found.

# Disclaimer

This is not a final production-quality stuff. Mostly something to give you an idea about the data. 

<table id="spelltable" class="display">
<thead>
<tr>
<th>Dist</th>
<th>Correct</th>
<th>Incorrect</th>
<th># Correct</th>
<th># Incorrect</th>
</tr>
</thead>
<tbody>
{% for dist,correct,incorrect,count_correct,count_incorrect in words %}
<tr><td>{{dist}}</td><td>{{correct}}</td><td>{{incorrect}}</td><td>{{count_correct}}</td><td>{{count_incorrect}}</td></tr>
{% endfor %}
</tbody>
</table>

<script type="text/javascript">
$(document).ready( function () {
    $('#spelltable').DataTable({ autoFill: true });
} );
</script>
