---
layout: base
---

# Browse online

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
