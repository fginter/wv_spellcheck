---
layout: default
---

# Words starting with {{letter}}

In the table below, you can type in any word and you will be shown all the spelling errors that were found. You can also type in a wrongly-spelled word, the search is global.

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
<tr><td>D={{dist}}</td><td>{{correct}}</td><td>{{incorrect}}</td><td>{{count_correct}}</td><td>{{count_incorrect}}</td></tr>
{% endfor %}
</tbody>
</table>

<script type="text/javascript">
$(document).ready( function () {
    $('#spelltable').DataTable({ "autoFill": true,  "pageLength": 200, "lengthMenu": [ 50, 200, 500 ] });
} );
</script>
